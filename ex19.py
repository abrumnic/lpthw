from sys import argv

script, input_file = argv

# Print what you read.
def print_all(f):
    print f.read()

# Return to the begining of the file.
def rewind(f):
    f.seek(0)

# Print a single line.
def print_a_line(line_count, f):
    print line_count, f.readline()
    
# Open the file.
current_file = open(input_file)

# Print the whole file.
print "First let's print the whole file:\n"
print_all(current_file)


# Return to the beginning.
print "Now let's rewind, kid of like a tape."
rewind(current_file)

# Print the lines.
print "Let's print three lines:"

current_line = 1
print current_line
print_a_line(current_line, current_file)

current_line += 1
print current_line
print_a_line(current_line, current_file)

current_line += 1
print current_line
print_a_line(current_line, current_file)