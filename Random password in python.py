#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
password="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$)%^&*(-=+}\{|abcdefghijklmnopqrstuvwxyz"
length=int(input("Enter the length of the password "))
a=''.join(random.sample(password,length))
print("Your password is {}".format(a))


# In[ ]:




