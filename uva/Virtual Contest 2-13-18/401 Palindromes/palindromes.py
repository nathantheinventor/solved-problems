back = {"A": "A", "M": "M", "Y": "Y", "Z": "5", "O": "O", "1": "1", "2": "S", "E": "3", "3": "E", "S": "2", "5": "Z", "H": "H", "T": "T", "I": "I", "U": "U", "J": "L", "V": "V", "8": "8", "W": "W", "X": "X", "L": "J"}

def mirror(s):
    try:
        ans = [back[c] for c in s]
        return "".join(ans[::-1])
    except:
        return ""

s = input()
while True:
    if s == s[::-1]:
        if s == mirror(s):
            print("{} -- is a mirrored palindrome.\n".format(s))
        else:
            print("{} -- is a regular palindrome.\n".format(s))
    else:
        if s == mirror(s):
            print("{} -- is a mirrored string.\n".format(s))
        else:
            print("{} -- is not a palindrome.\n".format(s))
    try:
        s = input()
    except:
        break