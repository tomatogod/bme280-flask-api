# Python3 app to expose sensor readings to simple api
# -------------
# Example usage
# web browse to http://host:5000/temp - output temperature from sensor
# -------------
# Prerequisites
# -------------
# raspberrypi
# bmi280 sensor
# enable l2c
# -------------
# pip3 install flask
# pip3 install RPi.bmi280
# pip3 install smbus2

# import modules
from flask import Flask
import bme280 #RPi.bmi280
import smbus2

# sensor setup
port = 1
address = 0x76
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)
app = Flask(__name__)

# root site gives you summary of all readings
@app.route('/')
def root():
    data = bme280.sample(bus, address, calibration_params)
    temp = str(round(data.temperature, 2))
    pressure = str(round(data.pressure, 2))
    humidity = str(round(data.humidity, 2))
    result = ("Temperature: " + temp + ", Pressure: " + pressure + ", Humidity: " + humidity)   
    return result

# /temp site for just temperature
@app.route('/temp')
def temp():
    data = bme280.sample(bus, address, calibration_params)
    temp = str(round(data.temperature, 3))
    return temp

# /pressure site for just pressure
@app.route('/pressure')
def pressure():
    data = bme280.sample(bus, address, calibration_params)
    pressure = str(round(data.pressure, 3))
    return pressure

# /humidity site for just humidity
@app.route('/humidity')
def humidity():
    data = bme280.sample(bus, address, calibration_params)
    humidity = str(round(data.humidity, 3))
    return humidity

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)