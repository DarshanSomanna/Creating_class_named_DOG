#!/usr/bin/env python
# coding: utf-8

# In[13]:


class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    
    def description(self):
        print("Name is ",self.name)
        print("Age is ",self.age)
    
    def get_info(self):
        print("Name is ",self.name)
        print("Coat Colour is ",self.coat_color)

class JackRussellTerrier(Dog):
    def racer(self):
        print(f"{self.name} loves sprots.")
    
    def hunter(self):
        print(f"{self.name} huntes and runs faster.")

class Bulldog(Dog):
    def foodie(self):
        print(f"{self.name} loves to eat all kind of food items")
    
    def gym_boy(self):
        print(f"{self.name} - gym dog,weights upto 120kgs.")


# In[8]:


my_dog = Dog("TOMMY", 1, "WHITE")


# In[11]:


jr_terrier = JackRussellTerrier("Jack", 2, "Black and White")


# In[12]:


bulldog = Bulldog("Bull", 3, "Black")


# In[20]:


my_dog.description()
my_dog.description()
my_dog.get_info()


# In[18]:


jr_terrier.description()
jr_terrier.racer()
jr_terrier.hunter()


# In[17]:


bulldog.description()
bulldog.foodie()
bulldog.gym_boy()


# In[ ]:




