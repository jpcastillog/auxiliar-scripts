from audioop import add
from distutils.fancy_getopt import OptionDummy
from importlib.resources import path
from os import remove
import struct
from struct import *

def addUniverse(u, file):
    f = open(file, 'rb+')
    previous_content = f.read()
    f.seek(0, 0)
    print('Writing Universe u: ', u)
    f.write(struct.pack('<I', 1))
    f.write(struct.pack('<I', u))
    print('Writing rest of inverted index')
    f.write(previous_content)
    f.close()
    print('FIN !!!!')

def removeElementsQueries(min_id, queries_file, out_file):
    f = open(file, 'r')
    filtered_queries = []
    nq = 0 
    for line in f:
        elements = line.strip().split(' ')
        elements = list(map(int, elements))
        flag = True
        for e in elements:
            if e > min_id:
                flag = False
                break
        if flag:
            filtered_queries.append(elements)
        nq += 1
    f.close()
    print(f'Total queries readed: {nq}')
    print(f'Writing {len(filtered_queries)} filtered queries!')
    fo = open(out_file, 'w')
    for q in filtered_queries:
        str_q = ' '.join(str(x) for x in q)
        fo.write(str_q)
    fo.close()





# path = 'D:/data/Gov2Flat/gov2.unsorted'
# path = 'D:/data/ClueWeb09Flat/clueweb09.sorted'
in_path = 'D:/Data/Gov2Flat/1mq.txt'
out_path = 'D:/Data/Gov2Flat/1mq_filtered.txt'
u = 50131015
# addUniverse(u, path)
removeElementsQueries(57224, in_path, out_path)
