import numpy
import random
import pandas
import json
import sys

#fungsi objektif = jumlah kilometer 

def seleksi(par,x):
    fitness= numpy.zeros(10)
    for i in range (0,10):
        for j in range (0,5):
            a=int(par[i,j])
            b=int(par[i,j+1])
            fitness[i]= fitness[i] + x[a][b]
    y=fitness
    sort_y=numpy.sort(y)
    x=len(fitness)/2
    parent=numpy.zeros((5,10))
    min1 = sort_y[0]
    min2 = sort_y[1]
    min3 = sort_y[2]
    min4 = sort_y[3]
    min5 = sort_y[4]
    
    for i in range (0,10):
        if y[i] == min1:
            indexmin1 =i
        if y[i] == min2:
            indexmin2 =i
        if y[i] == min3:
            indexmin3 =i
        if y[i] == min4:
            indexmin4 =i
        if y[i] == min5:
            indexmin5 =i
    for i in range (0,10):
        parent[0,i] = par[indexmin1,i]
        parent[1,i] = par[indexmin2,i]
        parent[2,i] = par[indexmin3,i]
        parent[3,i] = par[indexmin4,i]
        parent[4,i] = par[indexmin5,i]

    return parent
            


x=numpy.zeros((10,10))
x= [[0,36.3,31.4,39.6,34.1,38.1,35.4,19.1,38,63.2],
    [36.3,0,66.7,12.8,12.2,11.3,13.6,9.3,18.5,42.7],
    [31.4,66.7,0,65.4,53.1,63.9,54.4,40.3,57.6,90.2],
    [39.6,12.8,65.4,0,15.1,0.85,12.6,8.2,7.9,28.9],
    [34.1,12.2,53.1,15.1,0,13.6,1.7,5.6,4.2,31.9],
    [38.1,11.3,63.9,0.85,13.6,0,11.7,7.3,7.5,37.7],
    [35.4,13.6,54.4,12.6,1.7,11.7,0,5,3.5,31],
    [19.1,9.3,40.3,8.2,5.6,7.3,5,0,0.9,28.8],
    [38,18.5,57.6,7.9,4.2,7.5,3.5,0.9,0,28.1],
    [63.2,42.7,90.2,28.9,31.9,37.7,31,28.8,28.1,0]
    ]

##x = [
##    [0,51400,81100,34500,19000,36500,32200,17500,48000,22700],
##    [51400,0,42900,31100,69400,35000,81400,54700,74200,37400],
##    [81100,42900,0,47400,96700,70500,109000,88600,116000,70900],
##    [34500,31100,47400,0,63800,50900,75900,55700,83000,38000],
##    [19000,69400,96700,63800,0,47100,42400,15500,45900,33200],
##    [36500,35000,70500,50900,47100,0,69700,31400,55300,13800],
##    [32200,81400,109000,75900,42400,69700,0,47000,76100,56800],
##    [17500,54700,88600,55700,15500,31400,47000,0,31100,17600],
##    [48000,74200,116000,83000,45900,55300,76100,31100,0,41400],
##    [22700,37400,70900,38000,33200,13800,56800,17600,41400,0],
##    ]

par=numpy.zeros((10,10))
for i in range (0,10):
    n= random.sample(range(0,10),10)
    par[i]=n

paren = numpy.zeros((5,10))
paren = seleksi(par,x)

crov= numpy.zeros((4,10))
c = numpy.zeros((5,10))
cromo = numpy.zeros((10,10))
mut = numpy.zeros((3,10))
a = numpy.zeros((2,5))
iterasi = 1
ma=0
thres=1
while iterasi <=100 and thres>0.01 :
    #crossover 
    for i in range (0,2):
        for j in range (0,10):
            crov[i][j]=paren[i][j]
    totb=0
    for i in range (0,1):
        for j in range (0,5):
            c[i][j]=crov[i][j]
            c[i+1][j]=crov[i+1][j]
        for j in range (5,10):
            for k in range (0,10):
                    if (crov[i+1][k] not in c[i]):
                        c[i][j]=crov[i+1][k]
                    if (crov[i][k] not in c[i+1]):
                        c[i+1][j]=crov[i][k]
                                  
    #mutasi thrors
    muran= random.sample(range(0,10),3)
    for i in range (0,3):
        for j in range (0,10):
            mut[i][j]=paren[i+2][j]
    for i in range (2,5):
        for j in range (0,10):
            c[i][j]=mut[i-2][j]
        nu1 =c[i][muran[0]]
        nu3 =c[i][muran[2]]
        nu2 =c[i][muran[1]]
        c[i][muran[0]]= nu3
        c[i][muran[1]]= nu1
        c[i][muran[2]]= nu2
    #GANTAIII!!
    for i in range (0,5):
        for j in range (0,10):
            cromo[i][j]=paren[i][j]
        for i in range (5,10):
            for j in range (0,10):
                  cromo[i][j]= c[i-5][j]

    paren = seleksi(cromo,x)
    fit= numpy.zeros(5)
    for i in range (0,5):
        for j in range (0,5):
               a=int(paren[i,j])
               b=int(paren[i,j+1])
               fit[i]= fit[i] + x[a][b]
    ya=fit
    sort_ya=numpy.sort(ya)
    mx=sort_ya[0]
    thres=mx-ma
    ma=mx
    iterasi=iterasi+1
    
fitness= numpy.zeros(5)
for i in range (0,5):
    for j in range (0,5):
           a=int(paren[i,j])
           b=int(paren[i,j+1])
           fitness[i]= fitness[i] + x[a][b]
y=fitness
sort_y=numpy.sort(y)

literblade= 0.01618
litervario125 = 0.01682
literbeat = 0.01709
litercbr150r = 0.0264
pemakaianbbmblade = []
pemakaianbbmbeat = []
pemakaianbbmvario = []
pemakaianbbmcbr = []
for i in range (0,5):
    d=sort_y[i]*literblade
    pemakaianbbmblade.append(d)
for i in range (0,5):
    e=sort_y[i]*litervario125
    pemakaianbbmvario.append(e)
for i in range (0,5):
    g=sort_y[i]*literbeat
    pemakaianbbmbeat.append(g)
for i in range (0,5):
    h=sort_y[i]*litercbr150r
    pemakaianbbmcbr.append(h)

paren=numpy.array(paren).tolist()
sort_y=numpy.array(sort_y).tolist()
pamakaianbbmblade=numpy.array(pemakaianbbmblade).tolist()
pamakaianbbmbeat=numpy.array(pemakaianbbmbeat).tolist()
pamakaianbbmvario=numpy.array(pemakaianbbmvario).tolist()
pamakaianbbmcbr=numpy.array(pemakaianbbmcbr).tolist()
result = {'rute' : n, 'tot_jalur' : sort_y, 'konblade' : pemakaianbbmblade, 'konvario' : pemakaianbbmvario, 'konbeat' : pemakaianbbmbeat, 'koncbr' : pemakaianbbmcbr}
print(json.dumps(result))


