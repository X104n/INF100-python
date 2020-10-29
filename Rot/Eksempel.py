def avstand(tall_1, tall_2):
    """Regn ut avstand mellom to tall"""
    avstand = abs(tall_1 - tall_2)
    return(avstand)


def den_er_feil():
    """Denne funksjonen skulle ikke kjøre, men det fungerer uansett?"""
    abc = 5
    return xyz # forventer NameError... her


print('vvvvvvvvvvvvvvvv')

avst_1 = avstand(14, -9)
avst_2 = avstand(-36, 23)

print("Avstanden mellom tallene 14 og -9 er", avst_1)
print("Avstanden mellom tallene -36 og 23 er", avst_2)

print("Den største av disse avstandene er", max(avst_1, avst_2))

print('^^^^^^^^^^^^^^^^')