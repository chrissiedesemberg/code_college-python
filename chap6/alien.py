alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
    print(f"This alien is falling further and further behind - it has a {alien_0['speed']} setting!")
elif alien_0['speed'] == 'medium':
    x_increment = 2
    print(f"This alien is goes past you, almost slowly - it has a {alien_0['speed']} setting!")
else:
# This must be a fast alien.
    x_increment = 3
    print(f"This alien is zooms past and has a {alien_0['speed']} setting!")
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

