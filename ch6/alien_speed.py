alien_0 = {'x_pos': 0, 'y_pos': 25, 'color': 'yellow', 'speed': 'medium'}
print(f"Original position: {alien_0['x_pos']}")

#move the alien to the right
#determine how far to move based on current speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#the new position is the old position + the increment
# you have to store it in the dict here else it won't be saved
alien_0['x_pos'] = alien_0['x_pos'] + x_increment
print(alien_0['x_pos'])