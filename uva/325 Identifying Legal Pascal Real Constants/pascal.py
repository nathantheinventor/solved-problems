import re

s = input().strip()
while s != "*":
    if re.match("^[+-]?[0-9]+(\\.[0-9]+)?([eE][+-]?[0-9]+)?$", s):
        if "e" not in s and "E" not in s and "." not in s:
            print(s,"is illegal.")
        else:
            print(s,"is legal.")
    else:
        print(s,"is illegal.")
    s = input().strip()