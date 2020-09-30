a = 5
b = 9

print(a > b)
print('a > b =', a > b)
# avoid repetition with f-strings and =
print(f'{a > b = }')

# rewrite as f-string-=
print(a == b)
print(a <= b)

print(3 <= a <= 7 < b < 10)

navn_1 = 'Alice'
navn_2 = 'Albert'

print(f'{navn_1 < navn_2 = }')
print(navn_1 == navn_2)
print(navn_1 > navn_2)

matches = navn_1 == "Bob"
print(f'{matches = }')