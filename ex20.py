#imports the function argv
from sys import argv

script, input_file = argv

# defines the new function we're creating called print_all and
# naming the file "f"
def print_all(f):
    print(f.read())

# defining our function "rewind" which starts the file over at the
# beginning (note it's starting at the first byte, not first line)
def rewind(f):
    f.seek(0)

# defines the function "print_a_line" which prints the two arguments
# "line_count", which is new, and "f", which we defined in
# the print_all function
def print_a_line(line_count, f):
    print(line_count, f.readline())

# defines the varaible "current_file" as opening the input_file which
# was part of the input text when we called the script ex20.py
current_file = open(input_file)

print("First let's print the whole file:\n")

# prints open(input_file)
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# rewinds current_file to the start so we can print it again
rewind(current_file)

print("Let's print three lines:")

# tells the print to start on the first line
current_line = 1
print_a_line(current_line, current_file)

# tells the print_a_line function to add one to the current line
# and print it
current_line = current_line + 1
print_a_line(current_line, current_file)

# tells the print_a_line function to add one to the current line
# and print it
current_line = current_line + 1
print_a_line(current_line, current_file)
