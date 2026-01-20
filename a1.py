import random
playing = True
number = str(random.randint(10,20))
print("I will generate a number from 10 to 20, and you have to guess the number one digit at a time")
print( "The will be over when you guess correct number")
while playing:
    guess = input ("Give me your best guess:")
    if number == guess:
        print("You guessed the number correctly")
        break
    else:
        print("Your guess is not correct. Try again")