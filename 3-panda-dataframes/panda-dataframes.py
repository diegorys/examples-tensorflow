# Python
import pandas as pd
lightSensor = pd.Series([234, 42, 54, 192, 242, 23])
temperatureSensor = pd.Series([23, 18, 20, 26, 30, 15])
humiditySensor = pd.Series([40, 35, 20, 57, 18, 45])
sensors = pd.DataFrame({
    'Ligth': lightSensor,
    'Temperature': temperatureSensor,
    'Humidity': humiditySensor
})
print(sensors)