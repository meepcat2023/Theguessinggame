import random

def guessing_game():
    while True:
        try:
            low = int(input("Enter the lowest number (integer): "))
            high = int(input("Enter the highest number (integer): "))
            if low >= high:
                print("Low must be less than high. Try again.")
                continue
        except ValueError:
            print("Both low and high must be integers. Try again.")
            continue

        number = random.randint(low, high)
        print("It's the guessing game!")
        print("You only have 3 attempts, so guess wisely!")
        attempt = 0
        win = False

        while not win and attempt < 3:
            try:
                guess = int(input(f"Enter a number between ({low} - {high}): "))
                if guess < low:
                    print("Value too low!")
                elif guess > high:
                    print("Value too high!")
                elif guess == number:
                    print("Yay you got it!")
                    win = True
                else:
                    if attempt < 2:
                        print("Try again!")
                    attempt += 1
            except ValueError:
                print("Not an integer!")

        if not win:
            print(f"You lost! The correct number was {number}.")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
guessing_game()