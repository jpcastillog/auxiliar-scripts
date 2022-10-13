import struct
from os.path import join

def getStats(file):
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
            print("n: ", n)
            print(posting_list_geq)
        total_posting_lists += 1
    
    f.close()    
    print("Total posting lists: ", total_posting_lists)
    print("Universe: ", max_id+1)

file = "cc-news.docs"
# file = "gov2.docs"
# path = "E:\\PISA\\CC-News"
# path = "E:\\PISA\\Gov2"
path = "/media/jpcastillog/Respaldo 1/PISA/CC-News"
file = join(path, file)
getStats(file)

