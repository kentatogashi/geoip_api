#!/bin/sh
ROOT_DIR=$(cd $(dirname $0)/../; pwd)
rm -rf $ROOT_DIR/GeoLite2-*
wget https://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.tar.gz -P $ROOT_DIR
tar xvfz $ROOT_DIR/GeoLite2-Country.tar.gz
mv GeoLite2-Country_*/GeoLite2-Country.mmdb mmdb/GeoLite2-Country.mmdb
wget https://geolite.maxmind.com/download/geoip/database/GeoLite2-ASN.tar.gz -P $ROOT_DIR
tar xvfz $ROOT_DIR/GeoLite2-ASN.tar.gz
mv $ROOT_DIR/GeoLite2-ASN_*/GeoLite2-ASN.mmdb $ROOT_DIR/mmdb/GeoLite2-ASN.mmdb
rm -rf $ROOT_DIR/GeoLite2-*
