from time import *

import smbus2
import bme280

import RPi_I2C_driver

i2c_port = 1
endereco = 0x76 
bus = smbus2.SMBus(i2c_port)
bme280_parameters = bme280.load_calibration_params(bus, endereco)

while True:
    dado = bme280.sample(bus, endereco, bme280_parameters)

    temp  = dado.temperature
    humid = dado.humidity
    pres = dado.pressure
    
    print(f"P {pres:.2f}")
    print(f"U {humid:.2f} T {temp:.2f}")

    mylcd = RPi_I2C_driver.lcd()

    mylcd.lcd_display_string(f"P {pres:.2f}", 1)
    mylcd.lcd_display_string(f"U {humid:.2f} T {temp:.2f}", 2)

    sleep(1)