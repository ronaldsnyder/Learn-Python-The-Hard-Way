#chapter 17 from Learn Python the Hard Way
#my own shortened version.
from sys import argv

script, from_file, to_file = argv

indata = open(from_file).read()

out_file = open(to_file,'w').write(indata)

