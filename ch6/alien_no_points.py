alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points']) this fails because there is no value: points

point_value = alien_0.get('points', 'No point value assigned')
print(point_value)