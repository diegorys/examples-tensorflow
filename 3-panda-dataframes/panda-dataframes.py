# Python
import pandas as pd
import matplotlib
lightSensor = pd.Series([234, 42, 54, 192, 242, 23])
temperatureSensor = pd.Series([23, 18, 20, 26, 30, 15])
humiditySensor = pd.Series([40, 35, 20, 57, 18, 45])
sensorsDataFrame = pd.DataFrame({
    'ligth': lightSensor,
    'temperature': temperatureSensor,
    'humidity': humiditySensor
})
#sensorsDataFrame.to_csv("sensors.csv", sep=",")
sensorsDataFrame = pd.read_csv("sensors.csv", sep=",")
print(sensorsDataFrame)
desc = sensorsDataFrame.describe()
print(desc)
head = sensorsDataFrame.head(2)
print(head)
hist = sensorsDataFrame.hist()
print(hist)