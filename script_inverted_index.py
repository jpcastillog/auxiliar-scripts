import random
from os.path import join

def read_inverted_index(path, spaced=2):
    intervals = []
    f = open(path, "r")
    universo = 0
    count = 0
    for line in f:
        if count == 0:
            universo = int(line)
        else:
            s = list(map(int, line.strip().split(' ')))
            n = s[0]
            s = s[1:]
            grouped_s = [[s[spaced*i], s[(spaced*i+spaced)-1]] for i in range(int(n/spaced))]
            intervals += grouped_s
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


read_path = 'example.txt'
save_path = './'

# sizes = [100, 1000, 10000, 100000, 500000, 1000000]
# sizes = [1, 2, 3, 4]
complete = read_inverted_index(read_path, spaced=3)

# for size in sizes:
#     random.seed(5)
#     A = select_n(complete, size)
#     print(A)
#     random.seed(10)
#     B = select_n(complete, size)
#     write_intervals(A, join(save_path, 'invertedIndexA_{}.txt'.format(size)))
#     write_intervals(B, join(save_path, 'invertedIndexB_{}.txt'.format(size)))

print(len(complete))
print(complete[:10])