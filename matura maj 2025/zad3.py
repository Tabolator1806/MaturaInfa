import math
file = open("dane maj 23/dron.txt")

def pkt1():
    pary = 0
    for line in file:
        line = line[:-1]
        A=abs(int(line.split(" ")[0]))
        B=abs(int(line.split(" ")[1]))
        if nwd(A,B) > 1:
            pary+=1
    print(pary)
    
def nwd(a:int,b:int):
    if b==0:
        return a
    return nwd(b,a%b)
    return a

def pkt2():
    podpktA=0
    place = [0,0]
    placeList = []
    for line in file:
        A=int(line.split(" ")[0])
        B=int(line.split(" ")[1])
        placeList.append([A+place[0],B+place[1]])
        place[0]+=A
        place[1]+=B
        if place[0]<5000 and place[1]<5000:
            podpktA+=1
    for i in range(0,len(placeList)):
        for j in range(0,len(placeList)):
            for k in range(0,len(placeList)):
                sa, sb = placeList[i][0],placeList[i][1]
                la, lb = placeList[j][0],placeList[j][1]
                ra, rb = placeList[k][0],placeList[k][1]
                # print([la,lb],[sa,sb],[ra,rb],"||",(la+ra)//2,(lb+la)//2)
                if (sa == (la+ra)//2 and sb == (lb+rb)//2) and sa != la and sa != ra:
                    print([la,lb],[sa,sb],[ra,rb]) 
    print(podpktA)
    # print(placeList)

if __name__=="__main__":
    pkt2()