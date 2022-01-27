Emner = ["Skole111", "Matte222", "Prog333"]

Karkaterer = {
    "Skole111": "A",
    "Matte222": "",
    "Prog333": "C"
}

def meny():
    txt = """
---------------------
 0 Meny
 1 Emneliste
 2 Legg til emne
 3 Sett karakter
 4 Karaktersnitt
 5 Avslutt
---------------------"""
    return txt

def emneliste(N):
    out = ""
    if N != "":
        N = int(N)
        if N % 100 == 0:
            for i in Emner:
                if int(i[-3]) == N / 100:
                    out += i + "\n"
    else:
        for i in Emner:
            out += i + "\n"
    return out
def emneadd():
    None

def karakterset():
    None

def snitt():
    None

print(meny())
while True:
    inn = input("Velg handling (0 for meny): ")
    try:
        int(inn)
        if 0 <= int(inn) <= 5:
            None
        else:
            print("Skriv et tall mellom 0 og 5")
            print("")
            continue
    except ValueError:
        print("Skriv et tall mellom 0 og 5")
        print("")
        continue
    inn = int(inn)
    if inn == 0:
        print(meny())
        continue
    if inn == 1:
        N = input(" - Nivå: ")
        print(emneliste(N))
        continue
    elif inn == 2:
        temp = input("Skriv inn et emne som du skal legge til: ")
        Emner.append(temp)
        continue
    elif inn == 3:
        temp = input("Emne: ")
        for i in Emner:
            if temp == i:
                kar = input("Karakter ('enter' for å slette) ")
                if kar != "":
                    if kar == "A" or "B" or "C" or "D" or "E" or "F":
                        