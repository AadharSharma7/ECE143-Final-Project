#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('../data/Portfolio_by_percentile_income.csv')
df = df.dropna()
df = df.reset_index(drop=True)
df['Category'] = df['Category'].replace('Less than 20', '0-19.9')
df


# In[3]:


categories = ['0-19.9', '20-39.9', '40-59.9', '60-79.9', '80-89.9', '90-100']

for category in categories:
    filtered_df = df[df['Category'] == category]
    filtered_df = filtered_df.reset_index(drop=True)
    plt.figure(figsize=(10, 6))
    sns.barplot(x='year', y='Net_Worth', data=filtered_df)
    plt.title(f'Net Worth (in thousands) for {category}')
    plt.tight_layout()
    plt.show()


# In[4]:


column_names = df.columns.tolist()

column_names = column_names[2:]

for col in column_names:
    pivot_df = df.pivot(index='Category', columns='year', values=col)
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot_df, cmap='YlGnBu', annot=True, fmt=".1f", linewidths=0.5)
    plt.title(f'{col} Heatmap')
    plt.xlabel('Year')
    plt.ylabel('Category')
    plt.show()

