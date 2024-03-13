import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'], format='%Y%m')

#change missing values to NaN
df.replace(-99, np.nan, inplace=True)

#fill NaN values
df.interpolate(method='linear', inplace=True)

#Plot avg temp
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Value'], label='Average Temperature', color='blue')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Average Temperature Time Series')
plt.legend()
plt.grid(True)
plt.show()

#histogram
plt.figure(figsize=(10, 6))
plt.hist(df['Value'].dropna(), bins=20, color='green', edgecolor='black', alpha=0.7)
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.title('Histogram of Average Temperature')
plt.grid(True)
plt.show()

#kernel density plot
plt.figure(figsize=(10, 6))
df['Value'].plot(kind='kde', color='orange')
plt.xlabel('Temperature')
plt.ylabel('Density')
plt.title('Kernel Density Plot of Average Temperature')
plt.grid(True)
plt.show()

#statistics
statistics = df.describe()
print(statistics)
