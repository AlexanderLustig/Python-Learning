student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Comp Sci']}
student2 = {1: 'John', 'age': 44}

print(student['name'])
print(student2[1])
print(student.keys())
print(student.items())

student['name'] = "Jane"
print(student['name'])

print(student.get('name'))
print(student.get('phone', 'Not Found'))
student['phone'] = "555-5555"
print(student.get('phone', 'Not Found'))

del student['age']
print(student)

age = student2.pop('age')
print(student2)
print(age)

student.update({'name': 'Bob', 'age': 45, 'phone': '595-5532'})
print(student)

for key in student:
    print(key)

for key, value in student.items():
    print(key, value)