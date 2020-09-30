#Oppgave 1
#navn = input("Hva heter du? ")
#print(navn)
#print(len(navn))

#Oppgave 2
#alder = input("Hvor gammel er du? ")
#print("Du blir 100 år om " + str(100 - int(alder)) + " år!")

#Oppgave 3
#f = input("Temperatur i farenheit: ")
#c = (int(f) - 32) * 5/9
#print("Temperatur i Celsius: " + str(c))

#Oppgave 4
#tekst = input("Tekst: ")
#x = len(tekst)
#print("=" * (x + 4))
#print("= " + tekst + " =")
#print("=" * (x + 4))

#Oppgave 5
tekst = input("Tekst: ")
x = len(tekst)
tall = int(input("Tall: ",))
y = tall - x - 2
print("=" * tall)
print("=" + " " * (y//2) + tekst + " " * (y//2 + y%2) + "=")
print("=" * tall)