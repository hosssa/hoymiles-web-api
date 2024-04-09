# hoymiles-web-api

Simple web api to serve data from Hoymiles DTUs and the HMS-XXXXW-2T HMS microinverters in json format. It uses the [hoymiles-wifi](https://github.com/suaveolent/hoymiles-wifi) python library to retrieve data from the DTU.

Prerequesite: The DTU needs to be registered in your local network (wifi).

**Disclaimer: This project is not affiliated with Hoymiles. It is an independent project developed to provide tools for interacting with Hoymiles HMS-XXXXW-2T series micro-inverters featuring integrated WiFi DTU. Any trademarks or product names mentioned are the property of their respective owners.**

## local usage
```sh
pip install -r requirements.txt
python3 app.py
```

Access via [http://localhost:5000/DTUBI-<DTU_serial_number>](http://localhost:5000/DTUBI-<DTU_serial_number>)[^1] to get a list of all available endpoints.

1. /getRealDataNew/DTUBI-<DTU_serial_number>
2. /getRealDataHms/DTUBI-<DTU_serial_number>
3. /getRealData/DTUBI-<DTU_serial_number>
4. /getConfig/DTUBI-<DTU_serial_number>
5. /networkInfo/hoDTUBI-<DTU_serial_number>
6. /appInformationData/DTUBI-<DTU_serial_number>
7. /appGetHistPower/DTUBI-<DTU_serial_number>
8. /getInformationData/DTUBI-<DTU_serial_number>
9. /heartbeat/DTUBI-<DTU_serial_number>

[^1]: If the DTU hostname *DTUBI-<DTU_serial_number>* does not work use the DTU ip address instead.

## docker usage

### duild docker image
```sh
docker build --tag hoymiles-web-api .
```

### run docker image
```sh
docker run -d -p 5000:5000 --name hoymiles-web-api hoymiles-web-api 
```
Access via [http://localhost:5000/DTUBI-<DTU_serial_number>](http://localhost:5000/DTUBI-<DTU_serial_number>)

### save docker image
```sh
docker save hoymiles-web-api | gzip > build/hoymiles-web-api.tar.gz
```

## attribution

A special thank you for the inspiration to:

* [suaveolent](https://github.com/suaveolent): [hoymiles-wifi](https://github.com/suaveolent/hoymiles-wifi)