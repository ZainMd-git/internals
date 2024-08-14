#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:/ai ml/mtcars.csv")

plt.hist(data['mpg'], bins=10, edgecolor='black')
plt.title('Frequency Distribution of MPG')
plt.xlabel('MPG')
plt.ylabel('Frequency')
plt.grid(True)

plt.show()


# In[ ]:





# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:/ai ml/mtcars.csv")

plt.scatter(data['wt'], data['mpg'], color='blue', edgecolor='black')

plt.title('Scatter Plot: Car Weight vs MPG')
plt.xlabel('Weight (1000 lbs)')
plt.ylabel('Miles Per Gallon (MPG)')

plt.grid(True)
plt.show()


# In[7]:


import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:/ai ml/mtcars.csv")

data['transmission'] = data['am'].map({0: 'Automatic', 1: 'Manual'})

transmission_counts = data['transmission'].value_counts()


transmission_counts.plot(kind='bar', color=['blue', 'orange'], edgecolor='black')
plt.title('Frequency Distribution of Transmission Types')
plt.xlabel('Transmission Type')
plt.ylabel('Frequency')
plt.grid(axis='y')

plt.show()


# In[ ]:





# In[10]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("D:/ai ml/mtcars.csv")

plt.figure(figsize=(8, 6))
sns.boxplot(y=data['mpg'])
plt.title('Box Plot of MPG')
plt.ylabel('MPG')
plt.show()

five_num_summary = data['mpg'].describe()[['min', '25%', '50%', '75%', 'max']]
print("Five-Number Summary:")
print(five_num_summary)


# In[14]:


import pandas as pd

file_path = "D:/ai ml/rainfall in india 1901-2015.csv"
data = pd.read_csv(file_path)

print("First few rows of the dataset:")
print(data.head())

print("\nColumns in the dataset:")
print(data.columns)

rainfall_columns = data.columns[2:14]
data['ANNUAL_RAINFALL'] = data[rainfall_columns].sum(axis=1)

division_rainfall = data.groupby('DIVISION')['ANNUAL_RAINFALL'].mean().reset_index()

sorted_division = division_rainfall.sort_values(by='ANNUAL_RAINFALL', ascending=False)

top_division = sorted_division.head(5)
print("\nTop 5 division with the highest annual rainfall:")
print(top_division)


# In[ ]:


import pandas as pd

file_path = '/mnt/data/rainfall in india 1901-2015.csv'
df = pd.read_csv(file_path)

columns_to_drop = ['Jan-Feb', 'Mar-May', 'Jun-Sep', 'Oct-Dec']

df = df.drop(columns=columns_to_drop)

print(df.head())

df.to_csv('/mnt/data/updated_rainfall_in_india_1901-2015.csv', index=False)


# In[16]:


import pandas as pd

file_path = "D:/ai ml/rainfall in india 1901-2015.csv"
data = pd.read_csv(file_path)

print(data.columns)

pivot_table = data.pivot_table(index='DIVISION', values=data.columns[2:14], aggfunc='mean')

print(pivot_table)


# In[ ]:




