#!/usr/bin/env python
# coding: utf-8

# In[1]:


listodd  = list(range(1,20,2))
listeven = list(range(0,20,2))
listmerged = listodd + listeven
listmultiplied = [element * 2 for element in listmerged]
print(listmultiplied)
i = 0
while (i < len(listmultiplied)):
    print("The type of", listmultiplied[i], "is:", type(listmultiplied[i]))
    i = i + 1

