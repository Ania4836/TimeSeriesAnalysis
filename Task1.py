import pandas as pd
import matplotlib.pyplot as plt

#csv files
poland_df = pd.read_csv("poland_vacation.csv")
us_df = pd.read_csv("us_vacation.csv")
uk_df = pd.read_csv("uk_vacation.csv")

#datetime
poland_df['Month'] = pd.to_datetime(poland_df['Month'])
poland_df.set_index('Month', inplace=True)

us_df['Month'] = pd.to_datetime(us_df['Month'])
us_df.set_index('Month', inplace=True)

uk_df['Month'] = pd.to_datetime(uk_df['Month'])
uk_df.set_index('Month', inplace=True)

#rename columns
poland_df.rename(columns={"vacation: (Polska)": "PL"}, inplace=True)
us_df.rename(columns={"vacation: (Stany Zjednoczone)": "US"}, inplace=True)
uk_df.rename(columns={"vacation: (Wielka Brytania)": "UK"}, inplace=True)

#combine search
combined_df = pd.concat([poland_df, us_df, uk_df], axis=1)

#plot for all countries
combined_df.plot(figsize=(12, 6))
plt.title("Search Trend for 'Vacation' Over Time")
plt.xlabel("Year")
plt.ylabel("Search Count")
plt.grid(True)
plt.show()

#statistics
print(combined_df.describe())

#three histograms in one plot
combined_df.plot(kind='hist', bins=20, alpha=0.5, figsize=(12, 6))
plt.title("Histogram of 'Vacation' Search Counts")
plt.xlabel("Search Count")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

#three kernel densities
combined_df.plot(kind='kde', figsize=(12, 6))
plt.title("Kernel Density Estimation of 'Vacation' Search Counts")
plt.xlabel("Search Count")
plt.ylabel("Density")
plt.grid(True)
plt.show()
