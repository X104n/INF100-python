def renteOkning(verdi, fra, til):
    V = verdi
    for i in range(int(fra) + 1, int(til) + 1):
        pluss = V * 0.02
        V = V + pluss
    return print(V)

renteOkning(2, 2000, 2019)