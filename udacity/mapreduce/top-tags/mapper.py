from datetime import datetime
import sys
import csv


def mapper():
    data = csv.reader(sys.stdin, delimiter='\t')

    k = data.__next__()

    k_tagnames = k.index('tagnames')
    k_node_type = k.index('node_type')

    k_len = len(k)

    for line in data:
        if not len(line) == k_len:
            continue

        if not line[k_node_type] == 'question':
            continue
        
        for tagname in line[k_tagnames].split(' '):
            print('{}\t1'.format(tagname))

if __name__ == '__main__':
    mapper()
