# Задача 2. Напишете програма, която показва знака (+ или -) от частното на две реални числа,
# без да го пресмята.


a = -4
b = -5
try:
    if a / b > 0:
        print(f"Divided result is +")
    else:
        print(f"Divided result is -")
except ZeroDivisionError:
    print("WARNING :not possible to divide to zero")
