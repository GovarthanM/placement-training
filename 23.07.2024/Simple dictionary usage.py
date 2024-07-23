name = input("Enter the student's name: ")
age = int(input("Enter the student's age: "))
courses = input("Enter the student's courses, separated by commas: ").split(',')
student = {
    "name": name,
    "age": age,
    "courses": [course.strip() for course in courses]
}

print(student["name"])
