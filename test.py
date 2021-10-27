tall = int(input("Give me a number: "))
print(tall)
x = []
y = []
counter = 1

x.append(tall)
y.append(counter)

while tall != 1:
    if(tall %2 == 0):
        tall = tall // 2
        counter+=1
        y.append(counter)
        print(tall)
    elif(tall %2 != 0):
        tall = tall * 3 + 1
        counter+=1
        y.append(counter)
        print(tall)
    x.append(tall)

print(x)
print(y)