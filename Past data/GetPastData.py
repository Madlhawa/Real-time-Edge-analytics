# Import packages
import pandas as pd
from datetime import datetime
import numpy as np

#Reading predicted data and changing date column data type
pdata = pd.read_csv('/home/pi/LABS/Asingment/Real-time-Edge-analytics/PredictionDataset.csv', skiprows=0)
pdata['Date'] = pd.to_datetime(pdata['Date'])

#Selecting data according to date range
mask = (pdata['Date'] > '2013-6-1') & (pdata['Date'] < '2014-6-10')
poutput = pdata.loc[mask]

for index, row in poutput.iterrows():
    print(row['Date'], row['PredictionUntilThisMonth'])
    
    



