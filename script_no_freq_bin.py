
from asyncore import write
from hashlib import new


from struct import *
import struct


def noFreqII(path, out_path):
    file = open(path, "r")
    out = open(out_path, "wb")

    out.write(struct.pack('<I', 1))
    out.write(struct.pack('<I', 24622347))
    for l in file:
        data = l.strip().split(" ")
        new_line = []
        i = 0
        for number in data:
            if (i == 1 and (i%2) != 0) or (i != 1  and (i%2) == 0) and i != 0:
                new_line.append(number)
                out.write(struct.pack('<I', int(number)))
            i += 1
        str = (" ".join(new_line)) + "\n"
        # out.write(str.encode())

def normalize_queries(pathII, pathQ, out_path):
    file_ii = open(pathII, "r")
    file_q = open(pathQ, "r") 
    out = open(out_path, "w")
    
    d = {}
    new_id = 0
    for l in file_ii:
        data = l.split(" ", maxsplit= 1)
        id = data[0]
        d[id] = new_id
        new_id += 1

    for l in file_q:
        data = l.strip().split(" ")
        i = d[data[0]]
        j = d[data[1]]
        out.write(f'{i}\t{j}\n')



path = "./ii_random_1000.txt"
out_path = "./ii_random_1000_no_freq.txt"
out_path_q = "./queryLog_1000pairs.txt"
new_out_path_q = "./queryLog_1000pairs_normalize.txt"

noFreqII(path, out_path)
normalize_queries(path, out_path_q, new_out_path_q)