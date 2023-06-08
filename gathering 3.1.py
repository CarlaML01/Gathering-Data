#!/usr/bin/env python
# coding: utf-8

# ## Creating a DataFrame with the movie title, Roger Ebert review URL, and the review for each text file in the specified folder
# 
# So we have 88 Roger Ebert reviews to open and read, which you can see in the Jupyter Notebook in the ebert_reviews folder.
# 
# We'll need to loop to iterate through all of the files in this folder to open and read each, then extract the bits of text that we need as separate pieces of data:
# 
# - the first line, which is the movie title (to merge to the master dataset with)
# - the second line, which is the review URL (not necessary for the word cloud but nice to have)
# - everything from the third line onwards, which is the review text
# 
# >My task is to extract the movie title, Roger Ebert review URL, and the review in each text file and append each trio as a dictionary to df_list.

# In[1]:


import glob
import pandas as pd


# In[2]:


# List of dictionaries to build file by file and later convert to a DataFrame
df_list = []
for ebert_review in glob.glob('ebert_reviews/*.txt'):
    with open(ebert_review, encoding='utf-8') as file:
        title = file.readline()[:-1]
        
        # Extract the review_url
        review_url = file.readline()[:-1]
        
        # Extract the review_text
        review_text = file.read()
        
        # Append to list of dictionaries
        df_list.append({'title': title,
                        'review_url': review_url,
                        'review_text': review_text})

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(df_list, columns = ['title', 'review_url', 'review_text'])


# ## Solution Test
# Run the cell below the see if your solution is correct. If an `AssertionError` is thrown, your solution is incorrect. If no error is thrown, your solution is correct.

# In[3]:


df_solution = pd.read_pickle('df_solution.pkl')
df.sort_values('title', inplace = True)
df.reset_index(inplace = True, drop = True)
df_solution.sort_values('title', inplace = True)
df_solution.reset_index(inplace = True, drop = True)
pd.testing.assert_frame_equal(df, df_solution)


# In[ ]:


#correct!

