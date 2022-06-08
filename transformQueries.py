from os.path import join
from tkinter import N

def transformQueries(file_in, file_out):
    fin = open(file_in, "r")
    fout = open(file_out, "w")
    nQueries = 0
    for line in fin:
        ids = line.strip().split(" ")
        ids = list(map(int, ids))
        str_to_write = ""
        count = 0
        for id in ids:
            if count < len(ids)-1:
                str_to_write += f"{id}\t"
            else:
                str_to_write += f"{id}\n"
            count += 1
        fout.write(str_to_write)
        nQueries += 1 
        if nQueries%1000 == 0:
            print(str_to_write)
            print("Queries processed: ", nQueries)

file = "1mq.txt"
path_in = "D:\\data\\Gov2Flat"
path_out = "E:\\PISA\\Gov2"

path_in = join(path_in, file)
path_out = join(path_out, file)

transformQueries(path_in, path_out)


