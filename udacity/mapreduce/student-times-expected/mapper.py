from datetime import datetime
import sys
import csv


def mapper():
    data = csv.reader(sys.stdin, delimiter='\t')

    k = data.__next__()
    k_date_added = k.index('added_at')
    k_author_id = k.index('author_id')
    k_len = len(k)

    for line in data:
        if not len(line) == k_len:
            continue
        hour = line[k_date_added][11:13]
        print('{}\t{}'.format(line[k_author_id], hour))

if __name__ == '__main__':
    mapper()
