from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")
# Open filename i write mode
target = open(filename,'w')

# truncating (deleting contents of) file
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

#these are the text to be input into the model
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# write what you entered to line 1 in the first line
target.write(line1)
# linebreak
target.write("\n")
# text to be entered on line 2
target.write(line2)
# linebreak
target.write("\n")
# text to be entered on line 3
target.write(line3)
# linebreak
target.write("\n")

print("And finally, we close it.")
# closes and saves the file
target.close()
