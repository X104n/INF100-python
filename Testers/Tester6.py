# def is_divisible(a,b):
#     try:
#         if a%b == 0:
#             return "True"
#         else:
#             return "False"
#     except ZeroDivisionError:
#         return "Error!"

# print(is_divisible(-4,2))



# def is_prime(a):
#     for i in range(2,a):
#         if a % i == 0:
#             return print("False")

#     return print("True")

# is_prime(53)



# def evenize(l):
#     temp = []
#     for i in l:
#         if i % 2 == 0:
#             temp.append(i)
#         else:
#             temp.append(int(i)+1)
#     return print(temp)

# liste = [-3,4,5,9,0]
# evenize(liste)



# def pos_sum(l):
#     temp = 0
#     for i in l:
#         if i > 0:
#             temp += int(i)
#     return print(temp)

# pos_sum(liste)



# def plural(word):
#     l = len(word)
#     if word[l-2:l] == "ch":
#         return word + "es"
#     elif word[l-2:l] == "sh":
#         return word + "es"
#     elif word[l-1] == "s":
#         return word + "es"
#     elif word[l-1] == "y":
#         return word[:-1] + "ies"
#     else:
#         return word + "s"

# print(plural("witch"))



# l = ["apple", "apple", "grape", "banana", "pear", "kiwi", "kiwi", "kiwi"]
# def count(l):
#     dic = {}
#     for i in l:
#         dic.setdefault(i,0)
#         dic[i] += 1
#     return dic



# dic = count(l)

# for k, i in dic.items():
#     if i > 1:
#         k = plural(k)
#     print(f"{i} {k}")



# def center(s, width):
#     txtM = s.replace(" ","")
#     width = width - len(txtM)
#     txtV = (width // 2) * "␣"
#     txtH = ((width // 2) + (width % 2)) * "␣"
#     print(f"{txtV}{txtM}{txtH}")

# center("               piss         aa", 30)



# def print_tree(width, height):
#     pass


"""
Poeng = {}
log = []

def reg_incident(navn, beskrivelse, poeng):
    Poeng.setdefault(navn, 0)
    Poeng[navn] += poeng
    log.append([navn, beskrivelse, poeng])

reg_incident("Lise", "Slem", -1)
reg_incident("Roger", "Go gutt", 50)

print(Poeng)
print(log)

def is_nice(navn):
    if abs(int(Poeng[navn])) == int(Poeng[navn]):
        return "True"
    else:
        return "False"
"""



#is_nice("Lise")
#is_nice("Roger")



"""
def status_all():
    temp = {}
    for i in Poeng.keys():
        value = is_nice(i)
        temp.setdefault(i,value)
    return temp

status_all()



presang = [(23791, 'Dinosaurfigur', 0.3, 'AD-339'), 
(23792, 'Stripete slips', 0.2, 'ZR-201'),
(23793, 'Lekekjøkken', 5.3, 'UB-799'), 
(23794, 'PuffinBoard v0.1', 0.01, 'ZZ-237')
]


def assign_presents():
    temp = {}
    x = 0
    for k, v in status_all().items():
        if v == "True":
            temp.setdefault(k, presang[x])
            x += 1
    return temp

print(assign_presents())
"""
































def f(x):
    x = x + 1
    return x
x = 3
f(x)
print(x)



def f(x):
    x[0] = x[0] + 1
    return x
x = [3]
f(x)
print(x)


