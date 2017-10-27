a, b = map(int, input().split())
instructions = [input() for _ in range(int(input()))]

def simulate(l):
    x, y = 0, 0
    dir = 90
    for i in l:
        if i == 'Left':
            dir = (dir + 90) % 360
        elif i == 'Right':
            dir = (dir - 90) % 360
        else:
            if dir == 0:
                x += 1
            elif dir == 90:
                y += 1
            elif dir == 180:
                x -= 1
            else:
                y -= 1
        #print(x, y, dir)
    return x, y

for i in range(len(instructions)):
    orig = instructions[i]
    instructions[i] = "Left"
    if simulate(instructions) == (a, b):
        print(i + 1, "Left")
        break
    instructions[i] = "Right"
    #print(simulate(instructions))
    if simulate(instructions) == (a, b):
        print(i + 1, "Right")
        break
    instructions[i] = "Forward"
    if simulate(instructions) == (a, b):
        print(i + 1, "Forward")
        break
    instructions[i] = orig