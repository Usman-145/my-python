#question 1
first_number_input = input("Enter the first number: ")
first_number = int(50)
second_number_input = input("Enter the second number: ")
second_number = int(10)
total_sum = first_number + second_number

print("The sum of", first_number, "and", second_number, "is", total_sum)

# question2
favorite_animal = input("What's your favorite animal? ")
print(f"My favorite animal is also {favorite_animal}!")

# question3
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5.0 / 9.0
print(f"Temperature: {fahrenheit}F = {celsius}C")

# qusrion4
side1 = float(input("What is the length of side 1? "))
side2 = float(input("What is the length of side 2? "))
side3 = float(input("What is the length of side 3? "))
perimeter = side1 + side2 + side3

print(f"The perimeter of the triangle is {perimeter}")

# question5
number = float(input("Type a number to see its square: "))
square = number * number

print(f"{number} squared is {square}")

# question6
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)

print(numbers)

# question7
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)

print(list1)

# question8
items = [10, 20, 30, 40]
removed_value = items.pop()

print("Updated list:", items)
print("Removed value:", removed_value)

# question9
colors = ['red', 'blue', 'green', 'yellow']
index_of_green = colors.index('green')

print("The index of 'green' is:", index_of_green)

# question10
def get_last_element(lst):

    print(lst[-1])

# question11
def get_user_list():
    user_list = []

    while True:
        value = input("Enter a value: ")
        if value == "":
            break
        user_list.append(value)

    print("Here's the list:", user_list)
get_user_list()
