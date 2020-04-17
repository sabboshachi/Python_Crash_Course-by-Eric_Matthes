#!/usr/bin/env python
# coding: utf-8

# In[1]:


# What is a list 

names = ["rudra", "sandy","sabboshachi"]

print(names)


# In[4]:


#Accessing elements in a list 

names = ["rudra", "sandy","sabboshachi"]

print(names[0].title())


# In[5]:


names = ["rudra", "sandy","sabboshachi"]

message = "Happy Bithday !"

print(message + names[1].title() + "!!")


# In[8]:


#Exercise_3-1

names = ["rudra", "sandy","sabboshachi"]

print(names[0].title())

print("\n" + names[1].title())

print("\n" + names[2].title())


# In[9]:


#Exercise-3.2 (Using for loop)
names = ["rudra", "sandy","sabboshachi"]

for name in names:
    print("Hello," + name.title() + "!")


# In[11]:


#Exercise-3-3(using for loop)


bikes = ["honda" , "suzuki" , "yamaha"]

for bike in bikes:
    print ("\nI would like to buy a " + bike.title() + ".")


# In[16]:


#Modifying elements in a list

bikes = ["honda" , "suzuki" , "yamaha"]
print(bikes)

bikes[0] = "royal enfield"
print(bikes)


# In[17]:


#Appending elements in the end of a list

bikes = ["honda" , "suzuki" , "yamaha"]
print(bikes)

bikes.append("royal enfield")
print(bikes)


# In[19]:


#Removing item using dell(permanently)

bikes = ["honda" , "suzuki" , "yamaha"]
print(bikes)

del bikes[0]
print(bikes)


# In[20]:


#Removing item using pop()(not premanently)
#pop() can be called  as last come frist out

bikes = ["honda" , "suzuki" , "yamaha"]
print(bikes)

popped_bikes = bikes.pop()
print(bikes)
print(popped_bikes)


# In[23]:


#Popping item from any position in a list 

bikes = ["honda" , "suzuki" , "yamaha"]
print (bikes)

popped_bike = bikes.pop(1)
print(bikes)

print(popped_bike.title())


# In[24]:


#Removing an item by "value"

bikes = ["honda" , "suzuki" , "yamaha"]

print(bikes)

bikes.remove("honda")
print(bikes)


# In[27]:


bikes = ["honda" , "suzuki" , "yamaha"]
print (bikes)

print("In the list I don't like " + bikes[0].title() + ".")

bikes.remove("honda")
print (bikes)

bikes.append("royal enfield")
print(bikes)


# In[29]:


#Exercise_3-4

names = ["rudra", "sandy","sabboshachi"]

for name in names: 
    print("Hey, " + name.title() + " I would like to invite you for a dinner tonight")
    
    


# In[35]:


#Exercise_3-5

names = ["rudra", "sandy","sabboshachi"]
print(names)

new_list = names.pop(0)
print(new_list.title())

print(new_list.title() +" won't be able to come.")
print(names)

names.append("susmita")
print(names)


# In[40]:


#Exercise_3-6

names = ["rudra", "sandy","sabboshachi"]
print(names)

names.insert(0,"susmita") #using insert function
print(names)

names.insert(2,"tip") #using insert function
print(names)

names.append("susmita") #using append function
print(names)

for name in names:
    print("Happy New Year ! " + name.title())


# In[46]:


#Exercise_3-7 (Modifyed)

names = ["rudra", "sandy","sabboshachi"]
print(names)

print("But we have capacity for only two peoples")

first_session = names.pop(2)

first_sessions = []

first_sessions.append(first_session)
print(first_sessions)

for name in first_sessions:
    print("Sorry! " + name.title() + ". You are selected for our 2nd session.")
    
for name in names:
    print("Wellcome, Mr." + name.title() + "!")
    


# In[47]:


#Sorting a list

names = ["rudra", "sandy","sabboshachi"]
print(names)

names.sort()
print(names)


# In[49]:


#Sorting list Temporarily with sorted() function

names = ["rudra", "sandy", "sabboshachi"]
print(names)

print(sorted(names))

print (names)


# In[51]:


#Printing a list in reverse order

names = ["rudra", "sandy","sabboshachi"]
print(names)

names.reverse()
print(names)


# In[53]:


#Printing a list in reverse sorted order

names = ["rudra", "sandy","sabboshachi"]
print(names)

names.sort(reverse = True)
print(names)


# In[54]:


#Length of list

names = ["rudra", "sandy","sabboshachi"]
print(names)

len(names)


# In[71]:


#Exercise_3-8

places = ["everest", "amazon", "island", "hill", "sea"]
print(places)

print(sorted(places))
print(places)

new = sorted(places)
new.reverse()
print(new)
print(places)

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)


places.reverse()
print(places)


# In[72]:


#Exercise_3-9

places = ["everest", "amazon", "island", "hill", "sea"]
print(places)

len(places)


# In[ ]:




