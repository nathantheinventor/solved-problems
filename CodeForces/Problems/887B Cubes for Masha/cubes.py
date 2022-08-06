cubes = [input().split() for _ in range(int(input()))]

def canMake(s):
    if len(s) == 1:
        for cube in cubes:
            if s in cube:
                return True
        return False
    elif len(s) == 2:
        for i, cube1 in enumerate(cubes):
            if s[0] in cube1:
                for j, cube2 in enumerate(cubes):
                    if i != j and s[1] in cube2:
                        return True
        return False
    elif len(s) == 3:
        for i, cube1 in enumerate(cubes):
            if s[0] in cube1:
                for j, cube2 in enumerate(cubes):
                    if i != j and s[1] in cube2:
                        for k, cube3 in enumerate(cubes):
                            if i != k and j != k and s[2] in cube3:
                                return True
        return False

if not canMake("1"):
    print(0)
else:
    for i in range(1, 1000):
        if not canMake(str(i)):
            print(i - 1)
            break