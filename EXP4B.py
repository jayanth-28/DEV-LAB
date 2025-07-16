import pandas as pd
df = pd.read_csv(r'D:\College Files\DEV\work_hours.csv')
grouped = df.groupby('Department')['HoursWorked'].agg(['sum', 'mean']).reset_index()
grouped.columns = ['Department', 'Total_Hours', 'Average_Hours']

pivot_table = grouped.set_index('Department')
top_department = pivot_table['Average_Hours'].idxmax()

print("Summary Report: Total and Average Hours Worked per Department\n")
print(pivot_table)
print("\nDepartment with Highest Average Working Hours:", top_department)

