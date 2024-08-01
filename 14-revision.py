#tuples

# tuple_01 = ('Apple', 34, 46.4, True)
# tuple_02 = (1, 2, 3, 5)
# print(type(tuple_01))
# print(tuple_01[1:3])
# print(len(tuple_01))
# print(tuple_01 + tuple_02)
# print(tuple_02*2 + tuple_01)
# print(min(tuple_02))
# print(max(tuple_02))

#dictionaries

# fruits_1 = {"apple": 10, "banana": 24}
# fruits_2 = {"guava": 10, "orange": 24}
# fruits_1.update(fruits_2)
# print(fruits_1)
# fruits["guava"] = 50
# fruits["apple"] = 100
# print(fruits)
# fruits.pop("guava")
# print(fruits)
# print(type(fruits))
# print(fruits.keys())
# print(fruits.values())

#sets

# s1 = ["a", "b", "b","c", "a"]
# s2 = {2, 4, 3, 6, 0}
# s1.union(s2)
# s1.update()
# s1.add("sparta")
# s1.remove("b")
# print(s1.union(s2))
# if s1[0] == "a":
#     s1[0] = "S"
#     print(s1)


#if, elif & else

# d1 = {"k1": 10, "k2":20, "k3":30}
# if d1["k1"] == 10:
#     d1["k1"] += 100

# print(d1)

#for & While loop
# s1 = ["a", "b", "b","c", "a"]
# s2 = ["v", "4", "f","r", "3"]
# for i in s1:
#     print(i)

# for i in s1:
#     for j in s1:
#         print(i, j)

# i = 10
# while i>1:
#     print(i)
#     i-=2


# i = 1
# n = 2

# while i <= 10:
#     print(f"{n} * {i} = {n*i}")
#     i += 1


# i = 1
# n = input("Please enter number: ")
# if n.isdigit():
#    n = int(n)
# else:
#     print("Please enter valid number!")
#     quit()
# while i <= 10:
#     print(f"{n} * {i} = {n*i}")
#     i+=1
#     continue

# l1 = [1,2,3,4,5]
# i = 0
# while i< len(l1):
#     l1[i] += 100
#     i+=1

# print(l1)

    
#class & Objects
# class Phone:

#     def set_color(self, color):
#         self.color = color

#     def set_cost(self, cost):
#         self.cost = cost

#     def show_color(self):
#         return self.color

#     def show_cost(self):
#         return self.cost

#     def make_call(self):
#         print("make a phone call")

#     def play_game(self):
#         print("let's play game")

# p1 = Phone()
# p1.set_color("blue")
# p1.set_cost("999")
# print(p1.show_color())
# print(p1.show_cost())


# class Employee:
#     def __init__(self, name, age, salary, gender):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.gender = gender

#     def show_employee_details(self):
#         print("Name of the employee is", self.name)
#         print("Age of the employee is", self.age)
#         print("Salary of the employee is", self.salary)
#         print("Gender of the employee is", self.gender)


#     def e1(self):
#         print("You are excellent employee.")

# e1 = Employee("Saad", 24, 6000, "Male")
# e1.show_employee_details()
# e1.e1()


# class Vehicle:

#     def __init__(self, mileage, cost):
#         self.mileage = mileage
#         self.cost = cost

#     def show_vehicle(self):
#         print("I'm a vehicle")
#         print("Mileage of vehicle is", self.mileage)
#         print("Cost of vehicle", self.cost)

# class V8(Vehicle):
#     def __init__(self, mileage, cost, tyres, hp):
#         super().__init__(mileage, cost)
#         self.typres = tyres
#         self.hp = hp

#     def details(self):
#         print("I am a Car")
#         print("The number of tyres are", self.typres)
#         print("The horse power is", self.hp)

#     def brand(self):
#         print("toyota")

# v1 = V8(44, 100, 500, 600)
# v1.show_vehicle()
# v1.brand()
# v1.details()


#Multiple inheritance

# class Parent1():
#     def assign_str_one(self,str1):
#         self.str1 = str1

#     def show_str_one(self):
#         return self.str1

# class Parent2():
#     def assign_str_two(self,str2):
#         self.str2 = str2

#     def show_str_two(self):
#         return self.str2
    

# class Child(Parent1, Parent2):
#     def assign_str_three(self, str3):
#         self.str3 = str3

#     def show_three(self):
#         return self.str3
    

# child1 = Child()
# child1.assign_str_one("one")
# child1.assign_str_two("Two")
# child1.assign_str_three("Three")

# print(child1.show_str_one()) 
# print(child1.show_str_two()) 
# print(child1.show_three()) 


#Mutilevel Inheritance
class Parant():
    def assign_name(self, name):
        self.name = name

    def show_name(self):
        return self.name
    

class Child(Parant):
    def assign_age(self, age):
        self.age = age

    def show_age(self):
        return self.age
    
class GrandChild(Child):
    def assign_gender(self,gender):
        self.gender = gender

    def show_gender(self):
        return self.gender

g1 = GrandChild()
g1.assign_gender("male")
g1.assign_name("Ali")
g1.assign_age(42)

print(g1.show_name())
print(g1.show_age())
print(g1.show_gender())
