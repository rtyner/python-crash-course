cubes = [] # empty list to store the cubes in
for i in range(1,11): # creates your range of numbers to calculate against
    cube = i ** 3 # creates variable to store the values in the range above ^3 in
    cubes.append(cube) # appends the values^3 in the original list
print(cubes)