import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'D:\College Files\DEV\spam.csv', encoding='latin-1') 
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

df['label_num'] = np.where(df['label'] == 'spam', 1, 0)

print(df.head())
print(df.info())
print(df.describe())

print("Missing values:\n", df.isnull().sum())

spam_count = df['label'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(spam_count.index, spam_count.values, color=['blue', 'red'])
plt.xlabel("Message Type")
plt.ylabel("Count")
plt.title("Spam vs Ham Distribution")
plt.show()

df['message_length'] = df['message'].apply(len)

plt.figure(figsize=(8,5))
plt.hist(df[df['label'] == 'spam']['message_length'], bins=30, alpha=0.5, color='red', label='Spam')
plt.hist(df[df['label'] == 'ham']['message_length'], bins=30, alpha=0.5, color='blue', label='Ham')
plt.xlabel("Message Length")
plt.ylabel("Frequency")
plt.title("Message Length Distribution")
plt.legend()
plt.show()

print("Average message length for spam vs ham:\n", df.groupby('label')['message_length'].mean())