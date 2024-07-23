numbers = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", evens)

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
