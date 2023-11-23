#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:





# In[6]:


final_df = pd.read_csv('./transformed_data.csv')
final_df.head(15)


# In[ ]:





# In[7]:


values1 = ['India', 'United States of America', 'China']

graph1_data = final_df[final_df['Country'].isin(values1)]


# In[ ]:





# In[8]:


sns.set(style="whitegrid")  # Set the style (optional)
g = sns.catplot(
    x='Date_reported', y='Cumulative_cases', hue='Country',
    data=graph1_data, kind='bar',
    height=6, aspect=1.5  # Adjust the size and aspect ratio
)


# In[ ]:





# In[10]:


values2 = ['India', 'United States of America', 'China','Romania', 'South Africa', 'Australia']

graph2_data = final_df[final_df['Country'].isin(values2)]


# In[ ]:





# In[11]:


a = graph2_data['Country'].unique()
b = graph2_data['TOTAL_VACCINATIONS'].unique()

ax = sns.barplot(x=a, y=b)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")

plt.xlabel('Countries')
plt.ylabel('Total_Vaccinations')


# In[ ]:





# In[ ]:


print("visualized sucessfully!!!")

