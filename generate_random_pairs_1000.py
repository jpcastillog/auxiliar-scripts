import random
from os.path import join


def generate_random_pairs(read_path, out_ii, out_query_log, n_pairs = 1000):
    f = open(read_path, "r")
    
    termIds_4096 = []
    for line in f:
        data    = line.split(" ")
        termId  = int(data[0])
        size    = int(data[1])
        if size >= 4096:
            termIds_4096.append(termId)
    f.close()

    print("-> Listas invertidas > 4096 OK")

    l_relation = []
    r_relation = []
    query_ids  = []
    
    # generate random pairs
    for i in range (n_pairs):
        l = random.choice(termIds_4096)
        l_relation.append(l)
        r = random.choice(termIds_4096)
        if r == l:
            while r == l:
                r = random.choice(termIds_4096)
                r_relation.append(r)
        else:
            r_relation.append(r)
        query_ids.append(l)
        query_ids.append(r)
    
    print("-> Se generaron 1000 pares random exitosamente!")
    query_ids = list(set(query_ids)) # unique ids 
    query_ids.sort()

    f_write = open(out_ii, "w")
    f_q_write = open(out_query_log, "w")
    f_read = open(read_path, "r")
    print ("-> Escribiendo ii y QueryLog")
    n_il = 0
    for line in f_read:
        data = line.split(" ")
        if n_il == len(query_ids):
            break
        termId = int(data[0])
        if termId == query_ids[n_il]:
            f_write.write(line)
            n_il += 1

    for i in range(n_pairs):
        f_q_write.write("{0} {1}\n".format(l_relation[i], r_relation[i]))
    f_write.close()
    f_read.close()
    print ("->  ii y QueryLog escritos exitosamente!!!")

ii_path = "../../GOV2/index/ii/absDocIDS/gov2_url_absolute_freqs.ii"
# ii_path = "./data/example.txt"
save_path_ii = "./data/ii_random_1000.txt"
save_path_qlog = "./data/queryLog_1000pairs.txt"

generate_random_pairs(ii_path, save_path_ii, save_path_qlog)