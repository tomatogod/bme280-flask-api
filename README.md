# bme280-flask-api

Description
-----------
Python3 app to expose sensor readings to simple api using flask.

Hardware
-------------
raspberrypi (>3) (enable l2c).
bme280 sensor (https://www.amazon.co.uk/KeeYees-Temperature-Humidity-Atmospheric-Barometric-3-x-BME280-Digital-Sensor-Module/).

Example usage
-------------
install sensor to GPIO pins as described (https://pypi.org/project/RPi.bme280/).
install as a service - copy bmiflaskapi.service to /etc/systemd/system/bmiflaskapi.service.
start service (sudo systemctl start bmiflaskapi.service).
web browse to http://<hostname/ip>:5000 - summary readings from bmi280 sensor.

Python modules
-------------
pip3 install flask.
pip3 install RPi.bmi280.
pip3 install smbus2.
