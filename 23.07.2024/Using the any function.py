numbers = [1, 3, 5, 7]
any_even = any(num % 2 == 0 for num in numbers)

print("Any number is even:", any_even)

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is not even.")

numbers_with_evens = [1, 2, 5, 7]
any_even_with_evens = any(num % 2 == 0 for num in numbers_with_evens)
print("Any number is even (with evens):", any_even_with_evens)

