path = "./Dane-NF-2405/"

def main():
    filename = "skrot.txt"
    file = open(path+filename)
    maxim = 0
    count = 0
    for line in file:
        line = int(line.strip())
        if nieparzystySkrot(line) == 0:
            count+=1
            if line>maxim:
                maxim = line
    print(maxim, count)

def main2():
    filename = "skrot2.txt"
    file = open(path+filename)
    for line in file:
        line = int(line.strip())
        if nwd(line,nieparzystySkrot(line)) == 7:
            print(line, nieparzystySkrot(line),nwd(line,nieparzystySkrot(line)))

def nwd(a:int,b:int):
    while b > 0:
        a, b = b, a % b
    return a

def nieparzystySkrot(n:int):
    m = 0
    p = 1
    while n > 0:
        cyfra = n % 10
        if cyfra % 2 != 0:
            m += cyfra * p
            p *= 10
        n //= 10
    return m

if __name__=="__main__":
    main2()