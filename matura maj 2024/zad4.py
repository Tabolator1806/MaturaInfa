path = "./Dane-NF-2405/"

def zad1():
    filename = "liczby_przyklad.txt"
    file = open(path+filename).readlines()
    dzielniki = file[0].split(" ")
    liczby = file[1].split(" ")

    count = 0

    for dzielnik in dzielniki:
        dzielnik = int(dzielnik)
        for liczba in liczby:
            liczba = int(liczba)
            if liczba % dzielnik == 0:
                count+=1
                break
    print(count)

def zad2():
    filename = "liczby.txt"
    file = open(path+filename).readlines()
    dzielniki = file[0].split(" ")
    dzielniki2 = []
    for dzielnik in dzielniki:
        dzielniki2.append(int(dzielnik))
    dzielniki2.sort()
    dzielniki2.reverse()
    print(dzielniki2[100])

def zad3():
    filename = "liczby.txt"
    file = open(path+filename).readlines()
    dzielniki = list(map(int,file[0].split(" ")))
    liczby = list(map(int,file[1].split(" ")))
    dzielniki.sort()
    wyniki = []
    for liczba in liczby:
        liczba2 = liczba
        for dzielnik in dzielniki:
            if liczba2 % dzielnik == 0:
                liczba2 //= dzielnik
            if liczba2 <= 1:
                wyniki.append(liczba)
                break
    print(wyniki)


if __name__=="__main__":
    zad3()