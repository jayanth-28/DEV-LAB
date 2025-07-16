import pandas as pd
df = pd.read_csv(r'D:\College Files\DEV\temperature_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

grouped = df.groupby(['City', 'Month'])['Temperature'].sum().reset_index()
pivot_table = grouped.pivot(index='City', columns='Month', values='Temperature')
pivot_table.columns = ['June', 'July', 'August']
pivot_table['Summer_Total'] = pivot_table[['June', 'July', 'August']].sum(axis=1)
top_city = pivot_table['Summer_Total'].idxmax()

print("Month-wise Summary Table (Sum of Temperatures):\n")
print(pivot_table[['June', 'July', 'August']])
print("\nCity with Highest Total Temperature in Summer Months:", top_city)
