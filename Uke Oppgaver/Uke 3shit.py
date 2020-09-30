#Oppgave 1
"""
a = int(input("Tall 1: "))
b = int(input("Tall 2: "))

def egen_max(a, b):
    egen_max = (a + b + abs(a - b))//2
    return egen_max

def egen_min(a, b):
    egen_min = (a + b - abs(a - b))//2
    return egen_min

print(str(egen_max(a, b)) + "\n" + str(max(a, b)) + "\n" + str(egen_min(a, b)) + "\n" + str(min(a, b)))
"""
#Oppgave 2
"""
def f_til_c(tf):
    tc = (tf - 32) * 5/9
    return tc

def c_til_f(tc):
    tf = 9/5 * tc + 32
    return tf

tf = int(input("Gi en temp. i Fahrenheit: "))
tc = f_til_c(tf)
print("Temp i Celsius: ", round(f_til_c(tf), 1))
print("Temp i Far.: ", round(c_til_f(tc), 1))
"""
#Oppgave 3

def box(text):
    x = len(text)
    print("\n" + "=" * (x + 4))
    print("= " + text + " =")
    print("=" * (x + 4))
    return " "

text = input("Hva heter du? ")
print(box(text) + "\nJeg håper du har en fin dag!")