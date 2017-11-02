from collections import defaultdict

import sys


def reducer():
    dist = defaultdict(int)
    key_old = None

    def f_max(d):
        k = max(dist, key=lambda k: d[k])
        return d[k]

    for line in sys.stdin:
        data = line.split('\t')
        author_id, hour = data[0], int(data[1])

        if not author_id == key_old and key_old is not None:
            mx = f_max(dist)
            for k in {k: v for k, v in dist.items() if v==mx}:
                print('{}\t{}'.format(key_old, k))
            dist = defaultdict(int)

        key_old = author_id
        dist[hour] += 1

    if key_old is not None:
        mx = f_max(dist)
        for k in {k: v for k, v in dist.items() if v==mx}:
            print('{}\t{}'.format(key_old, k))

if __name__ == '__main__':
    reducer()
