import csv

def hilo():

    # Åpner først for å finne gjennomsittet slik at vi har et utgangspunkt for listene Høyest og Lavest
    with open("NO_ADM12.csv", newline='', encoding='iso-8859-1') as f:
        doc = csv.reader(f, delimiter=';')

        totalt = 0
        k = 0
        for snitt in doc:
            try:
                totalt += int(snitt[9])
                k += 1
            except ValueError:
                pass
            

        gjennomsnitt = int(totalt / k)


        Høyest = {1:gjennomsnitt, 2:gjennomsnitt, 3:gjennomsnitt, 4:gjennomsnitt, 5:gjennomsnitt}
        Lavest = {1:gjennomsnitt, 2:gjennomsnitt, 3:gjennomsnitt, 4:gjennomsnitt, 5:gjennomsnitt}

    # Så åpner vi filer for og finne de høyeste verdiene
    with open("NO_ADM12.csv", newline='', encoding='iso-8859-1') as f:
        doc = csv.reader(f, delimiter=';')

        for befolkning in doc:
            try:
                populasjon = int(befolkning[9])
            except ValueError:
                continue
            # Hvis det er over gjennomsnittet
            if populasjon >= gjennomsnitt:

                for k, v in Høyest.items():
                    
                    # Hvis den har en høyere verdi en de som er på topp listen
                    if populasjon > v:
                        Høyest[k] = populasjon
                        break

    # så de laveste verdiene
    with open("NO_ADM12.csv", newline='', encoding='iso-8859-1') as f:
        doc = csv.reader(f, delimiter=';')
        for folk in doc:
            try:
                populasjon = int(folk[9])
            except ValueError:
                continue

            # Hvis det er under gjennomsnittet
            if populasjon <= gjennomsnitt:

                for k, v in Lavest.items():

                    if populasjon < v:
                        Lavest[k] = populasjon
                        break


    return print(f"Top 5: {Høyest}. De minste 5: {Lavest}")



def print_fylke(num):

    Kommuner = {}

    with open("NO_ADM12.csv", newline='', encoding='iso-8859-1') as f:
        doc = csv.reader(f, delimiter=';')

        #Finner fylket
        for code in doc:

            if code[5] == "ADM2" and code[7] == str(num):
                Kommuner.setdefault(code[1], code[9])

            if code[5] == "ADM1" and code[7] == str(num):
                fylke = code[1]
    
    print("--------------------------------")
    print(f"{num} {fylke}")
    print("--------------------------------")
    for k, v in Kommuner.items():
        print(f"{k:16} {v}")



def loop():
    while True:
        inn = input("Serch word [q to quit]?")

        if inn == "q":
            break

        with open("NO_ADM12.csv", newline='', encoding='iso-8859-1') as f:
            doc = csv.reader(f, delimiter=';')
            for word in doc:
                if word[5] == "ADM1":
                    result = word[1].find(inn)
                    if result == 0:
                        print_fylke(word[7])
                        break
                    elif result == -1:
                        continue

            print("No matching fylke found. Try again")