def distance(x1, y1, x2, y2):
    return (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
print(distance(0, 0, 0, 5))
one_name = input("what is your name:  ")
one_pos = input("Enter your position x, y: ")
onex, oney = map(int, one_pos.split(', '))
onex, oney = ((onex,oney))
one_space = int(input("what is your personal space:  "))
one_pos = (onex, oney)

two_name = input("what is your name:  ")
two_pos = input("Enter your position x, y: ")
twox, twoy = map(int, two_pos.split(', '))
twox, twoy = ((twox,twoy))
two_space = int(input("what is your personal space:  "))
two_pos = (twox, twoy)
distance = distance(onex, oney, twox, twoy)

one_in_two = distance < two_space
two_in_one = distance< one_space

space_overlap = distance < one_space + two_space

one_inside = (two_space > distance + one_space)
two_inside = (one_space > distance + two_space)
msg = ""
if one_in_two:
    msg += "person test:  " + one_name + " is in " + two_name + "'s personal space\n"
if two_in_one:
    msg += "person test:  " + two_name + " is in " + one_name + "'s personal space\n"
if space_overlap:
    msg += "space test:  both spaces overlap\n"
if one_inside:
    msg += one_name + "'s personal space is entirely inside " + two_name + "'s space\n"
if two_inside:
    msg += two_name + "'s personal space is entirely inside " + one_name + "'s space\n"
print(msg)