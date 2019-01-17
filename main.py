#!/usr/bin/python3

import os
import sys

ver = '.'.join(map(str, sys.version_info[0:2]))
sys.path.append(os.path.join(os.path.dirname(__file__), '.././local/python%s/site-packages' % ver))
from flask import Flask, make_response, request
import geoip2.database

PORT=80
MMDB_CC=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'mmdb/GeoLite2-Country.mmdb')
MMDB_ASN=os.path.join(os.path.abspath(os.path.dirname(__file__)), 'mmdb/GeoLite2-ASN.mmdb')
app = Flask(__name__)

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

@app.route('/', methods=['GET'])
def get_license():
    text = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset='UTF-8'>
    <title>geoip api</title>
    </head>
    <body>
    <p>IPアドレスから、国名、AS番号、AS組織を取得するAPIです。</p>
    <p>使い方は、<a href= 'https://github.com/kentatogashi/geoip_api/blob/master/README.md'>https://github.com/kentatogashi/geoip_api/blob/master/README.md</a>を参照してください。</p>
    <p>この製品には MaxMind が作成した GeoLite2 データが含まれており、<a href="http://www.maxmind.com">http://www.maxmind.com</a> から入手いただけます。</p>
    </body>
    </html>
    """
    return make_response(text)

@app.route('/ip2cc/<ip>', methods=['GET'])
def get_cc(ip):
    return make_response(ip2cc(ip))

@app.route('/ip2asn/<ip>', methods=['GET'])
def get_asn(ip):
    return make_response(str(ip2asn(ip)))

@app.route('/ip2aso/<ip>', methods=['GET'])
def get_aso(ip):
    return make_response(ip2aso(ip))

@app.errorhandler(500)
def invalid_ip(error):
    return make_response('Internal Server Error', 500)

@app.errorhandler(404)
def not_found(error):
    return make_response('Not Found', 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
