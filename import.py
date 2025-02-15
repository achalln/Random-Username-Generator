#required module
import random
from random import randint

#Opening the text file which contains names
f = open('Aaron.txt')

#Creating a list by using list comprehension 
name = [i for i in f]

#Selecting a row of name
n = random.choice(name)

#removing the next line
n = n.rstrip('\n')

#removing the space 
n = n.replace(' ', '')

#printing the username with random no.
print(n + str(randint(0, 9999)))