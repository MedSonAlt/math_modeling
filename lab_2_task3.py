a = int(input("Год - "))
if a%4==0 and a%100!=0:
    print("Високосный")
elif a%4==0 and a%100==0 and a%400==0:
    print("Високосный")
else:
    print("Не високосный")



