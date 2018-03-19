# Python
import sys
from numpy import random
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

print("--------------------------------------")
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)
print("--------------------------------------")

location = '../../data/sensors.csv'

print('--------------------------------------')
print('1. CREATE DATA')

# METHOD 1
# lightSensor = pd.Series([234, 42, 54, 192, 242, 23])
# temperatureSensor = pd.Series([23, 18, 20, 26, 30, 15])
# humiditySensor = pd.Series([40, 35, 20, 57, 18, 45])
# sensorsDataFrame = pd.DataFrame({
#     'light': lightSensor,
#     'temperature': temperatureSensor,
#     'humidity': humiditySensor,
# })
# END METHOD 1

# METHOD 2
# sensors = ['light', 'temperature', 'humidity']
# light = [234, 42, 54, 192, 242, 23]
# temperature = [23, 18, 20, 26, 30, 15]
# humidity = [40, 35, 20, 57, 18, 45]
# sensorsDataSet = list(zip(light, temperature, humidity))
# sensorsDataFrame = pd.DataFrame(data = sensorsDataSet, columns=sensors)
# END METHOD 2

# METHOD 3
random.seed(500)
sensors = ['light', 'temperature', 'humidity']
light = [random.randint(low=0,high=1024) for i in range(1000)]
temperature = [random.randint(low=15,high=35) for i in range(1000)]
humidity = [random.randint(low=18,high=65) for i in range(1000)]
sensorsDataSet = list(zip(light, temperature, humidity))
sensorsDataFrame = pd.DataFrame(data = sensorsDataSet, columns=sensors)
# END METHOD 3

print("--------------------------------------")
print("DATAFRAME")
print(sensorsDataFrame)
desc = sensorsDataFrame.describe()
print('--------------------------------------')
# sensorsDataFrame.to_csv(location,index=False,header=False)
sensorsDataFrame.to_csv(location,index=False)
print('-> Exported to ' + location)

print("--------------------------------------")
print("DESCRIPTION")
print(desc)

info = sensorsDataFrame.info()
print("--------------------------------------")
print("INFO")
print(info)

head = sensorsDataFrame.head(2)
print("--------------------------------------")
print("HEAD")
print(head)

tail = sensorsDataFrame.tail(2)
print("--------------------------------------")
print("TAIL")
print(tail)

print("--------------------------------------")
print("HIST")
sensorsDataFrame.hist('light')
plt.show()