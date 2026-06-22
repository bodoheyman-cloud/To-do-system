list = []
while True:
    mie = input("enter tasks #note when u finish type exit#: ")
    if mie == "exit":
     break
    list.append(mie)
    list.sort()
print (list)
while True:
    dele = input("did you finished anything?: ")
    list.remove(dele)
    print (list)
    if not list:
        print("congrats! you did well tdy")
        break