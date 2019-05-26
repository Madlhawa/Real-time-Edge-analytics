import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import pandas as pd
from datetime import datetime
import numpy as np

server = "broker.hivemq.com"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("madhawa/future/startEndDate")
    
def on_message(client, userdata, msg):
    print(str(msg.payload))
    startDate = str(msg.payload)[12:22]
    endDate = str(msg.payload)[45:55]
    print('Start: '+startDate)
    print('End: '+endDate)

    mask = (pdata['Date'] > startDate) & (pdata['Date'] < endDate)
    poutput = pdata.loc[mask]

    for index, row in poutput.iterrows():
        print(row['Date'], row['PredictionUntilThisMonth'])
        publish.single("madhawa/future/data", row['PredictionUntilThisMonth'], hostname=server)
        
    print("Done!")
    
     
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#Reading predicted data and changing date column data type
pdata = pd.read_csv('/home/pi/LABS/Asingment/Real-time-Edge-analytics/PredictionDataset.csv', skiprows=0)
pdata['Date'] = pd.to_datetime(pdata['Date'])

client.connect(server, 1883, 60)
client.loop_forever()