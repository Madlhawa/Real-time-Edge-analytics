import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("madhawa/startEndDate")
    
def on_message(client, userdata, msg):
    try:
        print(str(msg.payload))
        startDate = str(msg.payload)[12:22]
        endDate = str(msg.payload)[45:55]
        print('Start: '+startDate)
        print('End: '+endDate)
    except:
        GPIO.cleanup()
        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()