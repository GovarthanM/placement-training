fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")

print("Index of 'banana':", index)

print("Fruit at index", index, "is", fruits[index])

if 0 <= index < len(fruits):
    print("The index is within the valid range of the list.")
else:
    print("The index is out of range.")

try:
    n=input("Fruit Name: ")
    missing_index = fruits.index(n)
    print("Index of 'grape':", missing_index)
except ValueError:
    print("'grape' is not in the list.")
