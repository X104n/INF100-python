import random

def simulate(rounds):

    brett = {0 : 10_000, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0, 15 : 0}

    # Hvor mange runder som skal gjøres
    for runde in range(rounds):

        #Temp brett:
        tempBrett = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0, 15 : 0}

        # Ser hvor spillere er på brettet
        for plassering in brett:

            

            # For hver spiller i plasseringen
            for spillere in range(brett[plassering]):
                
                terning = random.randint(1,6)
                flytt_til = plassering + terning
                
                # Land på 3 flytt til 8
                if flytt_til == 3:
                    tempBrett[8] += 1
                
                # Land på 9 flytt til 13
                elif flytt_til == 9:
                    tempBrett[13] += 1

                # Land på 10 flytt til 2
                elif flytt_til == 10:
                    tempBrett[2] += 1

                # Land på 15 flytt til 6
                elif flytt_til == 15:
                    tempBrett[6] += 1

                # Ellers bare flytt
                else:
                    if flytt_til > 15:
                        tempBrett[flytt_til - 15] += 1
                    else:
                        tempBrett[flytt_til] += 1




        brett.update(tempBrett)


    txt = ""
    for i in brett.values():
        prosent = i/10_000*100
        txt = txt + str(int(prosent)) + " "

    return print(txt)


simulate(20)