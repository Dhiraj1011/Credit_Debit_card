#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
import streamlit as st


# In[2]:


number=[]
no=[0]*16
num=[]
add=0
dig=[]
#print(number,no,num)

st.title("Verify the Credit/Debit Card number")
st.header("You can enter your credit/debit card number and then it will tell you whether it exists or not and which card it is")

# In[3]:
print("enter the card number")
number=int(st.number_input('enter the card number',value=None, placeholder="Enter Card Number here"))


for i in range(0,len(number)):
    n=int(number[i])
    num.append(n)
    print(number[i],num[i])

    
if len(number)==16:
    print("Thank you")
else:
    print("Number of digits entered are wrong")

print(len(num),len(no))


# In[4]:



for i in range(0,len(number)):
    if i%2==0:
        no[i]=num[i]*2
    else:
        no[i]=num[i]
        

print("no=",no)
print(len(no))


# In[5]:


for i in range(0,len(no)):
    d=int(no[i]/10)
    e=no[i]%10
    print(d,e)
    if d!=0:
        dig.append(d)
    if e!=0:
        dig.append(e)
        
print(dig)


# In[6]:


for i in range(0,len(dig)):
    add=add+dig[i]
print(add)


# In[13]:


print(number)
if add%10==0:
    print("Entered credit/debit card number exists.")
    if num[0]==3:
        print("The card is  American Express, JCB")
    elif num[0]==4:
        print("The card is  Visa")
    elif num[0]==5:
        print("The card is  Mastercard")
    elif num[0]==6:
        print("The card is  Discover, RuPay")
    else:
        print("Can't dertermine")
else:
    print("Entered credit/debit card number does not exist.")
    
    


# In[ ]:




