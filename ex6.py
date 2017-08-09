# stating the variable "types_of_people" has a value of 10
types_of_people = 10
# storing and formatting the string "There are 10 types of people."
# into variable "x"
x = f"There are {types_of_people} types of people."

# Storing a string as a variable
binary = "binary"
do_not = "don't"
# storing and formatting the string "Those who know binary and Those
# who don't" in variable "y"
y = f"Those who know {binary} and those who {do_not}."

# print "There are 10 types of people"
print(x)
# print "Those who know binary and those who don't"
print(y)

# print "I said There are 10 types of people"
print(f"I said: {x}")
# print "I also said Those who know binary and those who don't"
print(f"I also said: '{y}'")

# giving the variable "hilarious" with the False result
hilarious = False
# storing "Isn't that joke so funny?! False" in the variable
# "joke_evaluation"
joke_evaluation = "Isn't that joke so funny?! {}"

# Print "Isn't that joke so funny?! False"
print(joke_evaluation.format(hilarious))

# storing the string "This is the left side of..." in variable "w"
w = "This is the left side of..."
# storing the string "a string with a right side." in variable "e"
e = "a string with a right side."

# print "This is the left side of...a string with a right side."
print (w + e)
