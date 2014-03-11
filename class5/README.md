April 16, 2014
==============

Review From Class4
-----------------

During the last class we introduced classes and the concept of Introspection.  Objects are the fundamental building blocks in Python and an object is an instantiated class.  Upon instantiation, Python calls the ``__init__()`` ``method``.  It is during instantiation you should initialize ``self``.

Introspection provides you with the ability to observe the state of objects during run time.  This is powerful because you can decide how to execute the code depending on what kind of object you are dealing with.

The advanced exercise required the use of Python ``modules`` in order to import the ``utils.py`` file.  To correctly import the file we needed to tell Python where it should look for the ``module``.  This was done by adding to the ``PYTHONPATH`` environment variable.

``*args`` / ``**kwargs``
-----------------

Python allows you to define methods to accept ``*args`` and ``**kwargs`` parameters.  The ``*args`` are a ``list`` or ``tuple`` of ordered parameters.  You would use ``*args`` if you don't know how many parameters your function might take.

    def sum_nums(*args):
        total = 0
        for num in args:
            total += num
        return total

    total = sum_nums(1, 2, 3, 10, 14)

Or you call a function using the ``*`` notation with a ``list`` or ``tuple``.

    my_list = [1, 2, 3, 10, 14]
    total = sum_nums(*my_list)

Similarly, you can use ``kwargs`` (keyword args) to pass a dictionary of named values.  When using ``kwargs`` order does not matter.

    def print_stuff(**kwargs):
        for key, value in kwargs.items():
            print('{}: {}'.format(key, value))

    print_stuff(key1='value1', key2='value2')
    key1: value1
    key2: value2

Or you call a function using the ``**`` notation with a ``dict``.

    my_dict = {'key1': 'value1', 'key2': 'value2'}
    print_stuff(**my_dict)
    key1: value1
    key2: value2

You can use a combination of normal parameters, ``*args`` and ``**kwargs`` but be careful because order matters!  If you choose to use a combination you'll need to specify normal parameters first, ``*args`` next, explicit keyword arguments next and ``**kwargs`` last.

    def do_stuff(name, *args, your_name=None, **kwargs):
        print(name)
        for arg in args:
            print(arg)
        print('your_name: {}'.format(your_name))
        for key, value in kwargs:
            print('{}: {}'.format(key, value))

    do_stuff('rico')
    rico
    your_name: None

    do_stuff('rico', 1, 2)
    rico
    1
    2
    your_name: None

    do_stuff('rico', *(1, 2))
    rico
    1
    2
    your_name: None

    do_stuff(*('rico', 1, 2))
    rico
    1
    2
    your_name: None

    do_stuff(*('rico', 1, 2), your_name='bro')
    rico
    1
    2
    your_name: bro

    do_stuff(*('rico', 1, 2), your_name='bro', key1='val1', key2='val2')
    rico
    1
    2
    your_name: bro
    key1: val1
    key2: val2

    do_stuff(*('rico', 1, 2), your_name='bro', **{'key1': 'val1', 'key2': 'val2'})
    rico
    1
    2
    your_name: bro
    key1: val1
    key2: val2

    do_stuff(*('rico', 1, 2), **{'your_name': 'bro', 'key1': 'val1', 'key2': 'val2'})

Remember that order matters.  If you put ``kwargs`` before ``args`` there will be problems.

    do_stuff('rico', your_name='bro', 1, 2)
    SyntaxError: non-keyword arg after keyword arg

Using ``args`` and ``kwargs`` can let you do some powerful things.  You can use ``kwargs`` to provide default values.  In the example above the ``your_name`` parameter had a default value of ``None``.  Default parameters cause ``kwargs`` so be sure to supply default parameters after your normal list of ``args``.

Exceptions
-----------------

In class 4 Advanced Exercise 1 ``Battle()`` used exceptions to ensure the ``p1`` and ``p2`` objects were ``Player`` instantiations.  It is common to ``raise`` exceptions in this manner to ensure proper use of your code.  Congratulations, you've written your first API!  You can see a list of all built in exceptions within Python in the docs (http://docs.python.org/3.3/library/exceptions.html).

We'll discuss exception handling in further detail later in the course.


Modules
-----------------

Modules are a way of Python to organize files so that code within one file can be made accessible to another file.  This is very important because you don't want to build your entire project in a single file.  Just as you should always keep your code in small logical chunks so should you also keep your files as small logical chunks.  Put utility functions in a utils.py file, put models in a models.py file, etc.

You must be sure to add your module to the system's ``PYTHONPATH``.  The ``PYTHONPATH`` is an environment variable that tells Python where to look when you declare files.  This can be to execute files or to import code from another file.

You can imagine it might get tedious always trying to keep track of your ``PYTHONPATH``.  To fix that problem it's very useful to use virtual environments.  Virtual environments provide you the ability to install Python libraries, modify your interpreter, modify *any* environment variable...all without effecting your base system or any other virtual environment.

For example, suppose you have a project you are building using Python 3 and another Python library, say, psycopg2.  The psycopg2 library allows for you to interface with a PostgreSQL database.  You'll need to do some basic setup of environment variables to get this all working correctly.

Suppose you have other projects that use Python 2 and MySQL.  If you start fiddling with the environment variables or installing other libraries you may effect your other projects.  If you ensure you always use virtual environments you won't have this problem.


Exercise 1
-----------------

Rewrite the ``Human`` class from class 4 exercise 1 to use ``kwargs`` with default value for name of ``None`` and default value for level of ``1``.  Add a method that sets the ``health`` attribute to be 500 * level^2.

Exercise 2
-----------------

Create a new module called to_battle.  Create 3 files in the module - player.py, battle.py and utils.py.  Place the ``Player()`` class from class 5 exercise 1 in the player.py file, the ``Battle()`` class in the battle.py file and the ``pretty_print()`` function in the utils.py file.  Go through and use imports throughout.  Write a script to verify functionality.

Advanced Exercise 1
-----------------

Refactor ``Player()`` to create attributes for all extra ``kwargs`` passed.

Refactor ``Battle()`` to create attributes for all extra ``kwargs`` passed and add those attributes to the report.
