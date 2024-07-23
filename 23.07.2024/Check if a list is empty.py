numbers = []
if not numbers:
    print("List is empty")

numbers = [1, 2, 3]

if not numbers:
    print("List is still empty")
else:
    print("List is not empty")

empty_list = []
non_empty_list = [5, 10, 15]

for lst in [empty_list, non_empty_list]:
    if not lst:
        print("The list is empty.")
    else:
        print("The list contains:", lst)

empty_string = ""
if not empty_string:
    print("String is empty")

empty_dict = {}
if not empty_dict:
    print("Dictionary is empty")
