#Question1
def solve_riddle():
    usman_age = 21
    ali_age = usman_age + 6
    danish_age = ali_age + 20
    umar_age = danish_age + usman_age
    asad_age = danish_age

    print(f"usman is {usman_age}")
    print(f"ali is {ali_age}")
    print(f"danish is {danish_age}")
    print(f"umar is {umar_age}")
    print(f"asad is {asad_age}")
solve_riddle()

# Question2
name = "Usman"
age = 20
city = "Lahore"
sentence = f"{name} is {age} years old and lives in {city}."

print(sentence)

# Question3
a = "i aM uSmaN"
capitalized = a.capitalize()
uppercase = a.upper()
lowercase = a.lower()

print(capitalized)
print(uppercase)
print(lowercase)

# Question5
s = "I love programming in Python"
replaced_sentence = s.replace("Python","Java")
print(replaced_sentence)

#Question6
s = "mango,apple,Berry,Kiwi"
substr = s.split(',')
joine_str = ' '.join(substr)

print(substr)
print(joine_str)

#Question7
b = "   Python is fun!   "

stripped_b = b.strip()
left_side = stripped_b.ljust(20, '*')
right_side = stripped_b.rjust(20, '*')

print(stripped_b)
print(left_side)
print(right_side)

#Question8
num = 45
binary_number = bin(num)
print(f"Binary representation : {binary_number}")

#Question9
base:int = 6
exponent:int = 9
power_result= base ** exponent

print(power_result)

#Question10
value = 12.34567
rounded_to_integer = round(value)
rounded_to_two_decimal_places = round(value, 2)

print(f"Rounded to nearest integer: {rounded_to_integer}")
print(f"Rounded to two decimal places: {rounded_to_two_decimal_places}")
