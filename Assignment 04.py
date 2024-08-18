def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    name = input("Enter your name: ")

    numbers = []
    for i in range(1, 4):
        number = int(input(f"Enter your {i} favorite number: "))
        numbers.append(number)

    print(f"\nHello, {name}! Let's explore your favorite numbers:")

    even_odd_info = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]
    for num, eo in even_odd_info:
        print(f"The number {num} is {eo}.")

    for num in numbers:
        square = num ** 2
        print(f"The number {num} and its square: ({num}, {square})")

    total_sum = sum(numbers)
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"{total_sum} is not a prime number, but it's still great!")

if __name__ == "__main__":
    main()
