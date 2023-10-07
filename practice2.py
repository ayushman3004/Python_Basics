vowels = "aeiouAEIOU"
while True:
    c= input("vowel, or -1 to quit: ")
    if c != -1 :
        if c.isalpha() in vowels:
            print("vowel")
        elif c.isalpha() not in vowels:
            print("not vowel") 
        else:
            print("wrong input")
    if c== -1 :
        break