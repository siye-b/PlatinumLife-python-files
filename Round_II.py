#!/usr/bin/env python
# coding: utf-8

# In[142]:


import pandas as pd
import numpy as np 
from pandas.io.json import json_normalize



# In[143]:


#Question1


# In[144]:



df_teacher = pd.DataFrame({
    
'name': ["Pep Guardiola", "Jurgen Klopp", "Mikel Arteta", "Zinadine Zidane"],
'married': [True, True, False, True],
'school': ["Manchester High School", "Liverpool High School", "Arsenal High", np.nan]

})
 
df_student = pd.DataFrame({
    
"teacher": ["Mikel Arteta", "Mikel Arteta", "Pep Guardiola", "Jurgen Klopp", "Jurgen Klopp", "Jurgen Klopp", "Pep Guardiola","Pep Guardiola","Mikel Arteta"],
"name": ["Bukayo Saka", "Gabriel Martinelli", "Jack Grealish", "Roberto Firmino",
"Andrew Robertson", "Darwin Nunez", "Ederson Moraes", "Manuel Akanji", "Thomas Partey"],
"age": [21, 21, 27, 31, 28, 23, 29, 27, 29],
"height": ['2.1m','2.1m', '2.1m', '2.1m', '2.1m','2.1m', '2.1m', '2.1m', '2.1m']

})

df_teacher


# In[145]:


df2 = df_teacher.to_json(orient = 'columns')
df2


df = df_student.copy()
df = df.rename(columns={'name': 'student'}) 
df
dfn = pd.concat([df_teacher, df], axis=1, join='outer')
dfn


# In[146]:



strj ='[{"name":"Pep Guardiola","married":"True", "school":"Manchester High School","teacher":"Mikel Arteta","student":"Bukayo Saka","age":21,"height":"2.1m"},{"name":"Jurgen Klopp","married":"True", "school":"Liverpool High School","teacher":"Mikel Arteta","student":"Gabriel Martinelli","age":21,"height":"2.1m"},{"name":"Mikel Arteta","married":"False", "school":"Arsenal High","teacher":"Pep Guardiola","student":"Jack Grealish","age":27,"height":"2.1m"},{"name":"Zinadine Zidane","married":"True", "school":"NaN","teacher":"Jurgen Klopp","student":"Roberto Firmino","age":31,"height":"2.1m"},{"name":"NaN","married":"NaN", "school":"NaN","teacher":"Jurgen Klopp","student":"Andrew Robertson","age":28,"height":"2.1m"},{"name":"NaN","married":"NaN", "school":"NaN","teacher":"Jurgen Klopp","student":"Darwin Nunez","age":23,"height":"2.1m"},{"name":"NaN","married":"NaN", "school":"NaN","teacher":"Pep Guardiola","student":"Ederson Moraes","age":29,"height":"2.1m"},{"name":"NaN","married":"NaN", "school":"NaN","teacher":"Pep Guardiola","student":"Manuel Akanji","age":27,"height":"2.1m"},{"name":"NaN","married":"NaN", "school":"NaN","teacher":"Mikel Arteta","student":"Thomas Partey","age":29,"height":"2.1m"}]'

data= json.loads(strj)

df = json_normalize(data, None, None)
strj


# In[147]:



    
j = (df.groupby(['teacher','married','school'])
.apply(lambda x: x[['student','age','height']].to_dict('records'))
.reset_index()
.rename(columns={0:'Students'})
.to_json(orient = 'records'))
print(json.dumps(json.loads(j), indent=2, sort_keys=False))

