from sys import argv

script, filename = argv

# Using argv to get a file name from when you initially run the program
txt = open(filename)
print(f"Here's your file {filename}:")
print(txt.read())

# Using input() to get the filename once the program has started
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
