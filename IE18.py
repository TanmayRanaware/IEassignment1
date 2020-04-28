cows=1
bulls=1
import random
num=random.randint(1000,9999)
print(num)
c,b,guess=0,0,0 
while (c!=cows or b!=bulls):
    nument=int(input("Enter number"))
    if (num==nument):
        c+=1
        guess+=1
    elif (set(str(num))==set(str(nument))):
        b+=1
        guess+=1
    else:
         guess+=1
    print("cows=",c,"bulls=",b)
print("You took",guess,"number of trials to complete game")
            



