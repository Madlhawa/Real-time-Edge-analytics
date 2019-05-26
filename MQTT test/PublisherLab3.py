import paho.mqtt.publish as publish
import RPi.GPIO as GPIO
import time

try:
    count = 0
    while True:
            print('Button pressed ' + str(count) + ' times.')
            publish.single("madhawa/test", count, hostname="test.mosquitto.org")
            count = count + 1
            time.sleep(0.5)
except:
    GPIO.cleanup()