def FtilC(C):
    return (C*1.800) + 32

def svett(N):
    if N > 60:
        return "Jeg svetter i hjel!"
    return "Jeg har det bra"
    
def kovert():
    print("Clesius   Fahrenheit")
    for i in range(0,101,10):
        #a = svett(i)
        x = int(FtilC(i))
        print(f"{i:7d}{x:13d}")
        #{a:10d}

kovert()
