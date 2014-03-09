#!/usr/bin/env python


def get_highest_test_score(test_scores):
    highest_score = 0
    name = None
    for key, val in test_scores.items():
        if val > highest_score:
            highest_score = val
            name = key
    return name, highest_score


def exercise1():
    test_scores = {
        'james': 75,
        'karen': 78,
        'albert': 92,
        'kim': 66,
        'susan': 90,
        'rick': 88,
    }
    name, score = get_highest_test_score(test_scores)
    print('{} scored {}'.format(name, score))


def get_avg_test_info(test_scores):
    scores_tot = 0
    for val in test_scores.values():
        scores_tot += val
    avg = scores_tot / len(test_scores)

    names = list()
    for key, val in test_scores.items():
        if val > avg:
            names.append(key)
    return avg, names


def exercise2():
    test_scores = {
        'james': 75,
        'karen': 78,
        'albert': 92,
        'kim': 66,
        'susan': 90,
        'rick': 88,
    }
    avg, names = get_avg_test_info(test_scores)
    print('The average score was {} and the following people scored '
          'above average:'.format(avg))
    for name in names:
        print('\t{}'.format(name))


def get_fib_list(num):
    fib_list = list()
    for index in range(1, num + 1):
        fib_list.append(get_fib_num(index))
    return fib_list


def get_fib_num(n):
    if n < 1:
        raise IndexError('A sequence must have a positive integer index.')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return get_fib_num(n - 1) + get_fib_num(n - 2)


def exercise3():
    fib_list = get_fib_list(15)
    print(fib_list)


def exercise4():
    my_dict = dict()
    for index in range(1, 35):
        my_dict[index] = get_fib_list(index)
    pretty_print(my_dict)


# Advanced Exercise 1
def pretty_print(obj, indents=0):
    if isinstance(obj, (list, tuple)):
        for item in obj:
            return pretty_print(item)
    elif isinstance(obj, dict):
        if indents == 0:
            print('{')
        for key, val in obj.items():
            if isinstance(val, dict):
                print('{}{}: {{'.format(' ' * 4 * (indents + 1), key))
                pretty_print(val, indents + 1)
            else:
                print('{}{}: {}'.format(' ' * 4 * (indents + 1), key, val))
        closing = '{}}},'
        if indents == 0:
            closing = '{}}}'
        print(closing.format(' ' * 4 * indents))


if __name__ == '__main__':
    exercise1()
    exercise2()
    exercise3()
    exercise4()
