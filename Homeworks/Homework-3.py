#!/usr/bin/env python
# coding: utf-8

# In[ ]:


gradelist = list()
for i in range(5):  #taking user inputs
    record = {}
    record["name"] = input("Name of Student:")
    record["midterm"] = float(input("Midterm Exam Grade:"))
    record["project"] = float(input("Project Grade:"))
    record["final"]= float(input("Final Exam Grade:"))
    gradelist.append(record)
for i in gradelist:  #calculating passing grade
    passGrade = i["midterm"] * 0.3 + i["project"] * 0.3 + i["final"] * 0.4
    i["passGrade"] = passGrade

gradelist = sorted(gradelist, key = lambda i: i["passGrade"], reverse = True)

print(gradelist)

