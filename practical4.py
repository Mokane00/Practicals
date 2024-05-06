import math
#The program takes two integers from the user and return their sum and product.

num_1 =int(input("Enter the first integer: "))
num_2 =int(input("Enter the second integer: "))
sum = num_1 + num_2
product = num_1 * num_2
print(sum)
print(product)


#A program that computes the area of a circle based on the radius from the user
radius = int(input("Enter a radius: "))
Area_of_the_circle = ( round(math.pi,2)* radius**2)
print(Area_of_the_circle)

#A program that asks the user for a positive integer less than 100. Your program must then provide the user with the product of 7 and the last digit of the entered integer.
pos_int =int(input("Enter a positive integer: "))
if pos_int < 100 and pos_int % 7 == 0:print(pos_int) 
last_digit = pos_int % 10  
print(last_digit)

#Your program must ask the user the amount to convert and return the converted amount formatted as expected in two decimal places.
Lesotho_currency = 1.34
Botswana_currency = 1
amount_Maloti =float(input("Enter an amount in Maloti: ")) * Botswana_currency
amount_pula = float(input("Enter an amount in Pula: ")) * Lesotho_currency
print(amount_Maloti)
print(amount_pula)



#A program that reads a positive integer, n, from the user and then displays the sum of all of the integers from 1 to n.
n = int(input("Enter a positive integer: "))
sum = 0
for i in range(n):
  sum += 1
  print(sum)

coursework_mark = input("Enter your coursework mark: ")
part_of_the_final_mark = coursework_mark * (40/100)


# Prompting the user for input
n = int(input("Enter an integer value for n: "))

# Computing the value nnn-nn-n and displaying it
result = n * 100 + n * 10 + n - (n * 10 + n)
print(f"The result of {n}{n}{n}-{n}{n}-{n} is {result}")



# Prompting the user for input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Calculating the years until turning 70 and displaying the message
years_until_70 = 70 - age
print(f"{name}, you will be turning 70 in {years_until_70} years.")


# Prompting the user for input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
current_year = int(input("Enter the current year: "))

# Calculating the year of turning 70 and displaying the message
year_turning_70 = current_year + (70 - age)
print(f"{name}, you will be reaching 70 i.e. 'lilemo tsa pallo' in the year {year_turning_70}")


# Prompting the user for input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
current_year = int(input("Enter the current year: "))
repeat_times = int(input("How many times do you want to print the message? "))

# Calculating the year of turning 70 and printing the message multiple times
year_turning_70 = current_year + (70 - age)
message = f"{name}, you will be reaching 70 i.e. 'lilemo tsa pallo' in the year {year_turning_70}\n"

print(message * repeat_times)