# poi

poi is a terminal application to fetch multiple answers from Stackoverflow easily

## Installation

Download/clone the repository


Run ```sudo chmod +x poi.py``` to grant execute permissions

Install all necessary imports

## Usage

Run poi with the query at hand

```
./poi.py how to init array in java
```

Then you'll see a list of results during which you can copy and/or visit the link
```
[anthony@bloom Programming]$ ./poi.py how to init array in java
[-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------] 100%

1: How to initialize an array in Java?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        1       data[10] = {10,20,30,40,50,60,71,80,90,91};

        The above is not correct (syntax error). It means you are assigning an array to data[10] which can hold just an element.

        If you want to initialize an array, try using Array Initializer:

        2       int[] data = {10,20,30,40,50,60,71,80,90,91};
        2
        2       // or
        2
        2       int[] data;
        2       data = new int[] {10,20,30,40,50,60,71,80,90,91};

        Notice the difference between the two declarations. When assigning a new array to a declared variable, new must be used.

        Even if you correct the syntax, accessing data[10] is still incorrect (You can only access data[0] to data[9] because index of arrays in Java is 0-based). Accessing data[10] will
        throw an ArrayIndexOutOfBoundsException.

2: How do I declare and initialize an array in Java?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        You can either use array declaration or array literal (but only when you declare and affect the variable right away, array literals cannot be used for re-assigning an array).

        For primitive types:

        1       int[] myIntArray = new int[3];
        1       int[] myIntArray = {1, 2, 3};
        1       int[] myIntArray = new int[]{1, 2, 3};
        1
        1       // Since Java 8. Doc of IntStream: https://docs.oracle.com/javase/8/docs/api/java/util/stream/IntStream.html
        1
        1       int [] myIntArray = IntStream.range(0, 100).toArray(); // From 0 to 99
        1       int [] myIntArray = IntStream.rangeClosed(0, 100).toArray(); // From 0 to 100
        1       int [] myIntArray = IntStream.of(12,25,36,85,28,96,47).toArray(); // The order is preserved.
        1       int [] myIntArray = IntStream.of(12,25,36,85,28,96,47).sorted().toArray(); // Sort 

        For classes, for example String, it's the same:

        2       String[] myStringArray = new String[3];
        2       String[] myStringArray = {"a", "b", "c"};
        2       String[] myStringArray = new String[]{"a", "b", "c"};

        The third way of initializing is useful when you declare the array first and then initialize it. The cast is necessary here.

        3       String[] myStringArray;
        3       myStringArray = new String[]{"a", "b", "c"};

3: Java Initialize an int array in a constructor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        1       private int[] data = new int[3];

        This already initializes your array elements to 0. You don't need to repeat that again in the constructor.

        In your constructor it should be:

        2       data = new int[]{0, 0, 0};

4: Java: how to initialize String[]?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        You need to initialize errorSoon, as indicated by the error message, you have only declared it.

        1       String[] errorSoon;                   // <--declared statement
        1       String[] errorSoon = new String[100]; // <--initialized statement

        You need to initialize the array so it can allocate the correct memory storage for the String elements before you can start setting the index.

        If you only declare the array (as you did) there is no memory allocated for the String elements, but only a reference handle to errorSoon, and will throw an error when you try to
        initialize a variable at any index.

        As a side note, you could also initialize the String array inside braces, { } as so,

        2       String[] errorSoon = {"Hello", "World"};

        which is equivalent to

        3       String[] errorSoon = new String[2];
        3       errorSoon[0] = "Hello";
        3       errorSoon[1] = "World";

5: Any shortcut to initialize all array elements to zero?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        A default value of 0 for arrays of integral types is guaranteed by the language spec:

        If you want to initialize an one-dimensional array to a different value, you can use java.util.Arrays.fill() (which will of course use a loop internally).

Copy (c) and/or Visit (v)? (e.g. c32v4 to copy block 2 in option 3 and visit option 4, c21, c4, ...)
```
Examples
```
c23 #copies code block 3 of option 2
v4 #visits option 4
c12v1 #copies code block 2 of option 1 and visits option 1

```
