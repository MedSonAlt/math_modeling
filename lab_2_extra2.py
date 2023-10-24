a = int(input("Сторона А - "))
b = int(input("Сторона B - "))
c = int(input("Сторона C - "))
if a < (b + c):
    if a==b or a == c or b==c:
        print("Равнобедренный")
    elif a==b and b==c:
        print("Равносторонний")
    else:
        print("Произвольный")
else:
    print("Такого треугольника не существует")