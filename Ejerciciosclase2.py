#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ejercicio1 Find all of the numbers from 1-1000 that are divisible by 7
numerosdivisibles7=[]
for i in range(1000):
    i=i+1
    if (i%7)==0:
        numerosdivisibles7.append(int (i))
print ("la lista es:", numerosdivisibles7)


# In[7]:


#ejercicio2 Find all of the numbers from 1-1000 that have a 3 in them
x=[str(i) for i in range (1000)]
s=[]
for j in range(1000):
    if "3" in x[j]:
        s.append(j)
print("la lista es:",s)


# In[16]:


#ejercicio3 Count the number of spaces in a string
x=input("escribe la cadena: ")
a=0
for i in range(len(x)):
    if x[i]==" ":
        a=a+1
print ("el numero de espacios son:", a)


# In[36]:


#ejercicio4 Remove all of the vowels in a string [make a list of the non-vowels]
x=input("escribe la cadena: ")
vocales="aeiou"
a=[]
for i in range (len(x)):
    for j in range (5):
        if x[i]==vocales[j]:
            a.append(x[i])
print (a)


# In[7]:


x=input("escribe la cadena: ")
a=[]
for i in range (len(x)):
    if x[i]!="a" and x[i]!="e"and x[i]!="i" and x[i]!="o" and x[i]!="u":
            a.append(x[i])
print (a)


# In[20]:


#ejercicio5 Find all of the words in a string that are less than 4 letters.
x=input("Escribe la cadena: ")
cadena= x.split()
a=[]
for i in range (len(cadena)):
    if len(cadena[i])<4:
        a.append(x[i])
print (a)


# In[19]:


txt = "hello my name is Peter I am 26 years old"

x = txt.split()
a=[]
for i in range (len(x)):
    if len(x[i])<4:
        a.append(x[i])
print(len(x),a, len(a))


# In[ ]:




