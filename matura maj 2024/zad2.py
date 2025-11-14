#Zad 2
n = int(input("Podaj n: "))
b = 1
c = 0
count = 0
while n>0:
    a = n % 10
    n = n // 10
    if a % 2 == 0:
        c = c + b * (a // 2)
    else:
        c = c + b
        count += 1
    b *= 10
print(c, count)