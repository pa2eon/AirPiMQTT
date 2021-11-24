# AirPiMQTT
Use the AirPi v1.2 PCB board on Rpi and use MQTT

The file airpymqtt.py file will check the next sensors:
* DHT22
* BMP085

And will send the result via MQTT to Home Assistant Core.
In HA and on Rpi make the MQTT plugin (server/clinet) active and use in HA the next script code:

- platform: mqtt
  state_topic: "room/temperature"
  name: Kantoor temperatuur
  unit_of_measurement: '°C'
      
- platform: mqtt
  state_topic: "room/humidity"
  name: Kantoor vochtigheid
  unit_of_measurement: '%' 
  
- platform: mqtt
  state_topic: "room/pressure"
  name: Kantoor luchtdruk
  unit_of_measurement: 'hPa' 
  
  With the MQTT Explorer you can test the 'send messages' from the Rpi with the AirPi PCB connected.
  See http://mqtt-explorer.com/ for more info about MQTT Explorer.
