def square_cube(square, cube):
    print "The square of %d is " % square
    print square * square
    print "The cube of %d is " % cube
    print cube * cube * cube


print "Lets try with 4 and 5"
square_cube(4,5)

print "Lets try with adding inside the function"
square_cube(4+5, 5+5)

print "Lets try with subtracting inside the function"
square_cube(5 - 6, 6 - 7)