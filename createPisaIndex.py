import struct
from os.path import join

def createPisaFormat(inv_lists_file, collection_name, min_size):
    # Input files
    f = open(inv_lists_file, 'rb')
    # Out collection
    fdocs  = open(collection_name + '.docs', 'wb')
    ffreqs = open(collection_name + '.freqs', 'wb')
    fsizes = open(collection_name + '.sizes', 'wb')

    _1 = struct.unpack('<I', f.read(4))[0]
    u  = struct.unpack('<I', f.read(4))[0]
    
    total_documents = 0
    while True:
        b = f.read(4)
        if not b:
            break
        n = struct.unpack('<I', b)[0]
        if n > min_size:
            total_documents += 1
        f.seek(4*n, 1)

    print("Number of documents ", total_documents)
    # move cursor to begin
    f.seek(0, 0)
    _1 = struct.unpack('<I', f.read(4))[0]
    u  = struct.unpack('<I', f.read(4))[0]

    fdocs.write(struct.pack('<I', 1))
    fdocs.write(struct.pack('<I', total_documents))
    documents = []
    il = 0
    while True:
        b = f.read(4)
        if not b:
            break
        n = struct.unpack('<I', b)[0]
        if n > min_size:
            ffreqs.write(struct.pack('<I', n))
            fdocs.write(struct.pack('<I', n))
            fsizes.write(struct.pack('<I', n))
            for i in range(n):
                id = f.read(4)
                ffreqs.write(id)
                ffreqs.write(struct.pack('<I', 1))  # Add 1 to freq for all term ids
                fdocs.write(id)
            il+=1
            if il%1000 == 0:
                print(il, "inv lists readed")
        else:
            f.seek(4*n, 1)
    fdocs.close()
    ffreqs.close()
    fsizes.close()
    print("Pisa collection created Succefully")

input_filename = "D:\\data\\Gov2Flat\\gov2.sorted"
folder_to_save = "D:\\data\\PISA\\Gov2" 
colletion_filename = "gov2_4096"
colletion_filename = join(folder_to_save, colletion_filename)
createPisaFormat(input_filename, colletion_filename, 4096)

