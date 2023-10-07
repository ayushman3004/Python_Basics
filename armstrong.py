n = int(input("n: "))
x = n
num = len(str(n))
var = 0
sum = 0
while n>0:
    var = n%10
    sum += var**num
    n = n -var
    n = n//10
    print("sum of numbers : ", sum)
    # if x==n :
    #     print("Armstrong Number")
    # else :
    #     print("Not Armstrong")
