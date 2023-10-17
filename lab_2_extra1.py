a = int(input("коэффицент A = "))
b = int(input("коэффицент B = "))
c = int(input("коэффицент C = "))
D = b**2-4*a*c
x1 = ((b*(-1))+(D**0.5))/(2*a)
x2 = ((b*(-1))-(D**0.5))/(2*a)
if D < 0:
    print("Нет корней")
elif D > 0:
    print("2 корня")
else:
    print("1 корень")
print(x1)
print(x2)