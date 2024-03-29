import sys
import struct
import random

def sampleInvIndex(in_path:str, out_path:str, n:int) -> None:
    if n > 57000:
        return
    samples = random.sample(range(1000, 57001), n)
    with open(in_path, "rb") as inFile,\
          open(out_path, "wb") as outFile:
        
        _1 = struct.unpack('<I', inFile.read(4))[0]
        u = struct.unpack('<I', inFile.read(4))[0]
        
        # Singleton in sub inv index
        outFile.write(struct.pack('<I', 1))
        outFile.write(struct.pack('<I', u))
        
        total_posting_lists = 0
        posting_lists_writed = 0
        id = 0
        while posting_lists_writed < n:
            # print("posting list id: ", id)
            b = inFile.read(4)
            if not b:
                break
            n_ = struct.unpack('<I',b)[0]
            if id in samples:
                outFile.write(b)
                for i in range(n_):
                    outFile.write(inFile.read(4))
                posting_lists_writed+=1
                print(id, "writed")
            else:
                inFile.seek(4*n_, 1)
            total_posting_lists += 1
            id += 1
        print("Posting lists writed: ", posting_lists_writed)
    return 


def rangeSizeInvIndex(in_path:str, out_path:str, min_size:int, max_size:int) -> None:
    
    with open(in_path, "rb") as inFile,\
          open(out_path, "wb") as outFile:
        
        _1 = struct.unpack('<I', inFile.read(4))[0]
        u = struct.unpack('<I', inFile.read(4))[0]
        
        # Singleton in sub inv index
        outFile.write(struct.pack('<I', 1))
        outFile.write(struct.pack('<I', u))
        
        total_posting_lists = 0
        posting_lists_writed = 0

        b = inFile.read(4)
        while b:
            n_ = struct.unpack('<I',b)[0]
            if n_ > min_size and n_ <= max_size:
                outFile.write(b)
                for i in range(n_):
                    outFile.write(inFile.read(4))
                posting_lists_writed+=1
            else:
                inFile.seek(4*n_, 1)
            
            b = inFile.read(4)
            total_posting_lists += 1
            
        print("Posting lists writed: ", posting_lists_writed)
    return 

if __name__ == "__main__":
    n = 20000
    min_size = 4096
    max_size = 15000
    inFile = "/Users/jpcastillo/Documents/InvertedIndexes/CC-News/cc-news_4096.docs"
    # outFile = f"/Users/jpcastillo/Documents/Inverted Indexes/Gov2Flat/gov2sample{n}.bin" 
    outFile = f"/Users/jpcastillo/Documents/InvertedIndexes/CC-News/cc-news_{min_size}-{max_size}.bin"
    # sampleInvIndex(inFile, outFile, n)
    rangeSizeInvIndex(inFile, outFile, min_size, max_size)