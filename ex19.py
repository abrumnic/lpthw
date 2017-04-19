# Define the function taking two arguments.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    
    # Print the first argument.
    print "You have %d cheeses!" % cheese_count
    
    # Print the second argument.
    print "You have %d boxes of crackers!" % boxes_of_crackers
    
    # Make some joke or comment.
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    

# Pass to the function plain numbers.
print "We can just give the function numbers directly:"

# Call of the function with plain numbers.
cheese_and_crackers(20, 30)


# Define variables.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# Call of the function with the before defined variables as arguments.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can do math inside too:"

# Call of the function with math operation on plain numbers as arguments.
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two variables and math:"

# Call of the function with math opretaion on plain numbers and variables as
# arguments.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Definition of a new function to print the name an age.
def print_name(var_name, var_surname, var_age):
    print "You are %s %s." % (var_name, var_surname)
    print "You are %r years old." % var_age
    
prompt = '-->'

print "Enter your name please:"
user_name = raw_input(prompt)

print "Enter your surname please:"
user_surname = raw_input(prompt)

print "Enter your age please:"
user_age = int(raw_input(prompt))

# 1st time.
print_name(user_name, user_surname, user_age)

# 2nd time.
print_name('Vesna', 'Brumnic', 42)

# 3rd time
print_name('Mihaj' + 'lo', 'Pupin', 100 + 56)

# 4th time
print_name(user_name + '\n', '\t' + user_surname, user_age + 5)

# 5th time.
print_name(user_name + 'A', user_surname + 'B', user_age / 7.)

# 6th time.
print_name('A' + user_name, 'B' + user_surname, user_age / 13.)
