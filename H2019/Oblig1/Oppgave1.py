def nummer(a,b,c):
    print("Tall nr 1: " + str(a))
    print("Tall nr 2: " + str(b))
    print("Tall nr 3: " + str(c))
    if a < b < c:
        print("Disse tallene er stigende.")
    elif a > b > c:
        print("Disse tallene er synkende")
    else:
        print("Disse tallene er verken stigende eller synkende")

nummer(1,2,3)