d1 = int(input("Enter d1: "))
d2 = int(input("Enter d2: "))
d3 = int(input("Enter d3: "))

print('\n')

ll = int(input("Enter lower limit: "))
ul = int(input("Enter upper limit: "))

print('\n')

#d1=10,d2=13,d3=15

term = 'qwe'

def d1d2d3(term):
    dic1 = []
    y1 = 0
    for x1 in range(ll, ul+1):
        if (d1%x1==0) and (d2%x1==0) and (d3%x1==0):
            print(x1)
            return dic1.append(x1)
    for y1 in range(len(dic1)):
        y1+=1
    term = dic1
    print(term)
def d1d2(dic1, term):
    dic2 = []
    y2 = 0
    for x2 in range(ll, ul+1):
        if (d1%x2==0) and (d2%x2==0) and x2 not in term:
            dic2.append(x2)
    for y2 in range(len(dic2)):
        y2+=1
    term = dic1 + dic2
def d1d3(dic1, dic2, term):
    dic3 = []
    y3 = 0
    for x3 in range(ll, ul+1):
        if (d1%x3==0) and (d3%x3==0) and x3 not in term:
            dic3.append(x3)
    for y3 in range(len(dic3)):
        y3+=1
    term = dic1 + dic2 + dic3
def d2d3(dic1, dic2, dic3, term):
    dic4 = []
    y4 = 0
    for x4 in range(ll, ul+1):
        if (d2%x4==0) and (d3%x4==0) and x4 not in term:
            dic4.append(x4)
    for y4 in range(len(dic4)):
        y4+=1
    term = dic1 + dic2 + dic3 + dic4

#only group
def dq(dic1, dic2, dic3, dic4, term):
    zic1 = []
    z1 = 0
    for n1 in range(ll, ul+1):
        if (d1%n1==0) and n1 not in term:
            zic1.append(n1)
    for z1 in range(len(zic1)):
        z1+=1
    term = dic1 + dic2 + dic3 + dic4 + zic1
def dw(dic1, dic2, dic3, dic4, zic1, term):
    zic2 = []
    z2 = 0
    for n2 in range(ll, ul+1):
        if (d2%n2==0) and n2 not in term:
            zic2.append(n2)
    for z2 in range(len(zic2)):
        z2+=1
    term = dic1 + dic2 + dic3 + dic4 + zic1 + zic2
def de(dic1, dic2, dic3, dic4, zic1, zic2, term):
    zic3 = []
    z3 = 0
    for n3 in range(ll, ul+1):
        if (d3%n3==0):
            zic3.append(n3)
    for z3 in range(len(zic3)):
        z3+=1
    term = dic1 + dic2 + dic3 + dic4 + zic1 + zic2 + zic3

d1d2d3(term)
d1d2(dic1, term)
d1d3(dic1, dic2, term)
d2d3(dic1, dic2, dic3, term)
dq(dic1, dic2, dic3, dic4, term)
dw(dic1, dic2, dic3, dic4, zic1, term)
de(dic1, dic2, dic3, dic4, zic1, zic2, term)

print(term)