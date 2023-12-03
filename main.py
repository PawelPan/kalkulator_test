def Add():
    inp1 = int(input("first number:"))
    inp2 = int(input("second number:"))
    print("result: ", inp1 + inp2)

flag = True

while flag:
    opt = int(input("choose option\n1 addition\n"))
    if opt == 1:
        Add()
    else:
        continue
    inp = str(input("continue? [y/n]:"))
    flag = inp == 'y'



