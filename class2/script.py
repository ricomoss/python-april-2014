#!/usr/bin/env python

# Comments can be created using the '#' character at the beginning of a line
# Single line comments are the most commonly used and preferred method of
# commenting.  If you're comment needs more than a single line to explain you
# should consider refactoring your code to make it more readable and easier
# to understand.

"""
  Triple double quotes (") can also be used to generate blocks of comments.
  This is also used by Python's built-in documentation generator.  We'll talk
  more about this at another time.

  Notice I am able to type single and double quote characters without special
  considerations while within the triple quote comment block.

  Also notice I am not writing any lines to be longer than 79 characters.  This
  is because the PEP8 standard requires all lines be less than 79 characters.
  There are a handful of reasons to break this rule.  Remember to always follow
  PEP8 when writing Python code.
"""
# Use import statements to access Python libraries.  Not to be confused with
# built in functions!
import random
import itertools


# PEP 8 Standard:  Always separate each function or class at the file-level
# with 2 spaces.
def exercise1():
    person_info = {
        'first_name': 'Rico',
        'last_name': 'Cordova',
        'email': 'rico.cordova@rocksolidbox.com',
        'favorite_language': 'Python'
    }
    return [(key, val) for key, val in person_info.items()]


def exercise2():
    my_list = [
        ('first_name', 'Rico'), ('last_name', 'Cordova'),
        ('email', 'rico.cordova@rocksolidbox.com'),
        ('favorite_language', 'Python')
    ]
    return dict(my_list)


def exercise3():
    person_info = {
        'first_name': 'Rico',
        'last_name': 'Cordova',
        'email': 'rico.cordova@rocksolidbox.com',
        'favorite_language': 'Python'
    }
    return 'Hello, {} {}, it is nice to see you.'.format(
        person_info['first_name'], person_info['last_name'])


def exercise4():
    names = ['rico', 'dal', 'corban', 'brandon', 'kris', 'rob', 'luke']
    player1 = random.choice(names)
    player2 = player1
    while player2 == player1:
        player2 = random.choice(names)
    return player1, player2


def exercise5():
    p1, p2 = exercise4()
    num_of_rounds = 3
    dmg_summary = {
        'p1_dmg_done': 0,
        'p2_dmg_done': 0,
    }
    for _ in itertools.repeat(None, num_of_rounds):
        dmg_summary['p1_dmg_done'] += random.gauss(1, 100)
        dmg_summary['p2_dmg_done'] += random.gauss(1, 100)

    dmg_diff = abs(dmg_summary['p1_dmg_done'] - dmg_summary['p2_dmg_done'])
    msg = '{} is victorious over {} by dealing {:.0f} more damage.'
    if dmg_summary['p1_dmg_done'] > dmg_summary['p2_dmg_done']:
        msg = msg.format(p1, p2, dmg_diff)
    elif dmg_summary['p2_dmg_done'] > dmg_summary['p1_dmg_done']:
        msg = msg.format(p2, p1, dmg_diff)
    else:
        msg = "It's a tie!  They both did {:.0f} damage.".format(
            dmg_summary['p1_dmg_done'])
    return msg


def exercise6():
    team1 = list(exercise4())
    p1, p2 = exercise4()
    while (p1 in team1) or (p2 in team1):
        p1, p2 = exercise4()
    team2 = [p1, p2]

    num_of_rounds = 3
    dmg_summary = {
        'team1_dmg_done': 0,
        'team2_dmg_done': 0,
    }
    for _ in itertools.repeat(None, num_of_rounds):
        dmg_summary['team1_dmg_done'] += random.gauss(1, 100) + \
            random.gauss(1, 100)
        dmg_summary['team2_dmg_done'] += random.gauss(1, 100) + \
            random.gauss(1, 100)

    dmg_diff = abs(
        dmg_summary['team1_dmg_done'] - dmg_summary['team2_dmg_done'])
    msg = '{} and {} are victorious over {} and {} by dealing {:.0f} more ' \
          'damage.'
    if dmg_summary['team1_dmg_done'] > dmg_summary['team2_dmg_done']:
        msg = msg.format(team1[0], team1[1], team2[0], team2[1], dmg_diff)
    elif dmg_summary['team2_dmg_done'] > dmg_summary['team1_dmg_done']:
        msg = msg.format(team2[0], team2[1], team1[0], team1[1], dmg_diff)
    else:
        msg = "It's a tie!  They both did {:.0f} damage.".format(
            dmg_summary['team1_dmg_done'])
    return msg


if __name__ == '__main__':
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    exercise5()
    exercise6()
