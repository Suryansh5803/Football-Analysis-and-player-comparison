#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib as plt
import plotly.express as px


# In[4]:


df = pd.read_csv("C:/Users/91936/OneDrive/Desktop/Data.csv")


# In[5]:


df


# In[6]:


df=df.drop(['Country'], axis=1)


# In[7]:


df


# In[8]:


df = df[df['League'] == 'La Liga']


# In[9]:


df


# In[10]:


df=df.drop(['League'], axis=1)


# In[11]:


df=df.drop(['xG','xG Per Avg Match'], axis=1)


# In[12]:


df


# In[13]:


df['Year'] = pd.to_datetime(df['Year'], format='%Y')


# In[14]:


df = df.set_index('Year')


# In[15]:


df


# In[16]:


df.dropna()


# In[17]:


import plotly.express as px

fig = px.line(df, x=df.index, y='Goals', color='Player Names',title='Number of Goals Scored Throughout the Years')
fig.update_layout(
    autosize=False,
    width=800,
    height=800,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
fig.show()


# In[18]:


fig = px.line(df, x=df.index, y='Shots Per Avg Match', color='Player Names',title='Average Shots Taken per Player')
fig.update_layout(
    autosize=False,
    width=800,
    height=800,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
fig.show()


# In[21]:


df['Avg Goals Per Match'] = df['Goals'] / df['Matches_Played']


# In[22]:


df


# In[23]:


fig = px.line(df, x=df.index, y='Avg Goals Per Match', color='Player Names',title='Average Goals Scored per Match')
fig.update_layout(
    autosize=False,
    width=800,
    height=800,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
fig.show()


# In[24]:


df['Missed Goals'] = df['Shots'] - df['OnTarget']


# In[25]:


df


# In[26]:


fig = px.line(df, x=df.index, y='Missed Goals', color='Player Names',title='Number of Missed Goals per Player')
fig.update_layout(
    autosize=False,
    width=800,
    height=800,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
fig.show()


# In[27]:


df['Goals Per Minute'] = df['Goals'] / df['Mins']


# In[28]:


df


# In[29]:


fig = px.line(df, x=df.index, y='Goals Per Minute', color='Player Names',title='Number of Goals Scored per Minute')
fig.update_layout(
    autosize=False,
    width=800,
    height=800,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
fig.show()


# In[30]:


fig = px.bar(df, x='Player Names', y='Goals', title='Number of Goals Scored per Player')
fig.update_layout(
    autosize=False,
    width=800,
    height=800,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
fig.show()


# In[31]:


fig = px.bar(df, x='Player Names', y='Goals Per Minute', title='Number of Goals Scored per Minute')
fig.update_layout(
    autosize=False,
    width=800,
    height=800,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
fig.show()


# In[32]:


fig = px.bar(df, x='Player Names', y='Missed Goals', title='Number of Missed Goals Shot by Players')
fig.update_layout(
    autosize=False,
    width=800,
    height=800,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
fig.show()


# In[33]:


fig = px.bar(df, x='Player Names', y='Avg Goals Per Match', title='Avg Goals Scored per Match')
fig.update_layout(
    autosize=False,
    width=800,
    height=800,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
fig.show()


# In[36]:


fig = px.bar(df, x='Player Names', y='Shots Per Avg Match', title='Avg Shots Taken per Match')
fig.update_layout(
    autosize=False,
    width=800,
    height=800,
    margin=dict(l=50, r=50, b=100, t=100, pad=4)
)
fig.show()


# In[37]:


fig = px.scatter(df, x='Mins', y='Goals', title='Scatter Plot of Minutes Played vs Goals',trendline='ols')
fig.show()


# In[38]:


fig = px.scatter(df, x='Matches_Played', y='Goals', title='Scatter Plot of Minutes Played vs Goals',trendline='ols')
fig.show()


# In[39]:


fig = px.scatter(df, x='Shots', y='Goals', title='Scatter Plot of Shots vs Goals',trendline='ols')
fig.show()


# In[45]:


import tkinter as tk
import pandas as pd


df


# In[56]:


import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt


# Create the main window
window = tk.Tk()
window.title('Player Comparison')
window.geometry('400x300')

# Create a label for player selection
label = tk.Label(window, text='Select Players:')
label.pack()

# Create a listbox for player selection
listbox = tk.Listbox(window, selectmode=tk.MULTIPLE)
listbox.pack()

# Populate the listbox with player names from the dataset
players = df['Player Names'].unique()  # Update column name here
for player in players:
    listbox.insert(tk.END, player)

# Create a button to trigger the player comparison
button = tk.Button(window, text='Compare', command=lambda: compare_players(listbox.curselection()))
button.pack()

# Create a function to compare selected players
def compare_players(selected_indices):
    if len(selected_indices) == 2:
        player1_name = listbox.get(selected_indices[0])
        player2_name = listbox.get(selected_indices[1])
        
        player1 = df[df['Player Names'] == player1_name]  # Update column name here
        player2 = df[df['Player Names'] == player2_name]  # Update column name here
        
        # Get the required parameters for comparison
        player1_goals = player1['Goals'].values[0]
        player2_goals = player2['Goals'].values[0]
        player1_shots = player1['Shots'].values[0]
        player2_shots = player2['Shots'].values[0]

        
        # Perform the comparison and display the results
        result_label = tk.Label(window, text=f'Comparison between {player1_name} and {player2_name}:')
        result_label.pack()
        
        goals_label = tk.Label(window, text=f'Goals: {player1_name}: {player1_goals}, {player2_name}: {player2_goals}')
        goals_label.pack()
        
        shots_label = tk.Label(window, text=f'Shots Taken: {player1_name}: {player1_shots}, {player2_name}: {player2_shots}')
        shots_label.pack()
        
        players = [player1_name, player2_name]
        goals = [player1_goals, player2_goals]
        
    plt.bar(players, goals)
    plt.xlabel('Player')
    plt.ylabel('Goals')
    plt.title('Comparison of Goals')


    plt.bar(players, goals)
    plt.xlabel('Player')
    plt.ylabel('Goals')
    plt.title('Comparison of Goals')

    # Display the graph
    plt.show()



# Start the Tkinter event loop
window.mainloop()


# In[ ]:





# In[ ]:




