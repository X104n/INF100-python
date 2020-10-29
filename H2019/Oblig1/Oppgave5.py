def loop(a,b,c):
    print(f"Verdier som er delelige på {c}:")
    for i in range(int(a), int(b) + 1):
        if i % int(c) == 0:
            print(i)    

if __name__ == "__main__":
    loop(
        input("Start: "),
        input("Stopp: "),
        input("n: ")
    )