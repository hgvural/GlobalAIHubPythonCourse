#!/usr/bin/env python
# coding: utf-8

# In[2]:


cv1 = {"Name":"Hüseyin", "Surname":"Yalçın", "City of Birth":"Balıkesir", "Degree":"Mathematical Engineering", 
           "University":"İTÜ", "Total Exp. in Years":"14"}
cv2 = {"Name":"Fatih", "Surname":"Çalık", "City of Birth":"Muğla", "Degree":"Computer Engineering", 
           "University":"ODTÜ", "Total Exp. in Years":"9"}
cv3 = {"Name":"Refik", "Surname":"Sağlam", "City of Birth":"İstanbul", "Degree":"Industrial Engineering", 
           "University":"Uludağ", "Total Exp. in Years":"12"}
cv4 = {"Name":"Mert", "Surname":"Yücel", "City of Birth":"İzmir", "Degree":"Industrial Engineering", 
           "University":"Atatürk", "Total Exp. in Years":"5"}
cv5 = {"Name":"Tarık", "Surname":"Yılmaz", "City of Birth":"Ankara", "Degree":"Software Engineering", 
           "University":"9 Eylül", "Total Exp. in Years":"8"}
cvs = [cv1, cv2, cv3, cv4, cv5]
import pandas as pd
for i in cvs:
    seri1 = pd.Series(i.values(), index = i.keys())
    print(seri1)
    print()

