import re

for _ in range(int(input())):
    s = input()
    if len(re.findall("^\\?\\?*M\\?\\?*E\\?\\?*$", s)) != 0:
        x = s.index("M")
        y = s.index("E") - x - 1
        z = len(s) - y - x - 2
        if x + y == z and x > 0 and y > 0:
            print("theorem")
        else:
            print("no-theorem")
    else:
        print("no-theorem")