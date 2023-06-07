#!/usr/bin/env python
# coding: utf-8

# ## Extracting movie information from the Rotten Tomatoes HTML files using Beautiful Soup.
# Gathering website: Rotten Tomatoes
# - Using _Beautiful Soup_ to extract the desired Audience Score metric and number of audience ratings, along with the movie title so we have something to merge the datasets on later. For each HTML file, then saving them in a pandas DataFrame.
# - The task is to extract the title, audience score, and the number of audience ratings in each HTML file so each trio can be appended as a dictionary to df_list.

# In[3]:


#Firstly, import the necessary libraries and parse the HTML file using Beautiful Soup.
from bs4 import BeautifulSoup
import os
import pandas as pd


# In[4]:


# List of dictionaries to build file by file and later convert to a DataFrame
df_list = []
folder = 'rt_html'
for movie_html in os.listdir(folder):
    with open(os.path.join(folder, movie_html)) as file:
        soup = BeautifulSoup(file, 'lxml')
        title = soup.find('title').contents[0][:-len(' - Rotten Tomatoes')]
        audience_score = soup.find('div', class_='audience-score meter').find('span').contents[0][:-1]
        num_audience_ratings = soup.find('div', class_='audience-info hidden-xs superPageFontColor').find_all('div')[1].contents[2].strip().replace(',', '')
        
        # Appending to list of dictionaries
        df_list.append({'title': title,
                        'audience_score': int(audience_score),
                        'number_of_audience_ratings': int(num_audience_ratings)})
df = pd.DataFrame(df_list, columns = ['title', 'audience_score', 'number_of_audience_ratings'])


# In[8]:


df.head()


# ## Solution Test
# Runing the cell below to the see if my solution is correct. If an `AssertionError` is thrown, my solution is incorrect. If no error is thrown, my solution is correct.

# In[5]:


df_solution = pd.read_pickle('df_solution.pkl')
df.sort_values('title', inplace = True)
df.reset_index(inplace = True, drop = True)
df_solution.sort_values('title', inplace = True)
df_solution.reset_index(inplace = True, drop = True)
pd.testing.assert_frame_equal(df, df_solution)


# In[6]:


#correct solution!


# In[ ]:




