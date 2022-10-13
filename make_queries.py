from os.path import join

def read_terms(f_path):
    f = open(f_path, "r")

    map_terms = {}
    i = 0
    for line in f:
        map_terms[line.strip()] = i
        i+=1
    f.close()
    return map_terms

def read_queries(q_path, out_filename, map_terms):
    f = open(q_path, "r")
    queries = []
    for line in f:
        query = line.strip().split(":")[1]
        terms_of_query = query.split(" ")
        # print(terms_of_query)

        final_query = []
        for t in terms_of_query:
            if t in map_terms.keys():
                final_query.append(map_terms[t])
        if len(final_query) > 0:
            # print(final_query)
            queries.append(final_query)
    f.close()

    o = open(out_filename, "w")
    for q in queries:
        text_q = ""
        for t in q:
            text_q += (" " + str(t))
        print(text_q)
        o.write(text_q)
    o.close()

terms_file = "cc-news.terms"
queries_file = "queries/cc-news-spellnorm-ciff-queries.txt"
path = "/media/jpcastillog/Respaldo 1/PISA/CC-News"

terms_file = join(path, terms_file)
queries_file = join(path, queries_file)
map_terms = read_terms(terms_file)

read_queries(queries_file, join(path,"queries.pisa"), map_terms)


