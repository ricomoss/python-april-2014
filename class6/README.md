April 21, 2014
==============

Review From Class5
-----------------

During the last class we discussed the usage and power of ``args`` and ``kwargs``.  With a working knowledge of ``args`` and ``kwargs`` you are soon ready to learn about class inheritance.

We refactored some code to take advantage of Python ``modules``.  Organization of code is just as important as properly written code.  The more unorganized, sloppy or unreadable your code is the more difficult it is for someone else to understand what you are trying to accomplish.  Often you will find yourself having difficulty understanding your own code several months down the road if you've been negligent.  Be diligent when writing good code - it helps with technical debt.


Raising Exceptions
-----------------

Using exceptions you can control the flow of information through your code.  By defining this flow you're creating an ``API``.  APIs are the backbone of making your code compatible with the outside world.  After all, how userful is your code if other developers can't interface to it?

Python has several built in exceptions as well as the ability to create your own.  In general, you should try to use Python's exceptions rather than building your own.  The more standard your code is the more usable it is to others.

The process of raising exceptions entails deciding what type of data you expect and telling Python how it should error if something bad happens.  You should try and control how your code ``raises`` rather than letting the interpreter error.

    def add_nums(*args):
        tot = 0
        for arg in args:
            tot += arg

    In[1]: print(add_nums(1, 'rico', 2))
    Out[1]: TypeError: unsupported operand type(s) for +=: 'int' and 'str'

This error was raised by the interpreter because ``add_nums`` does not know how to handle strings as inputs.  This is a design decision that needs to be made as to what should happen in the event of an unsupported type.  Let's decide to ignore all types that aren't numbers and add the rest.

    def add_nums(*args):
        tot = 0
        for arg in args:
            if isinstance(arg, (int, float)):
                tot += arg

    In[1]: print(add_nums(1, 'rico', 2))
    Out[1]: 3

We could have also decided to prevent non-number types and raised an exception.  Doing this is more common than ignoring certain types - this is to avoid confusion on behalf of a developer using your function.  If the dev sees a function called ``add_nums`` and notices it accepts strings with no exceptions they might become confused.

    def add_nums(*args):
        tot = 0
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError('add_nums can only add number type objects.')
            tot += arg

    In[1]: print(add_nums(1, 'rico', 2))
    TypeError: add_nums can only add number type objects.

Handling Exceptions
-----------------

In addition to raising exceptions you can also handle them using a ``try-except`` block.  This is similar to ``try-catch`` in other languages.

Suppose we have a function that will divide two numbers.  We'd want to handle the case when someone tried to divide by zero.  In that case, we need the function to return the largest number your system can handle.

    def safe_divide(x, y):
        try:
            val = x / y
        except ZeroDivisionError:
            val = sys.maxsize
        return val

Here we tried to do the division.  If the code raised a ``ZeroDivisionError`` we will do something else.  Using ``try-except`` becomes very useful when you need to handle several cases with your code.

Take note that above we said that the code would raise ``ZeroDivisionError``.  This could be raised anywhere in the code - in Python's built in functions, other Python libraries, third party libraries or your code.

    def foo():
        raise KeyError()

    def bar():
        try:
            foo()
        except KeyError():
            pass

Exercise 1
-----------------

Rewrite the ``Player`` class in ``to_battle`` to use ensure the level parameter is an integer and raise a  ``TypeError`` otherwise.  Verify this with the script.

Exercise 2
-----------------

Expand the detail of the battle report to include information about each round.  (damage done per player per round, each player's current hp per round, etc.)

Exercise 3
-----------------

Create a utility function called ``get_list_item_safely`` that will safely allow invalid indexing of a list or tuple and return ``None`` if the index is out of range.

    In[1]: val = [1, 2]

    In[2]: val[0]
    Out[2]: 1

    In[3]: print(val[2])
    IndexError: list index out of range

Instead should read:

    In[1]: get_list_item_safely(val, 2)
    Out[1]: None


Advanced Exercise 1
-----------------

Create a ``Hero`` class that is a subclass of ``Player`` where the name options are listed below.

    ('Brandon', 'Corban', 'Dal', 'Kris', 'Luke', 'Rico', 'Rob')

Advanced Exercise 2
-----------------

Create a ``Villain`` class that is a subclass of ``Player`` where the name is ``Thanos``.  Set the villains health and attack to be considerably larger than the ``Hero``.
