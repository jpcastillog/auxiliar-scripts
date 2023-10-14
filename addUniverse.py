import sys
import struct

def addUniverse(in_path, out_path, u):
    with open(in_path, "rb") as inFile, open(out_path, "wb") as outFile:
        # Write a sigleton (1, u)
        print(f"Writing the universe u: {u}")
        outFile.write(struct.pack('<I', 1))
        outFile.write(struct.pack('<I', u))
        print("Writing the rest of inverted index...")
        while True:
            nb = inFile.read(4)
            if not nb:
                break
            n  = struct.unpack('<I', nb)[0]
            invList = inFile.read(n*4)
            outFile.write(nb)
            outFile.write(invList)
    print("All inverted index writed")
            

if __name__ == "__main__":
    u = int(sys.argv[1])
    inPath = sys.argv[2]
    outPath = sys.argv[3]
    addUniverse(inPath, outPath, u)
