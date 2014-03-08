April 9, 2014
==============

Review From Class2
-----------------

During the last class we introduced the concept of list comprehension - the ability to create lists based on iterated information with a single statement.  This is the most efficient way to create lists.

We've also made heavy use of the string method ``format()``.  This is a powerful tool used to format strings for readability.  Other languages use ``printf()`` style formatting, and that is available in Python but is no longer standard as of Python 3.  Never, ever use ``printf()`` style formatting.  Always opt for ``format()``.

Dictionaries were very useful in solving the advanced exercises.  Remember the key and value of a dictionary can be arbitrary Python objects.  This makes their potential use limitless.

    In[1]: my_dict = {
        'uniform': random.uniform,
        'gauss': random.gauss,
        'choice': random.choice,
    }

    In[2]: my_dict['choice']([1, 2])
    Out[2]: 1


Functions
-----------------

One of the core building blocks in Python are functions.  Functions allow you to modularize your logic.  If you have logic you are using repeatedly it's best to put that logic in a function and call the function multiple times rather than repeating yourself.  Python advocates the DRY principle (Don't Repeat Yourself).

Functions in Python are declared and defined at the same time.  If you have experience in other programming languages you may have seen a different paradigm.  Take C++ for example, you can declare a function prior to it's definition.  That is not necessary in Python.  The interpreter knows to look within the namespace for your definition.

Functions take parameters and those parameters are used within the function scope to execute code.  Once the function has completed execution the information held within that scope is lost.  You can define functions with the Python keyword ``def``.

    def foo(bar, baz):
        # Do something

In the above example ``foo`` is the function, ``bar`` is the first required parameter and ``baz`` is the second required parameter.  The naming convention advocated by PEP8 has function, method and variable names be ``lower_undersore``.  So, we wouldn't name our funciton ``Foo``.

To make use of a function you can simply call to the function with the required parameters within the same namespace.

    if one_thing > the_other:
        foo(one_thing, the_other)
    else:
        foo(the_other, one_thing)


Python and Recursion
-----------------

Recursion is the principle of repeating a process on itself repeatedly.  Python, by default, allows 1000 levels of recursion (this can be adjusted manually if needed).  Let's look at a recursive example.

Suppose I have a $1M and I want to give half of it away.  Then, I want to give half of the remaining away.  Then, I want to give half of the remaning away...you get the idea.  Suppose I want to have enough to buy a Trax pass when I'm done.  How much would I give away each time?  This can be solved very easily with recursion.

    def take_half(amount):
        trax_ticket = 5
        new_amount = amount / 2
        if new_amount > 2 * trax_ticket:
            return take_half(new_amount)
        return new_amount


Exercise 1
-----------------

Given a dictionary of test scores, create a function that will print the name of the person who had the highest score and their score.

    {
        'james': 75,
        'karen': 78,
        'albert': 92,
        'kim': 66,
        'susan': 90,
        'rick': 88,
    }

Exercise 2
-----------------

Using the same dictionary of test scores, create a function that will print the average test score and everyone who scored above average.

Exercise 3
-----------------

Create a function to return a list of the first ``n`` values of the Fibonacci sequence.

i.e.
    n = 1 => [0]
    n = 2 => [0, 1]
    n = 3 => [0, 1, 1]
    n = 4 => [0, 1, 1, 2]
    .
    .
    .

Exercise 4
-----------------

Create a dictionary for each set of ``n`` values of the Fibonacci sequence for all n < 35.

    {
        1: [0],
        2: [0, 1],
        3: [0, 1, 1],
        .
        .
        .
    }

Advanced Exercise 1
-----------------

Create a function that will take a dictionary and print the contents of the dictionary to STDOUT in "pretty print".  Use Python's PEP8 as a guide for style.  That is, use 4 spaces to indent each embedded level.

i.e.

    {
        'key1': {
            'subkey1': [1, 2, 3],
            'subkey2': 'foo',
            'subkey3': 'bar',
        },
        'key2': {
            'subkey1': {
                'subsubkey1': 'foo',
                'subsubkey2': 'bar',
            },
            'subkey2': [1, 2],
            'subkey3': (3, 4),
            'subkey4': 'foo',
        },
        .
        .
        .
    }
