#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Looping through an entire list

names = ["Sandy", "Rudra", "sabboshachi"]
for name in names:
    print(name.title())
    


# In[3]:


names = ["Sandy", "Rudra", "sabboshachi"]
for name in names:
    print("Hey! " + name.title() + ", Good Afternoon.")
    


# In[6]:


names = ["Sandy", "Rudra", "sabboshachi"]
for name in names:
    print("Hey! " + name.title() + ", Good Afternoon.")
print("\nYou all are invited for dinner tonight.")


# In[11]:


#Exercise_4.1

pizzas = ["veg", "chicken", "mutton"]
for pizza in pizzas:
    print("I love " + pizza.title() + "-Pizza!")

print("\nSusmita, loved pizza a lot !")    


# In[16]:


#Exercise_4.2

animals = ["cow", "dog", "cat"]
for animal in animals:
    print(animal.title())
print("All of these animals have four legs.")


# In[22]:


#Using range() function

for value in range(1,10):
    print(value)
    


# In[24]:


#Using range to make a list of Numbers

numbers = list(range(1604000,1604061))
print(numbers)


# In[28]:


#square making

numbers = list(range(101))
print(numbers)

squared_value = []

for number in numbers:
    square = number ** 2
    print(square)
    
    squared_value.append(square)

print(squared_value)


# In[29]:


#Simple statistics with a list of numbers

numbers = list(range(10))
print(numbers)

print(min(numbers))

print(max(numbers))

print(sum(numbers))


# In[30]:


#List Comprehensions

squares = [value ** 2 for value in range(1,11)]
print(squares)


# In[31]:


#Exercise_4-3

for value in range(1,21):
    print(value)


# In[38]:


#Exercise_4-4

numbers = list(range(1,100001))
print(numbers)

for value in numbers:
    print("I'm that much rich " + str(value))


# In[39]:


#Exercise_4-6

odd_numbers = list(range(1,20,2))

print(odd_numbers)


# In[40]:


#Exercise_4-7

numbers = list(range(3,31))
for number in numbers:
    mul = number * 3
    print(mul)


# In[42]:


#Exercise_4-8

numbers = list(range(101))
print(numbers)

cubed_value = []

for number in numbers:
    cube = number ** 3
    print(cube)
    
    cubed_value.append(cube)

print(cubed_value)


# In[46]:


#Exercise_4-9

cubes = [number ** 3 for number in range(101)]
print(cubes)


# In[56]:


#Slicing a List

names = ["sandy", "rudra", "sabboshachi", "susmita", "dey", "tip"]
print(names[0:3])

print(names[-3:])


# In[58]:


#Looping through a list

names = ["charles", "martina", "michael", "florence", "eli"]
print("Here is the first three members from my team:")
for name in names[:3]:
    print("\n \t " + name.title())


# In[61]:


#Copying List
names = ["charles", "martina", "michael", "florence", "eli"]
friends = names[:]

print(names)
print(friends)

names.append("susmita")

friends.append("sandy")

print(names)
print(friends)


# In[64]:


#Tuples(a list that cannot be changed)

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for number in dimensions:
    print(number)


# In[66]:


#Writing Over a tuple

dimensions = (200 , 50)
print("\nOriginal dimensions: ")
for dimension in dimensions:
      print(dimension)
      
dimensions = (100 , 500)
print("\nModified Dimensions:")
for dimension in dimensions:
      print(dimension)
          


# In[72]:


#Exercise_4.10

foods = ["biriyani", "cake", "icecream", "coke", "chicken", "burger","Pizza"]
print("The first three items in the list are:")
for food in foods[0:3]:
    print(food.title())
    
print("The middle items are: ")
for food in foods[3:4]:
    print(food.title())

print("The last three items are:")
for food in foods[4:7]:
    print(food.title())


# In[74]:


#Exercise_4.11

friend_pizzas = ["veg", "chicken", "mutton"]
print(friend_pizzas)

friend_pizzas.append("mushroom")
print(friend_pizzas)


# In[76]:


#Exercise_4.13

buffet_item = ["biriyani", "polao", "mutton", "chicken", "coke"]
print(buffet_item)

for food in buffet_item:
    print(food)


# In[ ]:




