i = 0
x = 50
y = x/10
numbers = []
while i <= x:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + y
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)
