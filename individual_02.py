a2 = int(input("Введите a2: "))
a1 = int(input("Введите a1: "))
b2 = int(input("Введите b2: "))
b1 = int(input("Введите b1: "))
s = a1 + b1
s1 = s % 10
c = s // 10
s2 = a2 + b2 + c
if (s2>=10):
    print ("Ошибка! Сумма а2 и b2 слишком большая")
else:
    print(f"Цифры суммы: {s2}; {s1}")
