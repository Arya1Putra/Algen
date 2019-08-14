import numpy as np
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

    print sort_y
    return parent
            


x=numpy.zeros((10,10))
x= [[0,51.4,81.1,34.5,19,36.5,32.2,17.5,48,22.7],
    [51.4,0,42.9,31.1,69.4,35,81.4,54.7,74.2,37.4],
    [81.1,42.9,0,47.4,96.7,70.5,109,88.6,116,70.9],
    [34.5,31.1,47.4,0,63.8,50.9,75.9,55.7,83,38],
    [19,69.4,96.7,63.8,0,47.1,42.4,15.5,45.9,33.2],
    [36.5,35,70.5,50.9,47.1,0,69.7,31.4,55.3,13.8],
    [32.2,81.4,109,75.9,42.4,69.7,0,47,76.1,56.8],
    [17.5,54.7,88.6,55.7,15.5,31.4,47,0,31.1,17.6],
    [48,74.2,116,83,45.9,55.3,76.1,31.1,0,41.4],
    [22.7,37.4,70.9,38,33.2,13.8,56.8,17.6,41.4,0]
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
while iterasi <=6:
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
    print cromo

    paren = seleksi(cromo,x)
    
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
result = {'rute' : paren, 'tot_jalur' : sort_y, 'konblade' : pemakaianbbmblade, 'konvario' : pemakaianbbmvario, 'konbeat' : pemakaianbbmbeat, 'koncbr' : pemakaianbbmcbr}
print(json.dumps(result))


