import random

def high_low_game(rounds):
    score = 0
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    for round_number in range(1, rounds + 1):
        print(f"Round {round_number}")
        
        your_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"Your number is {your_number}")
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
        
        if (guess == "higher" and your_number > computer_number) or \
           (guess == "lower" and your_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}\n")
    
    print("Thanks for playing!")
rounds = 5
high_low_game(rounds)

# game2
import random

def high_low_game(rounds):
    score = 0
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    for round_number in range(1, rounds + 1):
        print(f"Round {round_number}")
        
        computer_number = random.randint(1, 100)
        your_number = random.randint(1, 100)
        
        print(f"The computer's number is {computer_number}")
        print(f"Your number is {your_number}")
        
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
        
        if (guess == "higher" and your_number > computer_number) or \
           (guess == "lower" and your_number < computer_number):
            print("You were right!")
            score += 1
        else:
            print("Aww, that's incorrect.")
        
        print(f"Your score is now {score}\n")
    
    print("Thanks for playing!")

# Set the number of rounds
rounds = 5
high_low_game(rounds)
