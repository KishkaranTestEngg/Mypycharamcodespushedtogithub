# Task 1: Given a list of dictionaries each representing a person with name and age keys use lambada function to filter out the people under 18 and then map the remaining people to a new list

people = [
    {"name": "Kishore", "age": 17},
    {"name": "Arun", "age": 22},
    {"name": "Rahul", "age": 15},
    {"name": "Priya", "age": 25}
]

# Filter people whose age is 18 or above
adults = list(filter(lambda person: person["age"] >= 18, people))

# Map remaining people to a new list containing only names
adult_names = list(map(lambda person: person["name"], adults))

print(adults)
print(adult_names)

# Task 2: Given a list of numbers use the reduce function and a lambada expression to calculate the product of all the numbers in the list

from functools import reduce

numbers = [2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers)

print(product)

# Task 3: create a list with square of even numbers from a given list using a lambada function to check for even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Create squares of even numbers
square_even_numbers = list(map(lambda x: x ** 2, even_numbers))

print(square_even_numbers)

# Task 4: Need to create a lambada function to check a given string is a number

check_number = lambda x: x.isdigit()

print(check_number("123"))
print(check_number("Python"))
print(check_number("45a"))

# Task 5: Need to create a lambada function to extract the year, month, and day from date time object

from datetime import datetime

date = datetime.now()

extract = lambda x: (x.year, x.month, x.day)

print(extract(date))

# Task 6: Create a lambada function to generate a fibonacci series upto n terms

fib = lambda a, b: a + b

a = 0
b = 1

print(a)
print(b)

for i in range(8):
    c = fib(a, b)
    print(" After the fibonacci series result", c)

    a = b
    b = c

