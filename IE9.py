a=[]
b=[]
numa=int(input('Enter number of elements in a:'))
numb=int(input('Enter number of elements in b:'))

for i in range(numa):
   num=int((input("Element in a")))
   a.append(num)
for j in range(numb):
   num1=int((input("Element in b")))
   b.append(num1)
c=[x for x in a  if x in b]
print(c)

    


    
    


           
            
            
            



