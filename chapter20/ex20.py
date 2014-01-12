from sys import argv

script, input_file = argv

#print the entire file
def print_all(f):
    print f.read()

#go back to line 0
def rewind(f):
    f.seek(0)

#print a specific line of the file    
def print_a_line(line_count, f):
    print line_count, f.readline()

#open the file    
current_file = open(input_file)

print "First let's print the whole file:\n"

#print the entire file out to console
print_all(current_file)

print "Now let's rewind, kind of like a tape"

#go back to line 0
rewind(current_file)

print "Let's print three lines:"
#set the current line at 1 and print it out
current_line = 1
print_a_line(current_line, current_file)

#add 1 to the current line and print
current_line += 1
print_a_line(current_line, current_file)

#add 1 to the current line and print
current_line += 1
print_a_line(current_line, current_file)