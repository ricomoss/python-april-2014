April 23, 2014
==============

Review From Class6
-----------------

During the last class we exceptions and exception handling.  Using exception handling you can define your API to be very specific and handle information meeting your intent.  Exceptions help avoid unwanted behavior and exception handling allows you to customize flow based on unwanted behavior.

Inheritance
-----------------

Using classes allows us to create instantiable objects.  Python allows for class inheritance.  Inheritance is the ability to create a subclass from a base class, where the subclass inherits functionality from the base class.  Inheritance allows us to adhere to the DRY principle and gives you more opportunity to modularize your code making it easier to read and design.

Suppose we want to create classes for a square, rectangle and triangle.  These are all shapes and we could use a shape class that contains generic information about what attributes belong to shapes then create specific classes for each shape.

What attributes do all these shapes have in common?  They all have area and a number of sides.  (There are more but we'll limit our example to these two.)

What about these shapes are different?  Their areas are calculated differently.

So, let's create a generic class for shape and see how to use inheritance.

    class Shape(object):
        def __init__(self, area=0, num_of_sides=0):
            self.area = self._get_area()
            self.num_of_sides = num_of_sides

        def _get_area(self):
            pass

    class Square(Shape):
        def __init__(self, length_of_side=0):
            self.length_of_side = length_of_side
            super(Square, self).__init__(area=area, num_of_sides=4)

        def _get_area(self):
            return pow(self.length_of_side, 2)

Before moving on to the other shapes notice how we were able to avoid assigning ``self.area`` in the ``Square`` class because it will be handled in ``Shape``.  Also, notice how we needed to define ``_get_area()`` in ``Square``.  This method will be necessary for each unique shape type so we should put functionality in ``Shape`` that requires that method.

    class Shape(object):
        def __init__(self, area=0, num_of_sides=0):
            self.area = self._get_area()
            self.num_of_sides = num_of_sides

        def _get_area(self):
            msg = 'This shape must have a method to get area.'
            raise NotImplementedError(msg)

    class Rectangle(Shape):
        def __init__(self, length=0, width=0):
            self.length = length
            self.width = width
            super(Rectangle, self).__init__(area=area, num_of_sides=4)

        def _get_area(self):
            return self.length * self.width

    class Triangle(Shape):
        def __init__(self, base=0, height=0):
            self.base = base
            self.height = height
            super(Triangle, self).__init__(area=area, num_of_sides=3)

        def _get_area(self):
            return self.base * self.height / 2

File I/O
-----------------

The ability to read from and write to files is important in any programming language.  Much of the data that needs processing already exists and you'll need a way to import that data for processing.

We've talked about several built in types - dictionary, tuple, list, integer, float, etc.  Python also has a type ``file``.  The ``file`` object has several methods available for reading and writing against files on your computer.  It can even remove, create and rename files...and much more.

Let's look at a basic example of how to write to a file.

    filename = 'example.txt'
    my_file = open(filename, 'w')

The ``open`` function will create a ``file`` object based on the parameters passed.  The path to the file given as a string is the first argument.  All other arguments are ``kwargs`` where the ``mode`` is the second position, we've chosen to write to the file ('w') - see more info here (http://docs.python.org/3.3/library/functions.html#open)

Now we have a file object open for writing.  To write simply use ``.write()``.  Always be sure to close your file object when you're done!

    my_file.write('hello world')
    my_file.close()

Now let's open the file for reading and see what it says.

    In [1]: my_file = open(filename)

    In [2]: my_file.read()
    Out [2]: 'hello world'

Let's write more and see how it looks.  To do so we must now append rather than write.  If you continually open a file in write mode it clears the existing file and starts over.

    my_file = open(filename, 'a')
    my_file.write('another line')
    my_file.close()

Let's print it out again.

    In [1]: my_file = open(filename)

    In [2]: my_file.read()
    Out [2]: 'hello worldanother line'

Did you expect that?  Python's file I/O doesn't try and be smart it will start exactly where it left off when appending to a file.  If you intend to have separate lines you need to append ``\n`` at the end of the line.

    my_file = open(filename, 'w')
    my_file.write('hello world\n')
    my_file.write('another line\n')
    my_file.close()

Now you will have two separate lines in your file.

    In [1]: my_file = open(filename)

    In [2]: my_file.read()
    Out [2]: 'hello world\nanother line\n'

This might not be the easiest way to read the output but you can see the newlines exist where they should.  Now that you understand the basic functionality we'll introduce ``with`` as the proper way to do file I/O - it handles the closing for you!

    with open(filename, 'w') as my_file:
        my_file.write('hello world\n')
        my_file.write('another line\n')

You will get the same results in fewer lines and safer code.

    In [1]: with open(filename) as my_file:
       ....:     lines = my_file.read()
       ....:     print(lines)
       ....:
    hello world
    another line

There are several methods available for reading and writing to files.  You can read the entire file into a list with ``.readlines()``.  You can seek manually using ``.seek()``.  Play around and see what you can come up with.

Exercise 1
-----------------

Using the example above, which shape could have inherited from another shape?  Rewrite the class to use this inheritance.

Exercise 2
-----------------

Using file I/O create a file that contains the first 30 fibonacci numbers - one number per line.

Advanced Exercise 1
-----------------

Update the ``Player`` class to have experience.  Let the player level be dictated by the experience as follows:

    Level 1: exp >= 0
    Level 2: exp >= 10
    Level 3: exp >= 100
    Level 4: exp >= 1000
    Level 5: exp >= 10000
    Level 6: exp >= 100000
    Level 7: exp >= 1000000
    Level 8: exp >= 10000000
    Level 9: exp >= 100000000
    Level 10: exp >= 1000000000

Create a method for the ``Hero`` that grants experience

Advanced Exercise 2
-----------------

Create an information file for each "PLAYER_NAME_CHOICES" in a folder named "save_info".

Create a method for the ``Hero`` class that will update the player's save info with their current experience.

Update the ``Battle`` class to assign experience after each battle so that 2 experience is given to the winner and 1 experience is given to the loser.

Update the ``Hero`` class to get the experience from the save info file.
