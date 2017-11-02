from datetime import datetime
import sys
import csv


def mapper():
    data = csv.reader(sys.stdin, delimiter='\t')

    k = data.__next__()

    k_id = k.index('id')
    k_node_type = k.index('node_type')
    k_abs_parent_id = k.index('abs_parent_id')
    k_body = k.index('body')

    k_len = len(k)

    for line in data:
        if not len(line) == k_len:
            continue
        _id = (
            line[k_id] if line[k_node_type] == 'question' else
            line[k_abs_parent_id]
        )

        print('{}\t{}\t{}'.format(_id, line[k_node_type], len(line[k_body])))

if __name__ == '__main__':
    mapper()
