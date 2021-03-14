#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


HT = np.zeros(10)


# In[8]:


def insert_record():
    for i in range(len(HT)):
        key = int(input("Enter the key"))
        ind = key % len(HT)
        if(HT[ind] == 0):
            HT[ind] = key
        else:
            occupied_key = HT[ind]
            home_add_occupied_key = int(occupied_key) % 10
            if(home_add_occupied_key != ind):
                HT[ind] = key
                key = occupied_key
                for j in range(len(HT)):
                    ind = (int(key)+j) % len(HT)
                    if(HT[ind] == 0):
                        HT[ind] = key
                        break
            else:
                for j in range(len(HT)):
                    ind = (key+j) % len(HT)
                    if(HT[ind] == 0):
                        HT[ind] = key
                        break
                


# In[ ]:


def search_record():
    key = int(input("Enter the key to be search "))
    ind = key % len(HT)
    if(HT[ind] == key):
        print("Key found")
    else:
         for j in range(len(HT)):
            ind1 = (key+(j*j)) % len(HT)
            if(HT[ind1] == key):
                print("Key found")
                break
         if(j == 9):
            print("Key not found")


# In[6]:


def display():
    print("Hash Table", HT)


# In[ ]:


choice = 0
while(choice != 4):
    print("******** INSERT ********")
    print("******* SEARCH ********")
    print("******** DISPLAY ********")
    print("******** EXIT ********")
    choice = int(input("Enter the choice "))
    if(choice > 4):
        print("Choice Invalid")
    if(choice == 1):
        insert_record()
    elif(choice == 2):
        search_record()
    elif(choice == 3):
        display()


# In[ ]:





# In[ ]:




