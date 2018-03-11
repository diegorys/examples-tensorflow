# Python
import pandas as pd
import matplotlib

print("--------------------------------------")
print("Pandas Version: " + pd.__version__)
print("--------------------------------------")
lightSensor = pd.Series([234, 42, 54, 192, 242, 23])
temperatureSensor = pd.Series([23, 18, 20, 26, 30, 15])
humiditySensor = pd.Series([40, 35, 20, 57, 18, 45])
sensorsDataFrame = pd.DataFrame({
    'ligth': lightSensor,
    'temperature': temperatureSensor,
    'humidity': humiditySensor
})
print("--------------------------------------")
print("DATAFRAME")
print(sensorsDataFrame)
desc = sensorsDataFrame.describe()
print("--------------------------------------")
print("DESCRIPTION")
print(desc)
head = sensorsDataFrame.head(2)
print("--------------------------------------")
print("HEAD")
print(head)
print("--------------------------------------")