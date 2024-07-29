List Creation and Access
x = ["blue", "green", "red", "orange", "yellow"]
print(x[2])

List Slicing
x = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print(x[0:5])

Append and Insert
fruits = []
fruits.append(["apple", "orange", "grapes"])
print(fruits)
fruits.insert(3,"banana")
print(fruits)

Remove and Pop
cities = ["Rawalpindi", "Karachi", "Hyderabad"]
cities.remove(cities[1])
cities.pop()
print(cities)

List Comprehensions
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)

List iterations
animals = ['cat', 'dog', 'wolf', 'tiger', 'monkey']
for x in animals:
    print(x)

List Methods
integers = [3, 4, 5]
print(sum(integers))

List Sorting &List Length
numbers = [4, 3, 5, 6, 0, 2]
numbers.sort()
print(len(numbers))

Dictionary Creation
data = {
    "name": "Saad Altaf",
    "age": "24",
    "city": "Rawalpindi"
}
data["city"] = "Karachi"
print(data)
data.update({"country": "Pakistan"})
print(data)
data.pop("age")
print(data)
for x in data.items():
    print(x)
if "name" in data:
    print("Name is present in the list")
for x in data.keys():
    print(x)
for x in data.values():
    print(x)

students_grade = {
    "studentOne" : {
        "English": "A",
        "Urdu": "A+",
        "Science": "B"
    },
    "studentTwo" : {
        "English": "C",
        "Urdu": "D",
        "Science": "A"
    },
    "studentThree" : {
        "English": "F",
        "Urdu": "E",
        "Science": "A+"
    }
}

print(students_grade["studentTwo"]["Science"])
for all, student in students_grade.items():
    print(all)
    for all_values in student:
        print(all_values + ":", student[all_values])
        


dict1 = {1: 'One', 2: 'Two', 3: 'Three'}
dict2 = {3: 'Zero', 4: 'Four'}

print('Merged dictionary:', dict1|dict2)


animals = ['cat', 'dog', 'wolf', 'tiger', 'monkey']

a = [[1,2],[3,4]]
print(a[1][1])

for i in range(len(a)):
    print(i)
    print(a[i])
