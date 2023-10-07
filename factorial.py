s = int(input("Enter the number: "))
f = 1
for i in range(1,s+1):
    f = f*i
    i = i-1
print("factorial :",f)