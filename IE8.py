
import random

number = random.randint(1,9)

guess=0
count = 0

while guess != number:

    guess = int(input("What's your guess?"))
    

    count += 1

    

    if guess < number:

        print("Too low")

    elif guess > number:

        print("Too high")

    else:

        print("You got it")

        print("And only took ",count,"tries!")
    
            

    

    


    
    


           
            
            
            



