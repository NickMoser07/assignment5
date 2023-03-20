def distance(x1, y1, x2, y2):
    return (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
print(distance(0, 0, 0, 5))
one_name = input("what is your name:  ")
one_pos = input("Enter your position x,y: ")
onex, oney = map(int, one_pos.split(','))
onex, oney = ((onex,oney))
one_space = int(input("what is your personal space"))

two_name = input("what is your name:  ")
two_pos = input("Enter your position x,y: ")
twox, twoy = map(int, two_pos.split(','))
twox, twoy = ((twox,twoy))
two_space = int(input("what is your personal space"))

print("Social Situation Analysis Results\n")

