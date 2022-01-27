import numpy as np
# a = 5
# b = 7
# a, b = b, a
# print(a)
# print(b)

my_garden = [
        ["grass", "moss"],
        ["moss", "strawberry"],
        ["moss","rock"]
    ]

other_garden = [
    ["grass", "raspberry"],
    ["grass", "strawberry"],
    ["strawberry","rock"]
]

data1 = np.array(my_garden)

ein = data1[1,1]

data2 = np.array(other_garden)

to = data2[2,1]

print(ein)
print(to)

data1[1,1], data2[2,1] = data2[2,1], data1[1,1]

print(ein)
print(to)