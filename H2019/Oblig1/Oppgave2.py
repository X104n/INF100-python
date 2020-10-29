Suite = {
    "D": "Ruter",
    "H": "Hjerter",
    "S": "Spar",
    "C": "Kløver"
}

Value = {
    "A": "Ess",
    "2": "To",
    "3": "Tre",
    "4": "Fire",
    "5": "Fem",
    "6": "Seks",
    "7": "Sju",
    "8": "Åtte",
    "9": "Ni",
    "10": "Ti",
    "J": "Knekt",
    "Q": "Dame",
    "K": "Konge"
}

def bs(N):
    return print(Suite[str(N)])

def Tall(N):
    return print(Value[str(N)])

def Card(N):
    for i in N:
        try:
            S = Suite[i]
        except KeyError:
            V = Value[i]
    
    return print(str(S) + " " + str(V))

if __name__ == "__main__":
    Card("AD")
    Card("7H")
    Card("H7")