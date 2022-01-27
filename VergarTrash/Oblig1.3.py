def meny():
    txt = """
--------------------
 1 - vis saldo
 2 - innskudd
 3 - uttak
 4 - renteoppgjør
 5 - avlsutt
--------------------"""
    return txt

#Printer ut saldoen
def visSaldo():
    return print(saldo)

#Sjekekr om ting er et tall eller bare tull
def nummer(N):
    try:
        int(N)
    except ValueError:
        print("Skriv inn et gyldig nummer")
        return "STOP"
    return int(N)

#Legger til mer penger i saldoen
def innskudd(N):
    global saldo
    if saldo + int(N) > 1000000 and saldo < 1000000:
        print("gratulerer, du får nå bonusrente")
    saldo = saldo + int(N)
    return saldo

def uttak(N=0):
    global saldo
    if saldo < int(N):
        print("overtrekk")
        print("Saldo: " + str(saldo))
    else:
        if saldo - int(N) and saldo > 1000000:
            print("du har nå ordinær rente")
        saldo = saldo - int(N)
    return saldo


def renteoppgjør(saldo):
    if saldo > 1000000:
        saldo = saldo + saldo * 0.02
    else:
        saldo = saldo + saldo * 0.01
    return saldo
    
saldo = 500

while True:
    print(meny())
    inn = input("velg handling (0 for): ")
    try:
        inn = int(inn)
        if 0 <= inn <= 5:
            None
        else:
            print("Skriv inn et tall mellom 0 og 5")
            continue
    except ValueError:
        print("Skriv inn et tall mellom 0 og 5")
        continue

    if inn == 0:
        print(meny())
        continue

    if inn == 1:
        visSaldo()
        continue

    if inn == 2:
        N = input("Beløp: ")
        if nummer(N) == "STOP":
            continue
        innskudd(N)
        continue

    if inn == 3:
        N = input("Beløp: ")
        if nummer(N) == "STOP":
            continue
        uttak(N)
        continue

    if inn == 4:
        renteoppgjør(saldo)
        continue

    if inn == 5:
        print("Snakkes")
        break