import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import pandas as pd
from datetime import datetime
import numpy as np

server = "broker.hivemq.com"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("madhawa/startEndDate")
    
def on_message(client, userdata, msg):
    print(str(msg.payload))
    startDate = str(msg.payload)[12:22]
    endDate = str(msg.payload)[45:55]
    print('Start: '+startDate)
    print('End: '+endDate)
    
    mask = (dataset['Date'] > startDate) & (dataset['Date'] < endDate)
    output = dataset.loc[mask]

    for index, row in output.iterrows():
        print(row['Date'], row['Avg_Temp'])
        publish.single("madhawa/pastData", row['Avg_Temp'], hostname=server)
    
     
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

temp1 = pd.read_csv('/home/pi/LABS/IOTFinal/TempData1.csv', skiprows=0)

#To fix the date problem, divide the dates
df1=temp1.loc[0:1143,:]
df2=temp1.loc[1144:,:]

#converting the dates to python data types
df1['Date'] = pd.to_datetime(df1['Date'])
df2['Date'] = pd.to_datetime(df2['Date'])

#Appending the two datasets
dataset=df1.append(df2)

client.connect(server, 1883, 60)
client.loop_forever()