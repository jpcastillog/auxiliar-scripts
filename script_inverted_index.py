import random
from os.path import join

def read_inverted_index_spaced(path, spaced=2, max_lines=100):
    intervals = []
    f = open(path, "r")
    universo = 0
    count = 0
    for line in f:
        if count == 0:
            universo = int(line)
        elif count >= max_lines:
            break
    
        else:
            s = list(map(int, line.strip().split(' ')))
            n = s[0]
            s = s[1:]
            grouped_s = [[s[spaced*i], s[(spaced*i+spaced)-1]] for i in range(int(n/spaced))]
            intervals += grouped_s
        print(count)
        count += 1
    f.close()
    return intervals

def read_inverted_index(path, max_lines=100):
    intervals = []
    f = open(path, "r")
    universo = 0
    count = 0
    for line in f:
        if count == 0:
            universo = int(line)
        elif count >= max_lines:
            break
            
        else:
            s = list(map(int, line.strip().split(' ')))
            n = s[0]
            s = s[1:]

            start = s[0]
            previous = s[0]
            for i in range(1, len(s)):
                if previous + 1 != s[i]:
                    intervals.append([start, previous+1])
                    start = s[i]
                    previous = s[i]
                else:
                    previous = s[i]
            intervals.append([start, s[n-1]+1])
        print("line: ", count)
        count += 1
    f.close()
    return intervals


def write_intervals(intervals, path):
    f = open(path, "w")
    for i in intervals:
        f.write("{0} {1}\n".format(i[0], i[1]))
    f.close()


def select_n (intervals, n):
    if n > len(intervals):
        print("n > size of set")
    return random.sample(intervals, n)


read_path = './../../../data/bitvectors/ii/gov2/url/gov2_ii_nofreq_url_dif.txt.B'
save_path = './../../../data/intervals/invertedIndex'

# sizes = [100, 1000, 10000, 100000, 500000, 1000000]
sizes = [10000000]
# sizes = [1, 2, 3, 4]
# spaced = 100
# complete = read_inverted_index_spaced(read_path, spaced=spaced, max_lines=1000)
complete = read_inverted_index(read_path, max_lines=1000)

for size in sizes:
    random.seed(5)
    A = select_n(complete, size)
    # print("A: ", A[:10])
    random.seed(10)
    B = select_n(complete, size)
    # print("B: ", B[:10])
    write_intervals(A, join(save_path, 'invertedIndexADefault_{}.txt'.format(size)))
    write_intervals(B, join(save_path, 'invertedIndexBDefault_{}.txt'.format(size)))
    print("Creados los archivos para {}".format(size))

print("Fin del Script!!!\n")
# print(len(complete))
# print(complete[400:410])