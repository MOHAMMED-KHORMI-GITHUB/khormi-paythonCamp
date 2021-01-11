#!/usr/bin/env python
# coding: utf-8

# In[1]:



firstname=input("Enter your name")
print("welcome",firstname)
num1=float(input("Enter first number : "))
num2=float(input("Enter second number : "))
print(num1+num2)


# In[1]:


import turtle
from turtle import forward, right, left
turtle.shape('turtle')
for i in range(4):
    turtle.forward(50)
    turtle.right(90)


# In[1]:


from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


# In[8]:


import turtle
from turtle import *
squary = turtle.Turtle()
squary.speed(10)
for i in range(500):
    squary.forward(i)
    squary.left(91)
turtle.done()


# In[6]:


import turtle

tim = turtle.Turtle()

def drawSquare(length):
    for i in range(4):
         tim.forward(length)
         tim.right(90)
for i in range(90):
    drawSquare(100)
    tim.right(4)

for i in range(45):
    drawSquare(200)
    tim.right(8)
    turtle.done()


# In[10]:


import turtle
turtle.shape('turtle')
x =0
for x in range (60):
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.right(5)


# In[15]:


def name(n): 
	if n != 0: 
		name(n-1) 
		print("python") 
name(100) 


# In[ ]:


import random
import math
 # Taking Inputs
lower = int(input("Emter Lower bound:- ")) 
 
# Taking Inputs
upper = int(input("Enter Upper bound:- "))  
 
# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2))," chances to guess the integer!\n")
 
 # Initializing the number of guesses.
count = 0
 
# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
     
     # taking guessing number as input
    guess = int(input("Guess a number:- ")) 
     
    # Condition testing
    if x == guess:  
       print("Congratulations you did it in ", count, " try")
       # Once guessed, loop will break 
       break
    elif x > guess:
       print("You guessed too small!")
    elif x < guess:
       print("You Guessed too high!")
 
# If Guessing is more than required guesses, 
# shows this output.
if count >= math.log(upper - lower + 1, 2):
   print("\nThe number is %d"%x)
   print("\tBetter Luck Next time!")
 
# Better to use This source Code on pycharm!


# In[30]:


import turtle

turtle.shape("turtle")
turtle.speed(100)
scale = 0
while range(60):
    scale += 2
    for x in range(4):
        turtle.forward(25+scale)
        turtle.right(90)
    turtle.right(5)
     


# In[ ]:


import turtle
turtle.shape("turtle")
turtle.speed(100)
scale = 0
for i in range(60):
    scale += 5
    for x in range(4):
        turtle.forward(25+scale)
        turtle.right(90)
    turtle.right(5)

