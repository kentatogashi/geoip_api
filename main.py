#!/usr/bin/python3

import os
import sys
import logging

ver = '.'.join(map(str, sys.version_info[0:2]))
sys.path.append(os.path.join(os.path.dirname(__file__), '.././local/python%s/site-packages' % ver))
from flask import Flask, abort, make_response, request
import geoip2.database

PORT=80
MMDB_CC='/usr/share/GeoIP/GeoLite2-Country.mmdb'
MMDB_ASN='/usr/share/GeoIP/GeoLite2-ASN.mmdb'
LOG=os.path.join(os.path.dirname(__file__), 'log/api.log')

logger = logging.getLogger('werkzeug')
handler = logging.FileHandler(LOG)
logger.addHandler(handler)

api = Flask(__name__)

def ip2cc(ip):
    reader = geoip2.database.Reader(MMDB_CC)
    cc = reader.country(ip).country.iso_code
    return cc

def ip2asn(ip):
    reader = geoip2.database.Reader(MMDB_ASN)
    asn = reader.asn(ip).autonomous_system_number
    return asn

def ip2aso(ip):
    reader = geoip2.database.Reader(MMDB_ASN)
    aso = reader.asn(ip).autonomous_system_organization
    return aso

@api.route('/api/cc/<ip>', methods=['GET'])
def get_cc(ip):
    return make_response(ip2cc(ip))

@api.route('/api/asn/<ip>', methods=['GET'])
def get_asn(ip):
    return make_response(str(ip2asn(ip)))

@api.route('/api/aso/<ip>', methods=['GET'])
def get_aso(ip):
    return make_response(ip2aso(ip))

@api.errorhandler(500)
def invalid_ip(error):
    return make_response('Internal Server Error', 500)

@api.errorhandler(404)
def not_found(error):
    return make_response('Not Found', 404)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=PORT)
