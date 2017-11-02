from collections import defaultdict

import sys


def reducer():
    counter = 0
    key_old = None

    top10 = []

    for line in sys.stdin:
        tagname, _ = line.split('\t')

        if not tagname == key_old and key_old is not None:
            top10.append((key_old, counter))
            top10 = sorted(top10, reverse=True, key=lambda v: v[1])[:10]
            counter = 0

        key_old = tagname
        counter += 1


    if key_old is not None:
        top10.append((key_old, counter))
        top10 = sorted(top10, reverse=True, key=lambda v: v[1])[:10]

        for tag, counter in top10:
            print('{}\t{}'.format(tag, counter))


if __name__ == '__main__':
    reducer()
