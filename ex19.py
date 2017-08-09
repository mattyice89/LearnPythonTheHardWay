# defining the argument Cheese and crackers and naming your variables
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    # printing out the first variable, named "cheese_count"
    print(f"You have {cheese_count} cheeses!")
    # printing out the second variable, named "boxes_of_crackers"
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # some bullshit
    print("Man that's enough for a party!")
    # more bullshit
    print("Get a blanket.\n")

# loading the exact numbers you want into your function
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# you can create new variables and call them in your function
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

# using math instead of variables - note that this doesn't then Get
# stored as the variables that we defined in the previous step
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# prints using the variables we defined two steps ago plus some math
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
