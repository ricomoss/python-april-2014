#!/usr/bin/env python


def exercise1():
    amount = 1000000
    new_amount = take_half(amount)
    print(new_amount)


def take_half(amount):
    trax_ticket = 5
    new_amount = amount / 2
    if new_amount > 2 * trax_ticket:
        return take_half(new_amount)
    return new_amount



if __name__ == '__main__':
    exercise1()
