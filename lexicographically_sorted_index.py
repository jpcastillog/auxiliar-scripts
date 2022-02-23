from struct import *
import struct


def lexicographically_sorted_index(urls_path, index_path, out_file):
    f = open(urls_path, "r")
    print("Reading URLS")
    urls = []
    count = 0
    for line in f:
        if count != 0:
            docid, id, site, suffix, url = line.strip().split(" ")
            id = int(id) - 1
            urls.append((id, url))
        count+=1

    print("Sorting URLS")
    urls.sort(key= lambda x: x[1])
    f.close()
    print("Mapppig new ids")
    map_index = {}
    for i in range(len(urls)):
        id, url = urls[i]
        map_index[id] = i

    fi = open(index_path, "rb")
    out = open(out_file, "wb")
    
    _1  = struct.unpack('<I', fi.read(4))[0]
    u   = struct.unpack('<I', fi.read(4))[0]
    print(_1, u)

    out.write(struct.pack('<I', _1))
    out.write(struct.pack('<I', u))
    print("Writing index sorted lexicagraphically")
    while True:
        b = fi.read(4)
        if b == "":
            break
        n = struct.unpack('<I', b)[0]
        # if n >= 4096:
        il = list()
        out.write(struct.pack('<I', n))
        for j in range(n):
            id = struct.unpack('<I', fi.read(4))[0]
            new_id = map_index[id]
            il.append(new_id)
        
        il.sort()
        for new_id in il:
            out.write(struct.pack('<I', new_id))
        # else:
        #     fi.seek(4*n, 1) #skip n ints of 4 bytes


    fi.close()
    out.close()
    print("Fin")


urls_path   = "D:\\data\\CC-News\\cc-news-urls.txt"
index_path  = "D:\\data\\CC-News\\cc-news-en.pisa.docs"
out_path    = "D:\\data\\CC-News\\cc-news-en-url-sorted.docs"

lexicographically_sorted_index(urls_path, index_path, out_path)