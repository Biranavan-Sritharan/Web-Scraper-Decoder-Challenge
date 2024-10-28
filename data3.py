import numpy as np

#ok the coords given work on the traditonal graph layout, cartesian or whatever
#the coords i use have the 0,0 axis in the top left corner similar to how pygame coords work
#but unlike pygame, I have y going horizontally and x going downwards
#but a quick rot90 fixes all that

# Define the coordinates and characters in a list of tuples
data = [
    (0, '█', 0),
    (0, '█', 1),
    (0, '█', 2),
    (1, '▀', 1),
    (1, '▀', 2),
    (2, '▀', 1),
    (2, '▀', 2),
    (3, '▀', 2),
]

# (0, '█', 0),
# (0, '█', 1),
# (0, '█', 2),
# (1, '▀', 1),
# (1, '▀', 2),
# (2, '▀', 1),
# (2, '▀', 2),
# (3, '▀', 2),

# (0, '█', 0),
#     (0, '█', 1),
#     (0, '█', 2),
#     (2, '█', 0),
#     (1, '▀', 2),
#     (2, '█', 1),
#     (2, '█', 2),
#     (1, '▀', 0),

#initalise container array to add stuff in, basically making grid here
current_largest_x = 0
current_largest_y = 0
for x in data:
    x_coord = x[0]
    y_coord = x[2]
    if x_coord > current_largest_x:
        current_largest_x = x_coord
    if y_coord > current_largest_y:
        current_largest_y = y_coord
print()
print(current_largest_x)
print(current_largest_y)

current_largest_x += 1
current_largest_y += 1
container = np.zeros((current_largest_x, current_largest_y), dtype=str)
print(container)
# container[2][1] = 5   #container[row (up n down arrays)][col (elements in array)]
# print(container)

# some reason this flips everything
#ok correction, bascially does nothing
#adding spaces for empty elements
#correctiona gain doesnt do nothing, space everything evenly
i = 0
for x in container:
    j = 0
    for y in x:
        print("sdfa")
        print(y)
        if y == '':
            container[i][j] = ' '
        j += 1
    i += 1
print(container)

#adds the unqiue chars to array
i = 0
for x in data:
    row = x[0]
    col = x[2]
    # print(container)
    print(row)
    print(col)
    print()
    container[row][col] = x[1]
    print(container)

print(container)
print()

# np.rot90(container)
print(np.rot90(container))
print()

#more readable manner instead of array
for array_row in np.rot90(container):
    row_string = "".join([str(y) for y in array_row if y])  # Join non-empty strings
    print(row_string)




# some reason this flips everything
#ok correction, bascially does nothing
#adding spaces for empty elements
# i = 0
# for x in container:
#     j = 0
#     for y in x:
#         print("sdfa")
#         print(y)
#         if y == '':
#             container[i][j] = ' '
#         j += 1
#     i += 1
# print(container)
