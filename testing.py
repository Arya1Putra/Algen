import sys, json, numpy as np, math

#Load the data that PHP sent us
try:
    data = json.loads(sys.argv[1])

except:
    print('error')
    sys.exit(1)
query = data['words']

#ambil query inputan user, simpan dalam list_query
list_query = []
for i in range(len(query)):
    list_query.append(query[i])

#baca database vsm_term dan vsm_weight
f = open("vsm_term.txt", "r")
g = open("vsm_weight.txt", "r")
lines_term = f.readlines()
lines_weight = g.readlines()

#menyimpan setiap baris vsm_term dan vsm_weight
result_vsm = []
result_weight = []
for x in lines_term:
    x = x.replace('\n','')
    x = x.split()
    result_vsm.append(x)
for x in lines_weight:
    x = x.replace('\n', '')
    x = x.split()
    result_weight.append(x)
f.close()
g.close()

#hitung cosine similarity#
cosine = np.zeros(len(result_vsm), dtype="float32")
index_vsm = np.empty(len(result_vsm), dtype="int32")
div_vector_query = math.sqrt(len(list_query))
for i in range(len(result_vsm)):
    div_vector_db = 0.0
    for j in range(len(result_vsm[i])):
        x = int(result_weight[i][j])
        for k in range(len(list_query)):
            if list_query[k] == result_vsm[i][j]:
                cosine[i] += x * 1
        div_vector_db += math.pow(x, 2)
    index_vsm[i] = i + 1
    div_vector_db = math.sqrt(div_vector_db)
    divider_cosine = div_vector_db + div_vector_query
    cosine[i] = cosine[i] / divider_cosine

#urutkan nilai cosine similarity
for i in range(len(result_vsm)):
    j = i + 1
    for j in range(len(result_vsm) - 1):
        if cosine[j] < cosine[j + 1]:
            temp = cosine[j]
            idx = index_vsm[j]
            cosine[j] = cosine[j + 1]
            index_vsm[j] = index_vsm[j + 1]
            cosine[j + 1] = temp
            index_vsm[j + 1] = idx
cosine = cosine.tolist()
index_vsm = index_vsm.tolist()
# print index_vsm
# print cosine
#Generate some data to send to PHP
result = {'status' : 'yes', 'index' : index_vsm, 'cosine' : cosine}
# Send it to stdout (to PHP)
print(json.dumps(result))