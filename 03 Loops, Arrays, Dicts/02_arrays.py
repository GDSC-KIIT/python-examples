# Arrays/Lists are dynamically sized arrays that you can
# use to store homogeneous and heterogeneous data

a = [1, 2, 3]
b = ["python", 123, "allows", 3.45, "this"]

garage = ["ferrari", "mercedes", "aston martin"]

for car in garage:  # you can iterate over arrays
    print(car)

tic_tac_toe = [
    ["x", "o", "o"],
    ["o", "x", "0"],
    ["o", "o", "x"]
]

for line in tic_tac_toe:
    for move in line:
        print(move, end=" ")
    print()


# Slicing Arrays
# Python has a wonderful set of features to deal with arrays

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(a[3])
print(a[-1])
print(a[-3])
print(a[2:4])
print(a[3::])
print(a[::4])
print(a[::-1])

# List comprehensions - Dynamically building arrays


squares = [x**2 for x in range(0, 10)]
print(squares)
