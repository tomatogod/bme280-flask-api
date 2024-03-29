# bme280-flask-api

Description
-----------
Python3 app to expose sensor readings to simple api using flask <br />

Hardware
-------------
raspberrypi (>3) (enable l2c)<br />
bme280 sensor (https://www.amazon.co.uk/KeeYees-Temperature-Humidity-Atmospheric-Barometric-3-x-BME280-Digital-Sensor-Module/)<br />
![image](https://user-images.githubusercontent.com/12842988/207841794-537d670a-0218-4c61-8329-e0ed78c9ebac.png)
![image](https://user-images.githubusercontent.com/12842988/207841871-8e7b839b-dbe8-48a0-94f1-ab923bac6ff5.png)
![image](https://user-images.githubusercontent.com/12842988/207846012-f439f712-a16b-4b6c-a8d3-a6f009984dac.png)


Example usage
-------------
install sensor to GPIO pins as described (https://pypi.org/project/RPi.bme280/)<br />
install as a service - copy bmiflaskapi.service to /etc/systemd/system/bmiflaskapi.service<br />
start service (sudo systemctl start bmiflaskapi.service)<br />
web browse to http://<hostname/ip>:5000 - summary readings from bmi280 sensor<br />

Python modules
-------------
pip3 install flask (https://flask.palletsprojects.com/)<br /> 
pip3 install RPi.bmi280 (https://github.com/rm-hull/bme280)<br /> 
pip3 install smbus2 (https://pypi.org/project/smbus2/)<br /> 
