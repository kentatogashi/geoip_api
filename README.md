# geoip_api

## Requirements

- Ubuntu 18.04

## Setup

```
# cd /
# git clone https://github.com/kentatogashi/geoip_api
# apt update && apt install -y software-properties-common && \
echo | add-apt-repository ppa:maxmind/ppa && \
# apt update && apt install -y geoipupdate python3-pip git vim systemd
# git clone https://github.com/kentatogashi/geoip_api.git
# cd /geoip_api
# pip3 install -r requirements.txt
# /usr/bin/geoipupdate -f /geoip_api/conf/GeoIP.conf
```

## Start

```
# python3 main.py
```

## Example

```
# curl http://0.0.0.0/api/cc/8.8.8.8; echo
US
# curl http://0.0.0.0/api/asn/8.8.8.8; echo
15169
# curl http://0.0.0.0/api/aso/8.8.8.8; echo
Google LLC
```
