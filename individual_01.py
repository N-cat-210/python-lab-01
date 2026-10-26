print("Введите числа a и b")
a = int(input("a: "))
b = int(input("b: "))
if  b == 0:
    print("Ошибка! b не может быть равно 0")
else:
    Ans1 = round(a-b, 2)
    Ans2 = round(a*b, 2)
    Ans3 = round(a/b, 2)
    print(f"Результаты: {Ans1}; {Ans2}; {Ans3}")