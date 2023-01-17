# Задача 4. Напишете програма, която за дадена цифра (0-9), зададена като вход, извежда името
# на цифрата на български език.
try:
    user_input = int(input("Please enter a number between 0 and 9: "))
    if user_input == 0:
        print("Нула")
    elif user_input == 1:
        print("Едно")
    elif user_input == 2:
        print("Две")
    elif user_input == 3:
        print("Три")
    elif user_input == 4:
        print("Четири")
    elif user_input == 5:
        print("Пет")
    elif user_input == 6:
        print("Шест")
    elif user_input == 7:
        print("Седем")
    elif user_input == 8:
        print("Осем")
    elif user_input == 9:
        print("Девет")
    else:
        print("ГРЕШКА: Избраното число ТРЯБВА да е между 0 и 9")
except ValueError:
    print("Моля въведете само цифри!")
