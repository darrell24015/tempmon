"""
Raspberry Pi 4 CPU Temperature Monitor
Author: Darrell Little http://yatb.devcali.co
Date: 07/08/2019
Based on the Raspberry Pi Foundation Project
https://projects.raspberrypi.org/en/projects/temperature-log
Data logged on AdafruitIO
https://io.adafruit.com/dlittle55/dashboards/my-rpi4-dashboard
"""
from gpiozero import CPUTemperature
from time import sleep, strftime, time
import creds
from Adafruit_IO import Client

# Setup connection to AdafruitIO REST client
adafruit_io_username = creds.username
adafruit_io_key = creds.key
aio = Client(adafruit_io_username, adafruit_io_key)
delay = 120

cpu_temp = aio.feeds('raspberrypi4')

cpu = CPUTemperature()

def write_temp(temp):
    with open("/home/pi/logs/cpu_temp.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

try:
    while True:
        temp = cpu.temperature
        print(f"Data logged: {temp}")
        write_temp(temp)
        aio.send(cpu_temp.key, temp)
        sleep(delay)
except KeyboardInterrupt:
    print(" Keyboard Interrupt - Program Cancelled")
except IOError:
    print("There was an error opening the file")
except Exception as e :
    print(f"There was an unknown error: {e}")


