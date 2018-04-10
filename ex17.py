# Importing the argument variable - argv from the sys module
from sys import argv

# For the checking if the file exists.
from os.path import exists

#Definition and initialization of two argument variables.
script, from_file, to_file = argv

# Anouncing the action of file to file copying.
print "Copying from %s to %s." % (from_file, to_file)

# Opening the file named filename, and returning the value to txt variable
in_file = open(from_file); indata = in_file.read()

# Another way to open and read the file.
#indata = open(from_file).read()

# Getting the file length in bytes.
print "The input file is %d bytes long." % len(indata)

# Check the output file..
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit ENTER / RETURN to continue, CTRL-C to abort."
raw_input()

# Open and write to the output file.
out_file = open(to_file, 'w')
out_file.write(indata)

# Close the file.
print "Alright, all done."
out_file.close()
in_file.close()