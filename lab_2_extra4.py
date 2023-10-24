a = int(input("Числа - "))
a1 = a
if a%3 == 0 or a%2 == 0 or a%5 == 0 or a%7 == 0:
    while a != 1:
        if a%2 == 0:
            a = a//2
            print(2, end="*")
        elif a%3 == 0:
            a = a//3
            print(3, end="*")
        elif a%5 == 0:
            a = a//5
            print(5, end="*")
        elif a%7 == 0:
            a = a//7
            print(7, end="*")
        else:
            break
    print(f"{a}={a1}")
else:
    print(f"Это простое число, бро, ну если интересно то это будет ну {a} и 1 :D")