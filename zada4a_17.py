#Задача 17. Напишете програма, която чете две цели числа (N1 и N2) и оператор, с който да се
# извърши  дадена математическа операция с тях . Възможните операции
# са: събиране (+), изваждане (-), умножение (*), деление (/) и модулно деление (%). При
# събиране, изваждане и умножение на конзолата трябва да се отпечата резултата и дали той
# е четен или нечетен. При обикновено деление – единствено резултата, а при модулно деление
# – остатъка. Трябва да се има предвид, че делителят може да е равен на нула (= 0), а на нула не
# се дели. В този случай трябва да се отпечата специално съобщение.

n_1 = 0
n_2 = 2
act = "+"
try:
    if act == "+":
        sum = n_1 + n_2
        if sum > 0:
            sum1 = "even"
            print(f"{n_1} {act} {n_2} = {sum} - {sum1}")
        if sum < 0:
            sum2 = "odd"
            print(f"{n_1} {act} {n_2} = {sum} - {sum2}")

    if act == "-":
        minus = n_1 - n_2
        if minus > 0:
            minus_1 = "even"
            print(f"{n_1} {act} {n_2} = {minus} - {minus_1}")
        if minus < 0:
            minus_2 = "odd"
            print(f"{n_1} {act} {n_2} = {minus} - {minus_2}")

    if act == "*":
        mult = n_1 * n_2
        if mult > 0:
            mult_1 = "even"
            print(f"{n_1} {act} {n_2} = {mult} - {mult_1}")
        if mult < 0:
            mult_2 = "odd"
            print(f"{n_1} {act} {n_2} = {mult} - {mult_2}")

    if act == "/":
        divide = n_1 / n_2
        divide_2 = round(divide,2)
        print(f"{n_1} / {n_2} = {divide_2}")

    if act == "%":
        mod_div = n_1 % n_2
        #divide_2 = round(divide,2)
        print(f"{n_1} % {n_2} = {mod_div}")
except ZeroDivisionError:
    print(f"Cannot divide",{n_1},"by zero")