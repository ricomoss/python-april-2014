April 7, 2014
==============

Scripts
-----------------

A script is a program written to automate the execution of tasks.  Python is popular as a scripting language.  The advantage of a scripting language is the speed at which development is possible.  Scripting languages uses interpreters to "compile" the code at run-time.

Writing a script in Python is a simple task.  Simply create a file, place your code in the file and call the Python interpreter with the file as the argument.

    $> python script.py

You can see which interpreter is being used by your system by ``which``.  This is a shell command telling what command is ``aliased``.

    $> which python
    /home/ricomoss/.virtualenvs/class-apr-2014/bin/python

Your interpreter may be different - in fact, it most likely is as the interpreter above is within a virtual environment.  You're probably seeing something like this.

    $> which python
    /usr/bin/python

Or, you may see the following if your interpreter is set for Python 3.

    $> which python
    /usr/bin/python3

Your system stores the interpreter set for your environment within an environment variable.  You can always get to the appropriate Python interpreter though the environment.

    $> /usr/bin/env python

If you set your script to be executable then you can rely on the environment to use the appropriate Python interpreter.

    $> chmod +x script.py

The above command makes the script executable by every user.  Be careful modifying the permissions of files as you may accidentally grant more access than you intended.  For the purposes of these examples the file may be executable by all without any worries - we're not doing anything critical here.

Now, within the script file simply put the ``shebang`` as the first line and you're on your way.  The ``shebang`` is label telling the environment (shell, OS, browser, etc) which interpreter should be used for the file.

    #!/user/bin/env python

Or, for Python 3.

    #!/usr/bin/env python3

Now you can run the script by simply executing the file.

    $> ./script.py

First Things First
-----------------

In programming there are namespaces.  Python is a language that embraces namespaces and you should too.  When running a script the namespace of the file is ``'__main__'``.  So, you should always wrap your script in the ``'__main__'`` functionality otherwise information within your script can get accidentally executed by other code that wasn't implemented correctly.  It's just a safe guard and you should always do it.

    if __name__ == '__main__':
        # Do your stuff here


Review From Class1
-----------------

There were a few concepts introduced in the first class that we'll review shortly before we expand.  If you took the time to do the advanced exercises you may have run into some concepts we didn't discuss.  Let's do that now.

9. We used a Python ``max()`` built-in function.  Python has dozens of built-in functions and you are encouraged to use them whenever you can.  Without going into too much detail let's just say the Python team has optimized these built-in functions to be very efficient (much more efficient than your code would be).  In the case of finding the max value with ``for`` or ``while`` loops you'll be magnitudes of order slower than using Python's ``max()`` built-in function.  You can find more information about Python's built-in functions on the official `Python website <http://docs.python.org/3.3/library/functions.html>`_

10. We spliced the list using the following syntax.

    In[1]: my_obj[start:end]

Which is equivalent to the following (for lists).

    new_obj = list()
    for index in range(start, end):
        new_obj.append(my_obj[index])

11. To take the above concept even further we'll add to it ``step``.

    In[1]: name[::-1]

If ``start`` and ``end`` are left blank it will start at the beginning and finish at the end.  The ``step`` is the final value which determines how we'll "step" through the list.  In this case, with ``-1``, we're stepping backward one at a time.

13. This is called list comprehension and we'll discuss this in detail later in this class.

14. ``my_sentence`` is a string object.  Strings, in Python, have a method available called ``split()`` that does exactly that.  I looks for a pattern within the string and splits the string into a list where each entry is the patterns separated by the split.  If the argument to ``split()`` is left blank it will default to the ``space`` character.  We can define other characters to split against.

    In[1]: my_str = '1,2,3'

    In[2]: my_str.split(',')
    Out[2]: ['1', '2', '3']

15. Conversly strings have a ``join()`` method.  This might seem misleading at first - you may think the list should have the ``join()`` method because you are joining each element in the list.  This is not the case - and it makes sense when you think about it.  The reason is because the result you are looking to get is a string.  An object method on a list shouldn't result in a string.  Why would an objects method change the object type?  That doesn't make sense.  Plus, with the ``join()`` method on strings you can do lots of useful joins that would otherwise not make sense if it were a method on a list.

    In[1]: my_list = ['a', 'n', 'd']

    In[2]: '-'.join(my_list)
    Out[2]: 'a-n-d'

    In[3]: ' - 123'.join(my_list)
    Out[3]: 'a - 123n - 123d'

To see more on what methods are available for Python strings see the official `docs <http://docs.python.org/3.3/library/string.html?highlight=string#module-string>`_.

List Comprehension
-----------------

Python is capable of creating elaborate lists with a single command.  The process by which this is done is called ``list comprehension``.  This might seem confusing at first but with practice you'll learn to embrace the concept.  You should also be aware that Python has optimized list comprehensions so creating lists using this technique is much more efficient.

    my_list = list()
    for i in range(0, 100):
        my_list.append(i)

The above statement is equivalent to the following list comprehension.

    my_list = [i for i in range(0, 100)]

It's not so difficult, right?  Let's look at the advanced exercise 13 from last class.  The variable ``my_str`` has 3 characters.  Using the list comprehension we're looping through each with the ``for``.  We're naming each value we get from the ``iterator`` ``char``.  Then we're ``appending`` to the list ``char``.

    [some_value for some_value in some_iterator]

You can rest assured we're going to have some fun exercises with list comprehensions.

Dictionaries
-----------------

Python dictionaries are similar to ``hash`` or ``associative array`` in other languages.  It's simply a ``key``:``value`` pair.  Then the dictionary can be referenced by the ``key`` to get the ``value``.

    In[1]: my_dict = {'key': 'value'}

    In[2]: my_dict['key']
    Out[2]: 'value'

The key and value can be any Python object - this is where the true power lies.

    In[1]: my_list = [1, 2, 3, 4, 5]

    In[2]: my_dict = {
        'max_value': max(my_list),
        'min_value': min(my_list)
    }

    In[3]: my_dict['min_value']
    Out[3]: 1


Exercises
-----------------

1. Given the following dictionary, create a list that contains a tuple for each key:value pair.

    person_info = {
        'first_name': 'Rico',
        'last_name': 'Cordova',
        'email': 'rico.cordova@rocksolidbox.com',
        'favorite_language': 'Python'
    }

    i.e. Your result should look like [('first_name', 'Rico'), ('last_name', 'Cordova'), ...]

2. Let's do the reverse.  Given the above list create a dictionary from the information.

3. Using the person_info given above create a personal greeting string.

4. You are designing a game and have a list of players logged in to your system.  Given the list of names of each user in the system randomly choose 2 who will compete against each other in battle.  Be sure that the user won't be chosen to fight themselves.

    ['rico', 'dal', 'corban', 'brandon', 'kris', 'rob', 'luke']


Advanced Exercises
-----------------

5. Pit the two players against each other in simulated battle for 3 rounds.  Each player can deal damage from 1 to 100 each round (using a Gaussian distribution).  Whoever deals the most damage wins!

6. Randomly choose 4 players and make 2 teams to do battle.  Same rules, each player can do 1 to 100 damage per round to the other team.  Whichever team deals the most damage wins.
