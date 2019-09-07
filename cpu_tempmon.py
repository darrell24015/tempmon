"""
Raspberry Pi 4 CPU Temperature Monitor
Author: Darrell Little http://yatb.devcali.co
Date: 07/08/2019
Updated: 07/23/2019
Based on the Raspberry Pi Foundation Project
https://projects.raspberrypi.org/en/projects/temperature-log
Data logged on AdafruitIO
https://io.adafruit.com/dlittle55/dashboards/my-rpi4-dashboard
Creating an AdafruitIO Data Feed
https://learn.adafruit.com/adafruit-io-basics-feeds/creating-a-feed
"""
# Import the libraries needed
from gpiozero import CPUTemperature # Capture CPU temperature
from time import sleep, strftime, time
import psutil # Capture CPU usage
import creds
from Adafruit_IO import Client

# Setup connection to AdafruitIO REST client
adafruit_io_username = creds.username
adafruit_io_key = creds.key
aio = Client(adafruit_io_username, adafruit_io_key)
delay = 240

# Create an instance for each data feed using the key
cpu_temp = aio.feeds('cpu-temp')
cpu_load = aio.feeds('cpu-load')

# Create a gpiozero object
cpu = CPUTemperature()

# Function for writing data to a file
def write_temp(temp,load):
    with open("/home/pi/logs/cpu_temp_load.csv", "a") as log:
        log.write("{0},{1},{2}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp),str(load)))

try:
    while True:
        temp = cpu.temperature
        avg = psutil.cpu_percent()
        print(f"CPU Temp: {temp} C")
        print(f"CPU Load: {avg} %")
        write_temp(temp,avg)
        aio.send(cpu_temp.key, temp)
        aio.send(cpu_load.key, avg)
        sleep(delay)
except KeyboardInterrupt:
    print(" Keyboard Interrupt - Program Cancelled")
except IOError:
    print(" There was an error opening the file")
except Exception as e :
    print(f" There was an unknown error: {e}")
