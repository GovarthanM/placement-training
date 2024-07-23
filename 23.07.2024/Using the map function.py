numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))

print("Squares:", squares)

for number, square in zip(numbers, squares):
    print(f"The square of {number} is {square}")

squares_comprehension = [x**2 for x in numbers]
assert squares == squares_comprehension, "The results do not match!"

empty_numbers = []
empty_squares = list(map(lambda x: x**2, empty_numbers))
print("Squares of empty list:", empty_squares)
