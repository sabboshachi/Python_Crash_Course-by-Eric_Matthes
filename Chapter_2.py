#!/usr/bin/env python
# coding: utf-8

# In[1]:


#hello_world.py

print("Hello Python World!")


# In[2]:


#print using a variable

message = "Hello Python World!"
print(message)


# In[3]:


#Exercise_2-1

name = "sabboshachi"
print("My name is " + name.title())


# In[6]:


#Exercise_2-2

name = "sabboshachi"
print("My name is " + name.title() + "!")

name = "biriyani"
print("My favourute food is " + name.title() + "!")


# In[7]:


#title case

name = "sabboshachi"
print(name.title())


# In[8]:


#upper and lower case

name = "Sabbsoshachi"

print(name.upper())
print(name.lower())


# In[10]:


#adding two different variables

first_name = "sabboshachi"
last_name = "sarkar"

full_name = first_name +" "+ last_name

print("My name is " + first_name.title() + " " + last_name.title())

print("My name is " + full_name.title())


# In[11]:


#Addind whitespace

print("Python")

print("\t Python")


# In[13]:


print("My favourite languages are: ")
print("\n \t Python \n \t C \n \t Java")


# In[17]:


#Strippint Whitespace

favourite_languages = " Python "

print(favourite_languages)

print(favourite_languages.rstrip())

print(favourite_languages.lstrip())

print(favourite_languages.strip())


# In[19]:


#Exercise_2-3

name = "sandy"

print("Hello, " + name.title() + "! Would you like to learn sime Python today?")


# In[20]:


#Exercise_2-4

name = "sandy"

print(name.upper())
print(name.lower())
print(name.title())


# In[24]:


#Exercise_2-5/2-6

name = "Albert Einstein"
quote = '"A person who never made a mistake never trued anything new...!"'

print (name.title() + " once said, " + quote )


# In[28]:


#Integer_Numbers

2 + 3

5 - 2

4 * 3

4 / 2

#Floats_Numbers

0.1 + 0.1

2 * 0.1


# In[30]:


#declear type before printing

age = 23

print("My age is : " + str(age))


# In[32]:


#Exercise_2-8

addition = 2 + 6
print(addition)

subtraction = 3 - 2
print(subtraction)

multiplication = 2 * 6
print(multiplication)

division = 6 / 3
print(division)


# In[36]:


#Exercise_2-9

favourite_number = 23

print("My favourite number is : " + str(favourite_number) + " !")


# In[ ]:




