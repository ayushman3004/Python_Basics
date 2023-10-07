d = {1:"100","two":"hundred", 3:"Ram","sham":4}
print(d["two"]) #accessing dictionary items

l1 , l2 = [], []
n = int(input("items: "))
for i in range(n):
    key = input("give me the {} key".format(i))
    val = input("give me the {} value associated".format(i))
    l1.append(key)
    l2.append(val)
d = dict(key = val)
print(d,type(d, type(d)))


