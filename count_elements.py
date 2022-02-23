
# not binary file
def countInvertedLists(path, min_size):
    f = open(path, 'r')
    n_il       = 0 
    total_size = 0
    for line in f:
        data = line.split(' ', maxsplit=2)
        termId  = int(data[0])
        size    = int(data[1])

        if size > min_size:
            # print('Inverted lists > ', min_size,  '-> ', n_il)
            n_il += 1
            total_size += size
    f.close()
    print('-----------------------------------------------')
    print('Total # inverted lists: ', n_il)
    print('Total # ints: ', total_size)
    return n_il


ii_path = "../../GOV2/index/ii/absDocIDS/gov2_url_absolute_freqs.ii"
countInvertedLists(ii_path, 4096)