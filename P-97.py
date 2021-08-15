import random;
name="NUMBER GUESSING GAME"
print(name)

number=int(random.randint(1,30))
lives=5
numberguess=int(input("Guess any number between 1 to 30"))

while lives > 0:
    if numberguess == number :
        print("Congrats! Your Guess is correct.")
        break
    elif numberguess< number :
        print("Oops! Your guess was wrong. The number is greater.")
        numberguess=int(input(" Guess a number between 1 to 30"))
        lives=lives-1  
    elif numberguess>number:
        print("Oops! Your guess was wrong. The number is smaller")  
        numberguess= int (input("Guess a number between 1 to 30"))
        lives=lives-1

if lives == 0:
    print("You didn't get it this time. Do try again!")  
    print("The number was", number)      