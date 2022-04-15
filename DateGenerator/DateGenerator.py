import random
"""
Author: Kim Villatoro
Written: March 14, 2020
Program: DateGenerator.py
File: dates.txt
This program randomly chooses a date to go on.
"""


#Open the file and read the contents
list = open("dates.txt", "r")

#Check to see if program can read file
'''if list.mode == 'r':

    contents = list.read()
    print(contents) '''

#realines() reads the individual lines
f1 = list.readlines()
f1 = random.choice(f1)

'''
for x in f1:
    print(x) '''


print("Drum roll please... \n Your random date is...", f1.upper())








