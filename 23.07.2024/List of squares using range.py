squares = [x**2 for x in range(10)]

print("Squares:", squares)

for x in range(10):
    print(f"The square of {x} is {x**2}")

more_squares = [x**2 for x in range(5, 15)]
print("Squares from 5 to 14:", more_squares)

start = 1
end = 5
custom_squares = [x**2 for x in range(start, end)]
print(f"Squares from {start} to {end-1}:", custom_squares)
