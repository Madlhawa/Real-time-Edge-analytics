# Import packages
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

temp1 = pd.read_csv('/home/pi/LABS/IOTFinal/TempData1.csv', skiprows=0)
temp1.head
temp1.info()

#---------------------------------------------------------------------------------------------

#To fix the date problem, divide the dates
df1=temp1.loc[0:1143,:]
df2=temp1.loc[1144:,:]

#-------------------------------------------------------------------------------------------

#converting the dates to python data types
df1['Date'] = pd.to_datetime(df1['Date'])
df2['Date'] = pd.to_datetime(df2['Date'])

#---------------------------------------------------------------------------------------

#Appending the two datasets
dataset=df1.append(df2)

#--------------------------------------------------------------------------------------

#divide into train and validation set
#2344 - 2000-01-01
#2487 - 2011-12-01
#2488 - 2012-01-01
#2507 - 2013-08-01
#train = dataset.loc[2344:2487:][:int(1*(len(dataset.loc[2344:2487:])))]
#test = dataset.loc[2488:2507:][int(1*(len(dataset.loc[2488:2507:]))):]
train=dataset.loc[2344:2487,:]
test=dataset.loc[2488:,:]

#-----------------------------------------------------------------------------------------------------------------

#building the model
from pyramid import auto_arima
model = auto_arima(train['Avg_Temp'], trace=True, error_action='ignore', suppress_warnings=True)

#-------------------------------------------------------------------------------------------------------

forecast = model.predict(n_periods=len(test['Avg_Temp']))
forecast = pd.DataFrame(forecast,index = test['Avg_Temp'].index,columns=['Prediction'])
forecast.head()

#---------------------------------------------------------------------------------------------------

#PREDICT FROM 2013-Sept to 2014-Aug
forecastTest = model.predict(n_periods=24)
forecastTest = pd.DataFrame(forecastTest,columns=['PredictionUntilThisMonth'])
forecastTest.head(24)

#------------------------------------------------------------------------------------------------------



