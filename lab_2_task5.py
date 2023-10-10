a = int(input("Первое число - "))
b = int(input("Второе число - "))
if b == 0:
    print("Не дели на ноль ты че")
elif a%b==0:
    print(a/b)
else:
    print(a/b, a%b)
