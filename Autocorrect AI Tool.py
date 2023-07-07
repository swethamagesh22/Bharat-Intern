#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install autocorrect')


# In[2]:


from autocorrect import Speller


# In[3]:


spell = Speller(lang='en')


# In[4]:


def autocorrect_text(input_text):
    corrected_text = spell(input_text)
    return corrected_text


# In[ ]:


# Create an interactive loop
while True:
    input_text = input("Enter your text: ")
    if input_text.lower() == "exit":
        break

    corrected_text = autocorrect_text(input_text)
    print("Autocorrected Text:", corrected_text)

