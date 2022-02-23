
# not binary file
def countInvertedLists(path, min_size):
    f = open(path, 'r')
    
    for line in f:
        data = line.split(' ', maxsplit=2)
        termId  = int(data[0])
        size    = int(data[1])

        n_il = 0
        if size > min_size:
            n_il += 1
            print('Inverted lists > {0} -> {1}'.format(min_size, n_il))
    f.close()
    print(f'Total # inverted lists: {0}'.format(n_il))
    return n_il


ii_path = "../../GOV2/index/ii/absDocIDS/gov2_url_absolute_freqs.ii"
countInvertedLists(ii_path, 4096)