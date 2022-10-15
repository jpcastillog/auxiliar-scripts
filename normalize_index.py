import struct
from os.path import join

def normalize_ii(ii_file, q_file, o_ii_file, o_qfile, min_length=4096):
    print("-> ii file  readed: ", ii_file)
    print("-> query file readead: ", q_file)
    
    map_terms_ids = {}
    out = open(o_ii_file, "wb")
    f = open(ii_file, 'rb')
    f.seek(0)
    _1b = f.read(4)
    ub = f.read(4)
    
    _1 = struct.unpack('<I', _1b)[0]
    u = struct.unpack('<I', ub)[0]

    print("Singleton: ", _1, ",", u)

    out.write(_1b)
    out.write(ub)

    total_posting_lists = 0
    posting_list_geq = 0

    while True:
        b = f.read(4)
        if not b:
            break
        # Read size of posting list
        n = struct.unpack('<I',b)[0]
        
        if  n > min_length:
            out.write(b)
            posting_list = f.read(4*n)
            out.write(posting_list)
            map_terms_ids[total_posting_lists] = posting_list_geq
            posting_list_geq += 1
        else:
            f.seek(4*n, 1)
        total_posting_lists += 1
    f.close()
    out.close()

    print("Posting lists after filtering: ", posting_list_geq)
    print("End normalize index")
    
    # Reindexing queries 
    fq = open(q_file, "r")
    oq = open(o_qfile,"w")
    
    for line in fq:
        terms = line.strip().split(" ")
        terms = list(map(int, terms))
        new_terms_ids = [map_terms_ids[t] for t in terms]

        text = ""
        for t in new_terms_ids:
            text += (" "+str(t))
        text += "\n"
        oq.write(text)
    oq.close


terms_file = "cc-news.terms"
queries_file = "queries.pisa"
ii_file = "cc-news.docs"
path = "/media/jpcastillog/Respaldo 1/PISA/CC-News"
new_queries_file = "queries_4096.pisa"
new_ii_file = "cc-news_4096.docs"

terms_file = join(path, terms_file)
queries_file = join(path, queries_file)
ii_file = join(path, ii_file)
new_queries_file = join(path, new_queries_file)
new_ii_file = join(path, new_ii_file)

normalize_ii(ii_file, queries_file, new_ii_file, new_queries_file, 4096)