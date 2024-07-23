numbers = [2, 4, 6, 8]
all_even = all(num % 2 == 0 for num in numbers)

print("All numbers are even:", all_even)

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is not even.")

numbers_with_odds = [2, 4, 5, 8]
all_even_with_odds = all(num % 2 == 0 for num in numbers_with_odds)
print("All numbers are even (with odds):", all_even_with_odds)




