path = "./Dane-NF-2405/"

def zad1():
    filename = "liczby.txt"
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

if __name__=="__main__":
    zad1()