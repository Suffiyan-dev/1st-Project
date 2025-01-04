#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data = pd.read_csv("creditcard.csv")


# In[3]:


data.head()


# In[4]:


# How many rows and columns are in the dataset?
data.shape


# What are the column names and their data types?

# In[5]:


data.columns


# In[6]:


data.dtypes


# In[7]:


# Are there any missing or null values in the dataset?
data.isnull().sum()


# In[8]:


# How many transactions are fraudulent, and how many are legitimate?
fraudulent_transactions =data['Class'].sum()
legitimate_transaction = len(data) - fraudulent_transactions
print("Fraudulent Transactions: ",fraudulent_transactions)
print("Legitimate Transactions: ",legitimate_transaction)


# In[9]:


# What percentage of transactions are fraudulent?
(fraudulent_transactions / len(data))*100


# In[10]:


# What are the minimum, maximum, mean, and median values for numerical columns like Amount?
min_amount = min(data['Amount'])
max_amount = max(data['Amount'])
mean_amount = data['Amount'].mean()
median_amount = data['Amount'].median()

print("Minimum Amount:",min_amount)
print("Maximum Amount:",max_amount)
print("Mean Amount:",mean_amount)
print("Median Amount:",median_amount)


# In[11]:


# What is the maximum transaction amount in the dataset, and is it  fraudulent?
max_amount = data['Amount'].max()
is_fradualent = data[data['Amount']==max_amount]['Class'].iloc[0]
print("The transaction is fradulatent:","yes"if is_fradualent == 1 else "NO")


# In[5]:


# Can we create a bar chart showing the count of fraudulent vs legitimate transactions?
sns.countplot(x=data['Class'])
plt.title("Count Of Fradualent vs Legitimate transactions")


# In[9]:


# What does the histogram of transaction amounts look like?
sns.histplot(data['Amount'],bins=40)


# In[14]:


# Can we use a heatmap to visualize the correlation between numerical features?
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix,cmap="coolwarm")


# In[ ]:




