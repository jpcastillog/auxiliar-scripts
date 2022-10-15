import struct
from os.path import join

def read_ii(file):
    size_posting_lists = []
    print("File Readed: ", file)
    f = open(file, 'rb')
    f.seek(0)
    _1 = struct.unpack('<I', f.read(4))[0]
    u = struct.unpack('<I', f.read(4))[0]
    
    print("Singleton: ", _1, ",", u)

    total_posting_lists = 0
    posting_list_geq = 0
    max_id = 0
    while True:
        b = f.read(4)
        if not b:
            break
        n = struct.unpack('<I',b)[0]
        f.seek(4*(n-1), 1)
        last_id = struct.unpack('<I', f.read(4))[0]
        if last_id > max_id:
            max_id = last_id
        if n > 4096:
            posting_list_geq += 1
        total_posting_lists += 1
        size_posting_lists.append(n)
    
    f.close()    
    print("Total posting lists: ", total_posting_lists)
    print("Universe: ", max_id+1)
    return size_posting_lists

def read_terms(f_path):
    f = open(f_path, "r")

    map_terms = {}
    i = 0
    for line in f:
        map_terms[line.strip()] = i
        i+=1
    f.close()
    return map_terms

def read_queries(q_path, out_filename, map_terms, size_posting_lists, min_length):
    f = open(q_path, "r")
    queries = []
    for line in f:
        query = line.strip().split(":")[1]
        terms_of_query = query.split(" ")

        final_query = []
        for t in terms_of_query:
            if t in map_terms.keys():
                if size_posting_lists[map_terms[t]] > min_length:
                    final_query.append(map_terms[t])
        if len(final_query) > 1:
            queries.append(final_query)
    f.close()

    o = open(out_filename, "w")
    for q in queries:
        text_q = ""
        for t in q:
            text_q += (" " + str(t))
        text_q += "\n"
        print(text_q)
        o.write(text_q)
    o.close()

terms_file = "cc-news.terms"
queries_file = "queries/cc-news-spellnorm-ciff-queries.txt"
ii_file = "cc-news.docs"
path = "/media/jpcastillog/Respaldo 1/PISA/CC-News"

terms_file = join(path, terms_file)
queries_file = join(path, queries_file)
ii_file = join(path, ii_file)

size_posting_lists = read_ii(ii_file)
map_terms = read_terms(terms_file)
read_queries(queries_file, join(path,"queries.pisa"), map_terms, size_posting_lists, 4096)


