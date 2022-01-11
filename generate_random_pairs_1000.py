import random
from os.path import join


def generate_random_pairs(read_path, out_file, n_pairs = 1000):
    f = open(read_path, "r")
    
    termIds_4096 = []
    for line in f:
        data    = line.split(" ")
        termId  = int(data[0])
        size    = int(data[1])
        if size >= 4096:
            termIds_4096.append(termId)
    f.close()

    l_relation = []
    r_relation = []
    query_ids = []

    f = open(read_path, "r")
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
        
    query_ids = list(set(query_ids)) # unique ids 
    query_ids.sort()

    f_write = open(out_file, "w")

    ii_to_write = []
    n_il = 0
    for line in f:
        data = line.split(" ")
        if n_il == len(query_ids):
            break
        termId = int(data[0])
        if termId == query_ids[n_il]:
            f_write.write(line)
    
    f_write.close()

ii_path = "../../GOV2/index/ii/absDocIDS/gov2_url_absolute_freqs.ii"
save_path = "./data/ii_random_1000.txt"

generate_random_pairs(ii_path, save_path)