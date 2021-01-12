#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
number = random.randint(1, 100)
attempts = 0  # count no of attempts to guess the number
guess = 0
while guess != number:
    guess = int(input("خمن رقم:- ")) 
    attempts += 1
    if guess == number:
       print("أحسنت نجحت بعد ", attempts, " محاولات")
       # Once guessed, loop will break 
       break
    elif guess < number:
       print("حاول بعدد اكبر!")
    elif guess > number:
       print("انزل شوي!")
 


# In[ ]:





# In[ ]:





# In[ ]:




