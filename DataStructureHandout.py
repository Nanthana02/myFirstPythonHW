#!/usr/bin/env python
# coding: utf-8

# ## DataStructureHandout

# Nanthana Howong

# ### Exercise Question 1

# In[1]:


listOne = [6,12,18]
listTwo = [4,12,20,28]
listTree = listOne + listTwo
print(listTree)


# ### Exercise Question 2

# : Given an input list removes the element at index 4 and add it to the 2nd position
# and also, at the end of the list

# In[6]:


OriginalList = [34, 54, 67, 89, 11, 43, 94]
element = OriginalList.pop(4)
print(OriginalList)

OriginalList.insert(2,element)
print(OriginalList)

OriginalList.append(element)
print(OriginalList)


# ### Exercise Question 3

# :Given a list slice it into a 3 equal chunks and reverse each list

# In[13]:


OriginalList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chuck1 = [11,45,8]
chuck1.reverse()
print(chuck1)

chuck2 = [23,14,12]
chuck2.reverse()
print(chuck2)

chuck3 = [78,45,89]
chuck3.reverse()
print(chuck3)


# In[35]:


Original = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chuck1.pop(4)
print(chuck1)


# In[31]:


x = [1,2,3]
x[::-1]


# ### Exercise Question 4

# In[ ]:




