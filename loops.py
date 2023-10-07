# while loops are controlled by a true or false condition.
# The for loop is a count-controlled loop that repeats a specified number of times.


# count = 0
# while count < 100 :
#     print("programming is fun!")   #syntax of while loop
#     count = count + 1


#  continue loop = 'y'
#  while continueloop == 'y'                                    
#  execute the loop body once
#    prompt the user for condition
# continueloop = intput("Enter Y to Continue and N to quit")

c="Y"
x=1
while c=="Y":
    c = input("if ypu want to continue the loop press Y and if you want to break and come out press N : ")
    print("iteration no. : ", x)
    x=x+1