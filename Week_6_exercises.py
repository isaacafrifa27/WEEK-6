import math

squares = [4, 9, 16, 25]

for num in squares:
    square_root = math.sqrt(num)


    print(f"The square root of {num} is: {square_root}")




squares = [4, 9, 16, 25]

additional_squares = [49, 64, 81]

for num in additional_squares:
    squares.append(num)

print("Updated squares list:", squares)




squares = [4, 9, 16, 25, 49, 64, 81]

additional_squares = [121, 144, 169]

squares.extend(additional_squares)

print("Updated squares list:", squares)




squares = [4, 9, 16, 25, 49, 64, 81, 121, 144, 169]

squares[0:0] = [2]

print("Updated squares list:", squares)




squares = [2, 4, 9, 16, 25, 49, 64, 81, 121, 144, 169]

squares.remove(49)

print("Updated squares list:", squares)




squares = [2, 4, 9, 16, 25, 49, 64, 81, 121, 144, 169]

squares.remove(3)
print("Updated squares list:", squares)



my_list = [1, 2, 3, 4, 5, 7, 1, 2]

my_list.remove(2)

print("Updated list:", my_list)



squares = [2, 4, 9, 16, 25, 49, 64, 81, 121, 144, 169]

last_value = squares.pop()

print("Removed value:", last_value)

print("Updated squares list:", squares)



squares = [2, 4, 9, 16, 25, 49, 64, 81, 121, 144, 169]

first_value = squares.pop(0)

print("Removed value:", first_value)

print("Updated squares list:", squares)



names = ["Eric", "anna", "Sophie", "sam"]

names.sort()

print("Sorted names list:", names)



names = ["Eric", "anna", "Sophie", "sam"]

names.sort(key=lambda x: x.lower())

print("Case-insensitive sorted names list:", names)



squares = [2, 4, 9, 16, 25, 49, 64, 81, 121, 144, 169]

squares.reverse()

print("Reversed squares list:", squares)



colours = ["red", "green", "yellow", "blue", "red"]

print(colours.index("blue"))



colours = ["red", "green", "yellow", "blue", "red"]

colours_copy = colours.copy()

colours[0] = "black"
colours.append("grey")

print("Original colours list:", colours)
print("Copied colours list:", colours_copy)



cubes = [x ** 3 for x in range(2, 21)]

print("List of Cubes:", cubes)



# for a user name to be placed in the some_users list, it has to meet the condition of the name been less than 8 charaters.



house_number = 123
street = "Headingly"
postcode = "LS3 3DD"

address = (house_number, street, postcode)

print("Address:", address)



empty = ()
print("empty:", empty)
print("Type of empty:", type(empty))

the_one = "Neo",
print("the_one:", the_one)
print("Type of the_one:", type(the_one))

the_one = ("Neo")
print("the_one:", the_one)
print("Type of the_one:", type(the_one))



address = (123, "Headingly", "LS3 3DD")

house_num, street, postcode = address

print("House Number:", house_num)
print("Street:", street)
print("Postcode:", postcode)



address = (123, "Headingly", "LS3 3DD")

print("Address using '*':", *address)

print("Address without '*':", address)
