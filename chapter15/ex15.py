#make the script have arguments
from sys import argv

#define arguments
script, filename = argv

#open the file
txt = open(filename)

#print the file name and then the file
print "Here's your file %r:" % filename
print txt.read()
txt.close()

#ask for the filename again and print it out
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()