import struct

def createPisaFormat(inv_lists_file, collection_name):
    # Input files
    f = open(inv_lists_file, 'rb')
    # Out collection
    fdocs  = open(collection_name + '.docs', 'w')
    ffreqs = open(collection_name + '.freqs', 'w')
    fsizes = open(collection_name + '.sizes', 'w')

    _1 = struct.unpack('<I', f.read(4))
    u  = struct.unpack('<I', f.read(4))
    
    total_documents = 0
    while True:
        b = f.read(4)
        if b == '':
            break
        n = struct.unpack('<I', b)[0]
        total_documents += 1
        f.seek(4*n, 1)
    
    # move cursor to begin
    f.seek(0, 0)
    
    fdocs.write(struct.pack('<I', 1))
    fdocs.write(struct.pack('<I', total_documents))
    documents = []
    while True:
        b = f.read(4)
        if b == "":
            break
        n = struct.unpack('<I', b)[0]
        ffreqs.write(struct.pack('<I', n))
        fdocs.write(struct.pack('<I', n))
        fsizes.write(struct.pack('<I', n))
        for i in range(n):
            id = f.read(4)
            ffreqs.write(id)
            ffreqs.write(struct.pack('<I', 1))
            fdocs.write(id)
    fdocs.close()
    ffreqs.close()
    fsizes.close()

