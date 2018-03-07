import re

def num():
    global pos
    ans = 0
    while pos < len(string) and string[pos] in "1234567890":
        ans *= 10;
        ans += int(string[pos])
        pos += 1
    return ans

def exprMin() -> int:
    global pos
    tmp = termMin()
    if pos < len(string):
        pos += 1
        tmp += exprMin()
    return tmp

def termMin() -> int:
    global pos
    tmp = num()
    if pos < len(string) and string[pos] == "*":
        pos += 1
        tmp *= termMin()
    return tmp

def exprMax() -> int:
    global pos
    tmp = termMax()
    if pos < len(string):
        pos += 1
        tmp *= exprMax()
    return tmp

def termMax() -> int:
    global pos
    tmp = num()
    if pos < len(string) and string[pos] == "+":
        pos += 1
        tmp += termMax()
    return tmp

def trimMin(s: str) -> str:
    for _ in range(10):
        if "0" not in s or s == "0":
            break
        # handle *0*
        s = re.sub(r".*\*0\*.*", "0", s)
        
        # handle +0*
        s = re.sub(r"\+0\*.*", "", s)
        s = re.sub(r"^0\*.*", "0", s)
        
        # handle *0+
        s = re.sub(r".*\*0\+", "", s)
        s = re.sub(r".*\*0$", "0", s)
        
        # handle +0+
        s = re.sub(r"\+0\+", "+", s)
        s = re.sub(r"^0\+", "", s)
        s = re.sub(r"\+0$", "", s)
    
    # print(s)
    # assert(s == "0" or "0" not in s)
    if s == "":
        print(10//0)
        return "0"
    return s

def trimMax(s: str) -> str:
    for _ in range(10):
        if "0" not in s or s == "0":
            break
        
        # handle *0*
        s = re.sub(r"^[^+]*\*0\*[^+]*\+", "", s)
        s = re.sub(r"\+[^+]*\*0\*[^+]*$", "", s)
        s = re.sub(r"^[^+]*\*0\*[^+]*$", "0", s)
        
        # handle +0*
        s = re.sub(r"\+0\*", "*", s)
        s = re.sub(r"^0\*[^+]*\+", "", s)
        s = re.sub(r"^0\*[^+]*$", "0", s)
        
        # handle *0+
        s = re.sub(r"\*0\+", "*", s)
        s = re.sub(r"\+[^+]*\*0$", "", s)
        s = re.sub(r"^[^+]*\*0$", "0", s)
    
        # handle +0+
        s = re.sub(r"\+0\+", "+", s)
        s = re.sub(r"^0\+", "", s)
        s = re.sub(r"\+0$", "", s)
    
    if "*0*" not in s:
        global string, pos
        string = s
        pos = 0
        return str(exprMax())
    
    for _ in range(10):
        s = re.sub("\+([0-9]*)\+([0-9]*)\+", lambda x: "+{}+".format(int(x.group(1)) + int(x.group(2))), s)
        s = re.sub("^([0-9]*)\+([0-9]*)\+", lambda x: "{}+".format(int(x.group(1)) + int(x.group(2))), s)
        s = re.sub("\+([0-9]*)\+([0-9]*)$", lambda x: "+{}".format(int(x.group(1)) + int(x.group(2))), s)
        s = re.sub("\*([1-9][0-9]*)\*([1-9][0-9]*)\*", lambda x: "*{}*".format(int(x.group(1)) * int(x.group(2))), s)
        s = re.sub("^([1-9][0-9]*)\*([1-9][0-9]*)\*", lambda x: "{}*".format(int(x.group(1)) * int(x.group(2))), s)
        s = re.sub("\*([1-9][0-9]*)\*([1-9][0-9]*)$", lambda x: "*{}".format(int(x.group(1)) * int(x.group(2))), s)
    
    # print(s)
    # assert(s == "0" or "0" not in s)
    if s == "":
        print(10//0)
        return "0"
    return s

def parse(s: str):
    nums = [int(x) for x in s.replace("*", "+").split("+")]
    tmp = re.sub("[0-9]{1,}", "0", s)
    ops = tmp.split("0")[1:-1]
    assert(len(ops) == len(nums) - 1)
    return nums, ops

def solve(s):
    s = trimMax(s)
    if "*0*" in s:
        a = s.count("*0*")
        tmp = re.sub("\+[^+]*\*0\*", "*", s, 1)
        b = tmp.count("*0*")
        # print(a, b)
        assert(a>b)
        tmp2 = re.sub("\*0\*[^+]*\+", "*", s, 1)
        return max(solve(tmp), solve(tmp2))
    else:
        global string, pos
        pos = 0
        string = s
        return exprMax()

s = input()
while s != "END":
    minS = trimMin(s)
    maxS = trimMax(s)
    # print(minS, maxS)
    pos = 0
    string = minS
    minAns = exprMin()
    maxAns = solve(maxS)
    
    print(minAns, maxAns)
    s = input()