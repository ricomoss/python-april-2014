April 2, 2014
==============

Introduction
-----------------

We'll introduce Python as a programming language and briefly discuss the history, motivation and nuances.

PEP8
-----------------

The Python community has established standards to be used as a guideline for the way your code should be written.  You can find more information in the official guide, PEP8 (http://www.python.org/dev/peps/pep-0008/).

It mostly boils down to the most ``Pythonic`` way to come to your solution.  That is, if it's easy to read and understand it's correct.  If not, you're probably doing it wrong.

    $> ipython
    Python 3.3.2+
    In [1]: import this
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

Flow and Syntax
-----------------

Python syntax is unique in that it uses white space to determine functionality.  Always set your editor to use 4 spaces instead of tabs.

Programming flow is the basic foundation for logic in programming.  These basic flow paradigms are ``if``, ``else``, ``elif`` (or ``else if``), ``for`` and ``while``.  In Python all flow statements are followed by a colon (``:``).  This is an indication to the interperter (and reader) that relative logic is about to be executed.

Interpreter
-----------------

Python is an interpreted language and uses an interpreter to "compile" the code.  To begin, we'll use the interpreter on your computer to do basic flow logic.  These examples will use iPython (pip install ipython).

    $> ipython
    Python 3.3.2+
    In [1]:

We'll be doing our programming within the interpreter for this class.  We'll talk about scripts next class and see how the interpreter can use scripts to provide a way to write code more efficiently.

If / Else
-----------------

An ``if`` statement is evaluated by the interpreter for it's ``truthiness``.  If the statement evaluates ``true`` the embedded code is executed; otherwise it is skipped.

    In [1]: if True:
       ...:     print('hello world')
       ...:
    hello world

    In [2]: if False:
       ...:     print('hello world')
       ...:

The ``else`` part of the statement will handle the ``false`` condition of the statement.d

    In [1]: if False:
       ...:     print('hello world')
       ...: else:
       ...:     print('goodbye world')
       ...:
    goodbye world

The ``elif`` allows us to compare multiple ``if`` statements under differing conditions for ``truthiness``.

    In [1]: x = 1

    In [2]: y = pow(x, 2)

    In [3]: if x > y:
       ...:     print('{} > {}'.format(x, y))
       ...: elif y > x:
       ...:     print('{} > {}'.format(y, x))
       ...: else:
       ...:     print('{} and {} must be equal!'.format(x, y))
       ...:
    1 and 1 must be equal!

For
-----------------

The ``for`` loop evaluates the objects ``iterator`` and provides elements one-by-one.  These elementes are available within the ``scope`` of the loop for execution.  If the object is a ``list`` or ``tuple`` the ``iterator`` will ``yield`` each element of the list one-by-one starting with the first element in the list.

    In [1]: val = [1, 2, 3]

    In [2]: for i in val:
       ...:     print('{}'.format(i))
       ...:
    1
    2
    3

If the object is a ``dictionary`` the iterator will provide each ``key`` in the dictionary.  Note that ``dictionary`` objects do not perserve order.

    In [1]: val = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

    In [2]: for i in val:
       ....:     print('{}'.format(i))
       ....:
    key2
    key3
    key1

While
-----------------

The ``while`` loop is a combination of the ``if`` and the ``for``.  You provide a statement for the ``while`` to evaulate.  If the statement evaluates with ``truthiness`` the embedded code is executed.

    In [1]: x = 1

    In [2]: while x < 5:
       ....:     print('{}'.format(x))
       ....:     x += 1
       ....:
    1
    2
    3
    4

Exercise 1
-----------------

Print the first 5 odd numbers.

Exercise 2
-----------------

Create a list of the first 5 odd numbers.

Exercise 3
-----------------

Given a string, determine if the string is your first name.

Exercise 4
-----------------

Given a list of positive numbers, determine which number is the largest.

Exercise 5
-----------------

Given a list of strings, create a new list that is in reverse order.

Exercise 6
-----------------

Given a string, create a new string that is in reverse order.

Exercise 7
-----------------

Given a string of length 10, create a new string that is the 3rd through 7th character.

Exercise 8
-----------------

Given 2 lists create a third list that is the concatenation of the two.


Advanced Exercise 1
-----------------

Using Python libraries, solve exercise 4.

Advanced Exercise 2
-----------------

Using Python libraries, solve exercise 7.

Advanced Exercise 3
-----------------

Using Python libraries, solve exercise 5.

Advanced Exercise 4
-----------------

Using Python libraries, solve exercise 6.

Advanced Exercise 5
-----------------

Create a list from each letter of a string.  i.e. 'and' => ['a', 'n', 'd']

Advanced Exercise 6
-----------------

Create a list from each word in a sentence. i.e. 'I like Python.' => ['I', 'like', 'Python.']

Advanced Exercise 7
-----------------

Create a string from the contents of a list.  i.e. ['a', 'n', 'd'] => 'and'
