import random

while True:
    options = ('rock', 'paper', 'scissor')
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter your choice (rock/paper/scissor):")
        if player not in options:
            print("please choose valid option")


    print(f"You: {player}")
    print(f"Computer: {computer}")


    if player == computer:
        print("It's a draw.")
    elif player == 'rock' and computer =='paper':
        print("You Lose!")
    elif player == 'paper' and computer =='scissor':
        print("You Lose!")
    elif player == 'scissor' and computer =='rock':
        print("You Lose!")
    else:
        print("You Win")