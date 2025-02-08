import random
tries = 0
choice = int(input("Wanna play a guessing game? Guess a number from 1 to 100 and see if it matches the computer! "))
while 0 < choice <= 100:
    num = random.randint(1, 100)
    if choice == num:
        print(f"You guessed right! The number was {choice}")
        choice = int(input("Wanna play a guessing game? Guess a number from 1 to 100 and see if it matches the computer!"))
    else:
        print(f"You gussed wrong! LOSER! The number was {num}")
        tries = tries + 1
        print(f"You have tried {tries} times! FAILURE!")
        choice = int(input("Try again Loser. "))
else:
    print(f"{choice} Is not a number from 1 to a 100.")
        