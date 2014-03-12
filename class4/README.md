April 14, 2014
==============

Review From Class3
-----------------

During the last class we expanded on the concept of functions.  Functions allow modularization of code for repeated use without so as to not violate the DRY principle.

Additionally we discussed recursion and how it's used in Python.  Using functions we were able to create a recursive algorithm for generating the Fibonacci sequence.  The advanced exercise also used recursion and created a "pretty_print" function for displaying Python objects to STDOUT.

The advanced exercise used ``isinstance()``, which is a form of ``introspection`` available in Python.  We'll discuss this in more depth after we introduce classes.

Classes
-----------------

The most fundamental concept in Python are classes.  Classes are what defines objects in Python - and everything in Python is an object.  Using classes we're able to define functionality that can all fit within a single namespace and be used in a modular fashion.  Functions are used within classes to help accomplish modularity.  When a function is within a class it is called a ``method``.  The term method isn't anything special - it's just a way of distinguishing that a function is property of a class rather than stand-alone.

Classes are very powerful and provide the flexibility needed to build current enterprise level projects.  Designing code with classes is called Object Oriented Design (OOD).  Using classes in your programming is called Object Oriented Programming (OOP).

There are 3 fundamental ways to create a class in Python.  First, is the old-style object type and is only available in Python 2.

    class MyCar:
        pass

Second, is the new-style class available starting in Python 2.2 and are the de facto class type to be used.  Always use new-style classes.  In Python 2.x you can create a new-style class as follows.

    class MyCar(object):
        pass

Notice the ``(object)`` syntax.  This syntax is using a concept called inheritance.  The newly defined ``MyCar`` object is inheriting some functionality from the object ``object``.  Don't get confused about the naming here.  Everything in Python is an object but the keyword ``object`` object is a special kind of object.  Don't fret too much about this...just always inherit ``object`` when you are defining your class.

In Python 3 old-style classes don't even exist.  So, you can define your class without inheriting anything and it'll fundamentally have the functionality of a new-style object.

    class MyCar:
        pass

Remember, the 1st and 3rd examples here may look the same but they are fundamentally different when you consider the 1st example is interpreted with Python 2, while the 2nd example is using Python 3.  This should give you some insight into what problems you may face if trying to make your code to be compatible with both 2.x and 3.

To make it easier to support both Python 2.x and 3 they made it possible to explicitly inherit from ``object`` in Python 3.

    class MyCar(object):
        pass

The 3rd and 4th example here are equivalent in Python 3.  So making your code compatible for 2.x and 3 shouldn't be a problem when defining classes.

Instantiation
-----------------

The power behind a class is the ability to instantiate it.  Instantiation is simply creating a copy that functions independently of any other instantiation.  To instantiate a class simply declare a new object set equal to the class call.

    In[1]: my_car = MyCar()

Now, you have a ``my_car`` object that is an instantiation of ``MyCar``.  It is a local copy, can be manipulated, used for calculations, etc and all other instantiations of ``MyCar`` will be unaffected by the activity against this instantiation.

Notice the naming convention used here.  Classes use ``UpperCamelCase`` and the object instantiation uses the same name with ``lower_underscore``.  This the PEP8 standard.

If you are doing multiple instantiations of a class each will need a unique name (otherwise you'll be overwriting).  In this case it's common practice to append an index at the end of the name or name them to represent their intended functionality.

    In[1]: my_car1 = MyCar()
    In[2]: my_car2 = MyCar()

Or

    In[1]: aston_martin = MyCar()
    In[2]: maserati = MyCar()

Initialization
-----------------

During the instantiation of a class Python will use a ``magic method`` named ``__init__()``.  It is common practice to set initialization parameters within the ``__init__()`` method.  The ``object`` within Python contains a definition of ``__init__()`` but just uses ``pass``.  So, you are able to ``overwrite`` the ``__init__()`` by simply defining it within your class.

    class MyCar(object):
        def __init__(self, year, make, model, owner):
            self.year = year
            self.make = make
            self.model = model
            self.owner = owner

Now, when you instantiate an object you can initialize it with information.  Using the example above.

    In[1]: aston_martin = MyCar(2014, 'Aston Martin', 'DB9', 'James Bond')
    In[2]: maserati = MyCar(2014, 'Maserati', 'Granturismo', 'Christopher Moltisanti')

self
-----------------

You'll notice the use of the syntax ``self``.  This represents the instance of the object.  It is similar to ``this`` in other languages.  Each method in a class have ``self`` as the first argument so Python knows what object the method is being executed against.  To assign an attribute ``attr`` to a class simply assign the value to ``self.attr`` during instantiation.

The attributes associated with an object can be accessed using ``.`` notation.

    In[1]: print(aston_martin.model)
    Out[1]: DB9

Using ``self`` you now have access to the attribute within the scope of the object.

    class MyCar(object):
        def __init__(self, year, make, model, owner):
            self.year = year
            self.make = make
            self.model = model
            self.owner = owner

        def change_owner(self, new_owner):
            self.owner = new_owner

Using the above examples we can see how the instance changes as we execute methods against it.

    In[1]: print(aston_martin.owner)
    Out[1]: James Bond

    In[2]: print(maserati.owner)
    Out[2]: Chrisopher Moltisanti

    In[3]: aston_martin.change_owner('Rico Cordova')

    In[4]: print(aston_martin.owner)
    Out[4]: Rico Cordova

This is no different than any other object method we've been using throughout this course.  Consider formatted strings.

    In[1]: my_str = 'Hello, my name is {}.'

    In[2]: print(my_str)
    Out[2]: Hello, my name is {}.

    In[3]: my_str = my_str.format('Rico')

    In[4]: print(my_str)
    Out[4]: Hello, my name is Rico.


Introspection
-----------------

Using introspection we can inspect information about the structure of objects within Python.

In the advanced exercise in class 3 we used ``isinstance`` to inspect the object being passed to the ``pretty_print`` function to determine, at run time, how to handle it.  The ``isinstance`` built-in function is an introspective tool.

    In[1]: isinstance(aston_martin, MyCar)
    Out[1]: True

Exercise 1
-----------------

Create a class called ``Human`` that has an attribute for name, age and hair color.  Create a class called ``Cat`` that has an attribute for name, gender, breed and owner, where owner is a ``Human`` object.

Create a method in each of these classes to change each attribute (setter).

Exercise 2
-----------------

Given a list of objects, create a function that will change the owner of all the ``Cat`` objects to ``None``.

Exercise 3
-----------------

Given a list of objects, create a function that will assign a new ``Human`` owner to all cats that have no owners.

Advanced Exercise 1
-----------------

Create a class called ``Player`` with attributes health, level and name.  Set the health and level to initialize to 500 and 1, respectively.  Give the class a method called ``attack()`` that returns a random (uniform distribution) value between 10 and 50 multiplied by ``level``.

Create a class called ``Battle`` that instantiates with 2 player objects.  Create a ``do_battle()`` method that handles the players attacking each other using their ``attack()`` method.  Continue attacking until one of the players is dead.  Report information about the battle (who won, damage done, number of rounds, etc).

