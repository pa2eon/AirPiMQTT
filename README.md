# AirPiMQTT
Use the AirPi v1.2 PCB board on Rpi and use MQTT

The file airpymqtt.py file will check the next sensors:
* DHT22
* BMP085

And will send the result via MQTT to Home Assistant Core.<br>
In HA and on Rpi make the MQTT plugin (server/clinet) active and use in HA the next script code:

-- platform: mqtt <br>
  state_topic: "room/temperature" <br>
  name: Kantoor temperatuur<br>
  unit_of_measurement: '°C'<br>
  <p>
-- platform: mqtt<br>
  state_topic: "room/humidity"<br>
  name: Kantoor vochtigheid<br>
  unit_of_measurement: '%'<br> 
  <p>
-- platform: mqtt<br>
  state_topic: "room/pressure"<br>
  name: Kantoor luchtdruk<br>
  unit_of_measurement: 'hPa'<br>
    <p>
  
  With the MQTT Explorer you can test the 'send messages' from the Rpi with the AirPi PCB connected.<br>
  See http://mqtt-explorer.com/ for more info about MQTT Explorer.
