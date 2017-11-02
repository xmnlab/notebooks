from datetime import datetime
import sys
import csv


def mapper():
    data = csv.reader(sys.stdin, delimiter='\t')

    k = data.__next__()

    k_id = k.index('id')
    k_author_id = k.index('author_id')
    k_node_type = k.index('node_type')
    k_abs_parent_id = k.index('abs_parent_id')

    k_len = len(k)

    for line in data:
        if not len(line) == k_len:
            continue

        thread_id = (
            line[k_id] if line[k_node_type] == 'question' else
            line[k_abs_parent_id]
        )
        print('{}\t{}'.format(thread_id, line[k_author_id]))

if __name__ == '__main__':
    mapper()
