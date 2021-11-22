import random

number = random.randint(1, 9)

chances = 0

print("Guess a number (between 1 and 9):")

while chances < 5:


    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulation YOU WON!!!")
        break
    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)
    else:
        print("Your guess was too high: Guess a number lower than", guess)

    chances += 1

if not chances < 5:
    print("YOU LOSE!!! The number is", number)


'''
for number in user_input:
    if(number == user_input):
        print("You Have Won")
    elif():
        print(num)
'''
