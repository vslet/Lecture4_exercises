# Задача 3. Напишете програма, която намира най-голямото по стойност число, измежду три
# дадени числа

a = 111
b = 29
c = 413

#print(max(a, b, c))

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c>a and c>b:
    print(c)
