# Python
import sys
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

print("--------------------------------------")
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)
print("--------------------------------------")

location = '../data/sensors.csv'

print('--------------------------------------')
print('1. GET DATA')
df = pd.read_csv(location) # Read with header
# df = pd.read_csv(location, header=None) # Read without header
#df = pd.read_csv(location, names=['light', 'temperature', 'humidity']) # Read with custom header
print(df)

print('--------------------------------------')
print('2. PREPARE DATA')
# Check data type of the columns
print(df.dtypes)
# Check data type of temperature column
print('ligth dtype:')
print(df.light.dtype)

print('--------------------------------------')
print('3. ANALYZE DATA: MAX TEMPERATURE')

Sorted = df.sort_values(['temperature'], ascending=False)
print(Sorted.head(1)) # Method 1
print(df['temperature'].max()) # Method 2

print('--------------------------------------')
print('4. PRESENT DATA')
# Create graph
df['temperature'].plot()
# Maximum value in the data set
maxTemperature = df['temperature'].max()
ligth = df['light'][df['temperature'] == df['temperature'].max()].values
humidity = df['humidity'][df['temperature'] == df['temperature'].max()].values
# Text to display on graph
text = str(maxTemperature) + 'º\n' + str(ligth[0]) + ' \n' + str(humidity[0]) + '%'
# Add text to graph
plt.annotate(text, xy=(1, maxTemperature), xytext=(8, 0), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points')
df[df['temperature'] == df['temperature'].max()]  
plt.show()