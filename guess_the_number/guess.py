import random

#r = random.randrange(-5,10) # excluding 10
#r = random.randint(-5, 11) # upto 11
GUESSES = 0

top_range = input("Enter the number range: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Please type a number greater than 0")
        quit()
else:
    print("Please enter a number")
    quit()

random_number = random.randint(0, top_range)

while True:
    GUESSES += 1
    user_guess = input("Make a guess:")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please enter a number. String not supported")
        continue

    if user_guess == random_number:
        print("Woah... You guessed it right.")
        break
    elif(user_guess > random_number):
        print("You were above the number.")
    else:
        print("You were below the number.")

print("You got it in", GUESSES, "try")



