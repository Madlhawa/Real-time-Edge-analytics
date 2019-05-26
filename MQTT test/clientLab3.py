import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(24,GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    
    client.subscribe("CoreElectronics/test")
    client.subscribe("CoreElectronics/topic")
    
def on_message(client, userdata, msg):
    try:
        print(str(msg.payload))
        if str(msg.payload)=="b'1'":
            GPIO.output(24, True)
            time.sleep(0.2)
            print('Button pressed.')
        else:
            GPIO.output(24, False)
    except:
        GPIO.cleanup()
        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()