import random

number = random.randint(1,30)

print("I think about a Number between 1-30,you got 5 trys.")

for guesses in range(1,6):
    print("Guess the Number:")
    guess=int(input())

    if guess < number:
            print("Your guess is lower than my Number")
    elif guess > number:
            print("Your guess is higher than my Number")
    else:
        break
if guess == number:
    print("Yes,u got it! You got it in " + str(guesses) + " trys!")
else:
    print("The Number i was thinking of was : " +str(number)+".")
            