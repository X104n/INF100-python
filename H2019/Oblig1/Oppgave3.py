Valutta = {
    "EUR": 9.68551,
    "USD": 8.50373,
    "GBP": 11.0134,
    "SEK": 0.92950,
    "AUD": 6.06501,
    "NOK": 1.00000
}

def konverter(Verdi, Kurs):
    return Verdi * Valutta[Kurs]

def tilbake(Verdi, Kurs):
    return Verdi / Valutta[Kurs]

if __name__ == "__main__":
    
    print("Din kurs i NOK fra oppgit verdi er: " + str(konverter(100, "SEK")))

    print("Din kurs i oppgit verdi fra NOK er : " + str(tilbake(100, "SEK")))