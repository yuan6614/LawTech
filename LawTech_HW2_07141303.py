#!/usr/bin/env python
# coding: utf-8

# In[37]:


for i in range(1,10):
    if i >=2:
        for x in range(10):
            if x>=1:
                
                print('{}x{}={}\t.format(i,x,i*x)'end='')
        print()


# In[38]:


list(range(1,10))


# In[46]:


for i in range(2,10):
    for j in range(1,10):
        print(str(i) + 'x' + str(j) + '=' + str(i*j), end=' ')
    print() 


# In[ ]:




