"""
Program bmi_calculator.py
Author: Kim Villatoro
BMI Calculator
# This program is used to determine body-mass-index of a collection of six individuals
# Include a list of six names
# Use a for loop to prompt the user for height in inches and weight in pounds of each individual
# Each prompt should include the name of that individual of which is to be input
# Call a function that accepts the height and weight as parameters and returns BMI
# Formula weight x 703/height^2
# BMI should be added to an array
# Loop through array and return whether an individual is underweight, normal, or overweight
# Count the number of individuals in each category and display the number in each category 
"""
persons = ['Starr', 'Donnie', 'Kai', 'Haleigh', 'Bradley', 'Jordan']  # Create list for six people
weight_lst = []  # Create an empty list for weights
height_lst = []  # Create an empty list for heights
bmi_lst = []  # Create an empty list for BMI

underweight = 0  # Create variable for underweight count
normal_weight = 0  # Create variable for normal weight count
overweight = 0  # Create variable for overweight count

for item in persons:  # Iterating through persons
    weight = eval(input("Enter a weight for person %s in pounds: \n" % item))  # Prompt user input for weight
    height = eval(input("Enter a height for person %s in inches: \n" % item))  # Prompt user input for height
    weight_lst.append(weight)  # Add elements to weight list
    height_lst.append(height)  # Add elements to height list


for (a, b) in zip(weight_lst, height_lst):  # Using zip function to iterate over weight_lst and height_lst
    bmi = int(a * 703 / b ** 2)  # Calculate body mass index
    bmi_lst.append(bmi)  # Add elements to bmi list


for (x, y) in zip(persons, bmi_lst):  # Using zip function to iterate over persons and bmi_lst
    print("BMI for %s" % x + " is: %d" % y)  # Display every persons BMI


for i in bmi_lst: # Iterating through bmi_lst
    if i <= 18.5:  # Condition for underweight range
        underweight = underweight + 1  # Count underweight weights
    elif 18.5 < i <= 25:  # Condition for normal weight range
        normal_weight = normal_weight + 1  # Count for normal weights
    elif i > 25:  # Condition for overweight range
        overweight = overweight + 1  # Count for overweight weights
    else:
        None # None value
print("The number of weights within the underweight range is:", underweight)  # Display underweight weights
print("The number of weights within the normal weight range is:", normal_weight)  # Display normal weights
print("The number of weights within the overweight range is:", overweight)  # Display overweight weights
