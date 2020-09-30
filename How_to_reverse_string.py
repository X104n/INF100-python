while True:
    txt = input("Et ord: ")
    if not txt:
        break
    reverse = txt[::-1]
    print(reverse)

print("Bye!")