# geoip_api

## How to use

### get country code from ip

```
$ curl https://geoipapi.herokuapp.com/ip2cc/8.8.8.8;echo
US
```

### get autonomous system number from ip

```
$ curl https://geoipapi.herokuapp.com/ip2asn/8.8.8.8;echo
15169
```
### get autonomous system organization from ip

```
$ curl https://geoipapi.herokuapp.com/ip2aso/8.8.8.8;echo
Google LLC
```

## License

この製品には MaxMind が作成した GeoLite2 データが含まれており、<a href="http://www.maxmind.com">http://www.maxmind.com</a> から入手いただけます。
