def find(name, number):
    b = 0
    Fname = False
    Fnumber = False
    with open("telefon.txt", "r") as f:
        for line in f:
            b = 0
            for word in line.split():
                if word == name:
                    Fname = True
                    b = 1
                if word == number and b == 1:
                    Fnumber = True
                if Fname and Fnumber:
                    return True
    if Fname and Fnumber != True:
        return False

def del2(name, n1, n2):
    if find(name, n1):
        with open ("telefon.txt", "r") as f:
            with open("telefon3.txt", "w") as wf:
                for line in f:
                    if line == f"{name} {n1}\n":
                        wf.write(f"{name} {n2}\n")
                    else:
                        wf.write(line)
    else:
        return print("Something went wrong")


if __name__ == "__main__":
    navn = input("Navn: ")
    nummer = input("Skriv nummer her: ")
    nummer2 = input("Skriv nummer 2 her: ")
    del2(navn, nummer, nummer2)
    

#99455443