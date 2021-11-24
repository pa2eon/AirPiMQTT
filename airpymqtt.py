#
# Adapted from https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/ 
# TemperatureMQTT.py (c) Jonathan Haddock, @joncojonathan, 2020
# also using guidance from https://appcodelabs.com/introduction-to-iot-build-an-mqtt-server-using-raspberry-pi
# and http://www.steves-internet-guide.com/into-mqtt-python-client/
# Many thanks!
# Added more items for AirPi PCB

import Adafruit_DHT
import paho.mqtt.client as paho
import os
import time

# BMP085 via I2C bus
import Adafruit_BMP.BMP085 as BMP085
BMP_SENSOR = BMP085.BMP085()

# Define constants
# Sensor type (Adafruit_DHT.DHT11 or Adafruit_DHT.DHT22)
DHT_SENSOR = Adafruit_DHT.DHT22


# Configure GPIO pins
ROOM_PIN = 4                    # Room temp and room humidity

# MQTT details
MQTT_BROKER="127.0.0.1"
MQTT_PORT=1883

# Output file name
LOGFILE = "/home/pi/sensors.csv"

##########################################################
# Only edit below if you know what you're doing!
##########################################################

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
client1= paho.Client("control1")                    #create client object
client1.on_publish = on_publish                     #assign function to callback
client1.connect(MQTT_BROKER,MQTT_PORT)              #establish connection

try:
    f = open(LOGFILE, 'a+')
    if os.stat(LOGFILE).st_size == 0:
            f.write('Date,Time,Sensor,Temperature,Humidity,Pressure\r\n')
except:
    pass

roomHumidity, roomTemperature = Adafruit_DHT.read_retry(DHT_SENSOR, ROOM_PIN)
roomPressure = BMP085.BMP085(mode=BMP085.BMP085_STANDARD)

#print('Pressure = {0:2.2f} hPa'.format(BMP_SENSOR.read_pressure()))
print("Pressure %.2f hPa" % (BMP_SENSOR.read_pressure()/100))
    
if roomHumidity is not None and roomTemperature is not None:
    ret= client1.publish("room/temperature","{0:0.1f}".format(roomTemperature))
    ret= client1.publish("room/humidity","{0:0.1f}".format(roomHumidity))
    #ret= client1.publish("room/pressure","{0:0.2f}".format(BMP_SENSOR.read_pressure()))
    ret= client1.publish("room/pressure","%.1f" % (BMP_SENSOR.read_pressure()/100))
    #f.write('{0},{1},Room,{2:0.1f}*C,{3:0.1f}%,{4:0.2f}Pa\r\n'.format(time.strftime('%y-%m-%d'), time.strftime('%H:%M'), roomTemperature, roomHumidity, roomPressure))
    #f.write('{0},{1},Room,{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%y-%m-%d'), time.strftime('%H:%M'), roomTemperature, roomHumidity))
else:
    ret= client1.publish("room/temperature","FAILED")
    print("Failed to retrieve data from room sensor")

def on_disconnect(client, userdata, rc):
   print("client disconnected ok")
client1.on_disconnect = on_disconnect
client1.disconnect()

