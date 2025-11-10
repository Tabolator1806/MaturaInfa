path = "pliki/dane maj 23/"
fileName = "symbole_przyklad.txt"

file = open(path+fileName)
#ZAD 2.1
# for line in file:
#     line=line.strip()
#     palindrom = True
#     for i in range(0,6):
#         if line[i]!=line[11-i]:
#             palindrom=False
#             break
#     if palindrom:
#         print(line)

# ZAD 2.2
fileArray = []

# for line in file:
#     line = line.strip()
#     fileArray+=[line]

# # print(fileArray)
# square = []

# for j in range(0,len(fileArray)-2):
#     for i in range(0,10):
#         szukane = fileArray[j][i]
#         znalezione = True
#         gdzie = (0,0)
#         for x in range(0,3):
#             if not znalezione:
#                 break
#             for y in range(0,3):
#                 if fileArray[j+y][i+x]!=szukane:
#                     znalezione=False
#                     break
#                 else:
#                     gdzie=(i+2,j+2)
#         if znalezione:
#             square.append(gdzie)
# print(square)

#Zad 2.3
# biggest=0
# foundline = ""
# for line in file:
#     line = line.strip()[::-1]
#     suma = 0
#     for j,letter in enumerate(line):
#         if letter=="+":
#             suma+=1*(3**j)
#         elif letter=="*":
#             suma+=2*(3**j)
#     if suma>biggest:
#         biggest=suma
#         foundline=line
# print(biggest,foundline)

#Zad 2.4
suma = 0
sumatrzy = ""
for line in file:
    line = line.strip()[::-1]
    for j,letter in enumerate(line):
        if letter=="+":
            suma+=1*(3**j)
        elif letter=="*":
            suma+=2*(3**j)
suma2 = suma
while suma2 > 0:
    r = suma2 % 3
    if r == 0:
        sumatrzy+="o"
    elif r == 1:
        sumatrzy+="+"
    elif r== 2:
        sumatrzy+="*"
    suma2 //=3
print(suma,sumatrzy[::-1])