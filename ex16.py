# Importing the argument variable - argv from the sys module
from sys import argv

#Definition and initialization of two argument variables.
script, filename = argv

# Anouncing the action of file deletion.
print "We're going to erase %r." % filename

# Opening the file named filename, and returning the value to txt variable
print "Opening the file for reading..."
target = open(filename)

# Read the file content.
print "Here is the file content."
print target.read()

# Giving the user the posibility not to delete the file.
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit ENTER/RETURN."

# Expectiong the user decision.
raw_input("?")

# Close the file and opening it for writing..
print "Close the file and open it for writing."
target.close()
# Truncating the file filename..
print "Truncating the file while opening for write and read. Goodbye!"
target = open(filename, 'w')

# Initiating a second action.
print "Now I'm going to ask you for thee lines."

# Getting the lines.
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# Anouncing the write to file filename of the entered lines.
print "I'm going to write these to the file."

# # Write line1.
# target.write(line1)

# # Adding new-line caracter at the end of line1.
# target.write("\n")

# # Write line2.
# target.write(line2)

# # Adding new-line caracter at the end of line2.
# target.write("\n")

# # Write line3.
# target.write(line3)

# # Adding new-line caracter at the end of line3.
# target.write("\n")

file_content = line1 + "\n" + line2 + "\n" + line3 + "\n"
# Write lines all together..
target.write(file_content)

# Close the file before reading.
print "Closing and opening for reading."
target.close()

# Opening the file named filename, and returning the value to txt variable
print "Opening the file for reading..."
target = open(filename)

# Read the new data entered.
print "Here is the new file content."
print target.read()

# Close the file.
print "And finaly we close it."
target.close()