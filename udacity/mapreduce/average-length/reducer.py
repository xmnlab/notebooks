from collections import defaultdict

import sys


def reducer():
    question_length = 0
    answer_length = []
    key_old = None

    def f_avg(v):
        count = len(v)
        return sum(v)/count if count > 0 else 0

    for line in sys.stdin:
        data = line.split('\t')
        question_id, node_type, length = data[0], data[1], int(data[2])

        if not question_id == key_old and key_old is not None:
            print(
                '{}\t{}\t{}'.format(
                    key_old, question_length, f_avg(answer_length)
            ))
            question_length = 0
            answer_length = []
            key_old = None


        key_old = question_id

        if node_type == 'question':
            question_length = length
        else:
            answer_length.append(length)

    if key_old is not None:
        print(
            '{}\t{}\t{}'.format(
                key_old, question_length, f_avg(answer_length)
        ))


if __name__ == '__main__':
    reducer()
