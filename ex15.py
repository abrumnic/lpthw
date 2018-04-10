# Importing the argument variable - argv from the sys module
from sys import argv
#Definition and initialization of two argument variables.
script, filename = argv

# Opening the file named filename, and returning the value to txt variable
txt = open(filename)

# Print the file name and content.
print "Here's your file %r:" % filename
# Print the file content.
print txt.read()

# Close the file.
txt.close()

# Get new file_name.
print "Type the filename again:"
# SAve new file_name in the file_again variable.
file_again = raw_input("--> ")
# Opening the file named filename, and returning the value to txt_again variable
txt_again = open(file_again)

# Print the file content.
print txt_again.read()

# Close the file.
txt_again.close()