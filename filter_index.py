from audioop import add
from importlib.resources import path
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

# path = 'D:/data/Gov2Flat/gov2.unsorted'
path = 'D:/data/ClueWeb09Flat/clueweb09.sorted'
u = 50131015
addUniverse(u, path)