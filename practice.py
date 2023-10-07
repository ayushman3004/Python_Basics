print("Enter -1 to exit")
positive = 0
negative = 0 
zero = 0

while True :
    i = int(input("Enter a number: "))
    if i==-1:
        break
    if i != -1:
        if i>0 : 
            positive +=1
        elif i==0:
            zero += 1
        elif i<0 : 
            negative += 1
print("Positive",positive)    
print("Negative",negative)    
print("Zero",zero)    


