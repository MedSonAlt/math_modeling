colvo = int(input("кол-во чисел ряда Фибоначчи - "))
a = 1
b = 1
print(a, b, end=" ")
colvo -= 1
for i in range(colvo):
    i = i + 2
    c = a + b
    a = b
    b = c
    print(c, end=" ")