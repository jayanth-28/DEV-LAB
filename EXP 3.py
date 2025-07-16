import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arr1 = np.arange(1, 6)                    
arr2 = np.arange(1, 7).reshape(2, 3)  

print("Original Array:", arr1)
print("Array * 2:", arr1 * 2)            
print("Sliced Array (step 2):", arr1[::2])
print("Flattened 2D Array:", arr2.ravel())
print("Reshaped 2D Array (3×2):\n", arr2.reshape(3, 2))

data = {
    'Name':  ['Alice', 'Bob', 'Charlie'],
    'Age':   [25, 30, 35],
    'Score': [85, 90, 88]
}
df = pd.DataFrame(data)
df['Passed'] = df['Score'] >= 90    

print("\nDataFrame:")
print(df)
print("\nQuick Summary:")
print(df.describe(include='all'))

plt.style.use('ggplot')                   

plt.figure()
plt.plot(df['Name'], df['Score'], marker='o', linewidth=2)
plt.title('Scores of Students')
plt.xlabel('Name')
plt.ylabel('Score')
for x, y in zip(df['Name'], df['Score']):
    plt.text(x, y + 0.5, y, ha='center')   
plt.tight_layout()
plt.show()

plt.figure()
plt.scatter(df['Age'], df['Score'], s=100)
plt.title('Age vs Score')
plt.xlabel('Age')
plt.ylabel('Score')
plt.tight_layout()
plt.show()

explode = [0.05] * len(df)                 
plt.figure()
plt.pie(df['Score'],
        labels=df['Name'],
        autopct='%1.1f%%',
        startangle=90,
        explode=explode,
        shadow=True)
plt.title('Score Distribution')
plt.tight_layout()
plt.show()

plt.figure()
plt.bar(df['Name'], df['Score'], color='skyblue', edgecolor='black')
plt.title('Bar Chart of Student Scores')
plt.xlabel('Name')
plt.ylabel('Score')
for i, (name, score) in enumerate(zip(df['Name'], df['Score'])):
    plt.text(i, score + 0.5, str(score), ha='center')
plt.tight_layout()
plt.show()
