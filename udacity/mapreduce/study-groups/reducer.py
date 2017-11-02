from collections import defaultdict

import sys


def reducer():
    counter = 0
    key_old = None

    authors_id = []

    for line in sys.stdin:
        thread_id, author_id = line.split('\t')

        if not thread_id == key_old and key_old is not None:
            print('{}\t{}'.format(key_old, str(authors_id)))
            authors_id = []

        key_old = thread_id
        authors_id.append(author_id.replace('\n', ''))


    if key_old is not None:
        print('{}\t{}'.format(key_old, str(authors_id)))


if __name__ == '__main__':
    reducer()
