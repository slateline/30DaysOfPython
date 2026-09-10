# Day 2: 30 Days of Python Programming
firstname = "Chung"
lastname = "Truong"
fullname = "Chung Truong"
country = "Canada"
city = "Vancouver"
age = "20"
year = "2026"
is_married = False
is_true = True
is_light_on = True
var1, var2, var3 = "Chung", "Truong", "Canada"

print(type(firstname))
print(type(lastname))
print(type(fullname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(var1))
print(type(var2))
print(type(var3))

print(len(firstname))
print(len(lastname))

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
floor_division = num_one // num_two

area_of_circle = 3.14 * 30 ** 2
circum_of_circle = 2 * 3.14 * 30

input_radius = input("Enter radius: ")
area_of_circle = 3.14 * int(input_radius) ** 2
print("Area of circle:", area_of_circle)