#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime


# In[ ]:


#Question1


# In[3]:


def is_date_format_correct(date:str)->bool:
    if len(date) == 10:
        
        if date[4] == '-' and date[7] == '-' :
            if int(date[5:7]) <= 12 and int(date[8:10]) <=31:
                return True
            else:
                return False
        
    else:
        return False


# In[ ]:


#Question2


# In[4]:


for i in range(1, 11):
    if i==6:
        continue
    else:
        print(i, end=',')


# In[ ]:


#Question3


# In[7]:




def getPrevdate(date):
    dict = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
    
    if int(date[8:10]) == 1:
        if int(date[5:7]) == 1:
            '''date[5:7] - month
               date[:4]  -year
               date[8:10] -day
            '''

            #make month = 12 ,get the value of a key
            #decrease year by 1
            
            d = 31
            y = int(date[:4])-1
            m = dict[12]
            
            final = str(d)+" "+str(m)+" "+ date[:4]
            return final
             
        elif int(date[5:7]) > 1:
            tt = int(date[5:7])-1    #month
            #make it equal 30 or 29 or 31 check condition
            
            k = int(date[5:7])
            if (k<=7 and k!=3  and  k%2 !=0) or (k>7 and k%2 ==0 ):
                d = 30
            elif (k<=7 and k%2==0) or (k>7 and k%2!=0):
                d = 31
            elif k == 3 and int(date[:4])%4 != 0 :
                d = 28
            elif k == 3 and int(date[:4])%4 == 0 :     #leap year take into account
                d = 29
            
            final = str(d)+" "+dict[tt]+" "+ date[:4]
            return final
        
    elif int(date[8:10]) > 1:
        d = int(date[8:10])-1
        m = dict[int(date[5:7])]
        final = str(d)+" "+str(m)+" "+ date[:4]
        return final
        

def compute_prev_date(dates_list:list):
    a = []
    for i in dates_list:
        a.append(getPrevdate(i))
    
    return a
compute_prev_date(['2012-03-01', '2022-12-30', '2099-12-21'])


# In[ ]:


#Question 4


# In[21]:


def main():
    qty = None
    cost = None

def fetch_quantity():
    """
    Returns a number, any number
    """
    ...
    return ...

def fetch_cost():
    """
    Returns a number, any number
    """
    ...
    return ...

def compute_cost_per_quantity():

    qty = fetch_quantity()
    cost = fetch_cost()
    cost_per_quantity = cost/qty
    
    try:
        fetch_cost()
    except:
        pass
        
    #second try except
    try:
        fetch_quantity()
        cost_per_quantity = cost/qty
            
            
    except Exception as e:
        print(e)
        sys.exit(1)
    
    
    return cost_per_quantity
cost_per_quantity = compute_cost_per_quantity()
a = 1 + 2 + cost_per_quantity
b = 4 + 5
print(a+b)


# In[8]:


#Question 6


# In[12]:


class TestMath:
    
    def __init__(self):
        self.x = 10
        self.y = 10

    def test_add(self):
    
        return self.x + self.y
    
    def test_subtract(self):
        
        return self.x - self.y
    
    def test_milutiply(self):
        
        return self.x * self.y
    
obj = TestMath()
obj.test_add()
obj.test_subtract()
obj.test_milutiply()

