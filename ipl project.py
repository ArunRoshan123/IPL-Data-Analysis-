#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[14]:


match_data = pd.read_csv("C:/Users/arunrakhsha/Desktop/ipl project/IPL Matches 2008-2020.csv")
ball_data = pd.read_csv("C:/Users/arunrakhsha/Desktop/ipl project/IPL Ball-by-Ball 2008-2020.csv")


# In[15]:


match_data.head()


# In[16]:


ball_data.head()


# In[17]:


match_data.isnull().sum()


# In[18]:


ball_data.isnull().sum()


# In[19]:


ball_data.shape


# In[20]:


match_data.columns


# In[21]:


print('Matches played so far:', match_data.shape[0])
print('\n Cities played at:', match_data['city'].unique())
print('\n Teams participated:', match_data['team1'].unique())


# In[52]:


match_data['Season'] = pd.DatetimeIndex(match_data['date']).year
match_data.head()


# In[23]:


match_per_season = match_data.groupby(['Season'])['id'].count().reset_index().rename(columns={'id':'matches'})
match_per_season


# In[60]:


sns.countplot(match_data['Season'])
plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('Season', fontsize=10)
plt.ylabel('Count', fontsize=10)
plt.title('Total matches played in each season', fontsize = 10, fontweight= "bold")


# In[26]:


season_data=match_data[['id','Season']].merge(ball_data, left_on = 'id', right_on = 'id', how = 'left').drop('id', axis = 1)
season_data.head()


# In[27]:


season=season_data.groupby(['Season'])['total_runs'].sum().reset_index()
p=season.set_index('Season')
ax = plt.axes()
ax.set(facecolor = "grey")
sns.lineplot(data=p,palette="magma") 
plt.title('Total runs in each season',fontsize=12,fontweight="bold")
plt.show()


# In[28]:


runs_per_season=pd.concat([match_per_season,season.iloc[:,1]],axis=1)
runs_per_season['Runs scored per match']=runs_per_season['total_runs']/runs_per_season['matches']
runs_per_season.set_index('Season',inplace=True)
runs_per_season


# In[29]:


toss=match_data['toss_winner'].value_counts()
ax = plt.axes()
ax.set(facecolor = "grey")
sns.set(rc={'figure.figsize':(15,10)},style='darkgrid')
ax.set_title('No. of tosses won by each team',fontsize=15,fontweight="bold")
sns.barplot(y=toss.index, x=toss, orient='h',palette="icefire",saturation=1)
plt.xlabel('# of tosses won')
plt.ylabel('Teams')
plt.show()


# In[30]:


ax = plt.axes()
ax.set(facecolor = "grey")
sns.countplot(x='Season', hue='toss_decision', data=match_data,palette="magma",saturation=1)
plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=15)
plt.xlabel('\n Season',fontsize=15)
plt.ylabel('Count',fontsize=15)
plt.title('Toss decision across seasons',fontsize=12,fontweight="bold")
plt.show()


# In[31]:


match_data['result'].value_counts()


# In[64]:


match_data.venue[match_data.result!='runs'].mode()


# In[33]:


match_data.venue[match_data.result!='wickets'].mode()


# In[65]:


match_data.venue[match_data.toss_winner=='Chennai Super Kings'][match_data.winner=='Chennai Super Kings'].mode()


# In[35]:


match_data.winner[match_data.result!='runs'].mode()


# In[36]:


match_data.winner[match_data.result!='wickets'].mode()


# In[37]:


toss = match_data['toss_winner'] == match_data['winner']
plt.figure(figsize=(10,5))
sns.countplot(toss)
plt.show()


# In[38]:


plt.figure(figsize=(12,4))
sns.countplot(match_data.toss_decision[match_data.toss_winner == match_data.winner])
plt.show()


# In[66]:


player = (ball_data['batsman']=='MS Dhoni')
df_dhoni=ball_data[player]
df_dhoni.head()


# In[68]:


df_dhoni['dismissal_kind'].value_counts().plot.pie(autopct='%1.1f%%',shadow=True,rotatelabels=True)
plt.title("Dismissal Kind",fontweight="bold",fontsize=15)
plt.show()


# In[69]:


def count(df_dhoni,runs):
    return len(df_dhoni[df_dhoni['batsman_runs']==runs])*runs


# In[70]:


print("Runs scored from 1's :",count(df_dhoni,1))
print("Runs scored from 2's :",count(df_dhoni,2))
print("Runs scored from 3's :",count(df_dhoni,3))
print("Runs scored from 4's :",count(df_dhoni,4))
print("Runs scored from 6's :",count(df_dhoni,6))


# In[47]:


match_data[match_data['result_margin']==match_data['result_margin'].max()]


# In[48]:


runs = ball_data.groupby(['batsman'])['batsman_runs'].sum().reset_index()
runs.columns = ['Batsman', 'runs']
y = runs.sort_values(by='runs', ascending = False).head(10).reset_index().drop('index', axis=1)
y


# In[49]:


ax = plt.axes()
ax.set(facecolor = "grey")
sns.barplot(x=y['Batsman'],y=y['runs'],palette='rocket',saturation=1)
plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('\n Player',fontsize=15)
plt.ylabel('Total Runs',fontsize=15)
plt.title('Top 10 run scorers in IPL',fontsize=15,fontweight="bold")


# In[50]:


ax = plt.axes()
ax.set(facecolor = "black")
match_data.player_of_match.value_counts()[:10].plot(kind='bar')
plt.xlabel('Players')
plt.ylabel("Count")
plt.title("Highest MOM award winners",fontsize=15,fontweight="bold")


# In[ ]:




