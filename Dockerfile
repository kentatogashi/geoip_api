FROM ubuntu:18.04
MAINTAINER kenta.togashi@example.com

RUN apt update && apt install -y software-properties-common && \
    echo | add-apt-repository ppa:maxmind/ppa && \
    apt update && apt install -y geoipupdate python3-pip git vim systemd
RUN git clone https://github.com/kentatogashi/geoip_api.git
WORKDIR /geoip_api
RUN pip3 install -r requirements.txt
RUN /usr/bin/geoipupdate -f /geoip_api/conf/GeoIP.conf

COPY service/geoip_api.service /etc/systemd/system/geoip_api.service
RUN systemctl enable geoip_api.service

EXPOSE 80
