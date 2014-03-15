
def get_fib_num(n):
    if n < 1:
        raise IndexError('A sequence must have a positive integer index.')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return get_fib_num(n - 1) + get_fib_num(n - 2)
