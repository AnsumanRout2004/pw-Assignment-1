#!/usr/bin/env python
# coding: utf-8

# 
# Q1. Create one variable containing following type of data:
# (i) string
# (ii) list
# (iii) float
# (iv) tuple
# 
# 
# 

# In[2]:


mixed_data = {
    "string": "Hello, World!",
    "list": [1, 2, 3, 4],
    "float": 3.14,
    "tuple": (5, 6, 7)
}
print(mixed_data)


# In[ ]:


Q2. Given are some following variables containing data:
(i) var1 = ‘ ‘
(ii) var2 = ‘[ DS , ML , Python]’
(iii) var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
(iv) var4 = 1.
What will be the data type of the above given variable.


# In[7]:


var1 = ' '  
var2 = '[ DS , ML , Python]' 
var3 = ['DS', 'ML', 'Python']  
var4 = 1. 

So, the data types are:

var1: str
var2: str
var3: list
var4: float


# In[ ]:


Q3. Explain the use of the following operators using an example:
(i) /
(ii) %
(iii) //
(iv) **


# In[ ]:


i)Division /: Returns the quotient as a float.
print(10 / 3)  # Output: 3.3333
ii)Modulus %: Returns the remainder of division.
print(10 % 3)  # Output: 1
iii)Floor Division //: Returns the quotient rounded down (integer division)    
print(10 // 3)  # Output: 3

iv)Exponentiation **: Raises one number to the power of another    
print(2 ** 3)  # Output: 8


    


# In[ ]:


'''Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
element and its data type.''''


# In[9]:


data_list = [10, "Python", 3.14, True, [1, 2, 3], (4, 5, 6), {'a': 1}, None, complex(2, 3), b'byte']

for item in data_list:
    print(f"Element: {item}, Type: {type(item)}")


# In[ ]:


Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
times it can be divisible.


# In[10]:


A = 81
B = 3
count = 0

while A % B == 0:
    A = A // B
    count += 1

print(f"The number is divisible {count} times.")


# In[ ]:


Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
divisible by 3 or not.


# In[11]:


numbers = list(range(1, 26))  # Creates a list from 1 to 25

for num in numbers:
    if num % 3 == 0:
        print(f"{num} is divisible by 3")
    else:
        print(f"{num} is NOT divisible by 3")


# In[ ]:


Q7. What do you understand about mutable and immutable data types? Give examples for both showing
this property.


# In[16]:


##Mutable Data Types: Can be changed after creation.
my_list = [1, 2, 3]
my_list[0] = 10  # Modifying the list (allowed)
print(my_list)  # Output: [10, 2, 3]

##Immutable Data Types: Cannot be changed after creation.
my_tuple = (1, 2, 3)
my_tuple[0] = 10  # This will raise an error

## Examples:

## Mutable: list, dict, set
## Immutable: int, float, tuple, string


# In[ ]:




