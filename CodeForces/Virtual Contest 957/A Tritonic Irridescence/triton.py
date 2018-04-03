def solve(s):
    if "MM" in s or "CC" in s or "YY" in s:
        return False
    if "??" in s or "C?C" in s or "M?M" in s or "Y?Y" in s:
        return True
    if s.startswith("?") or s.endswith("?"):
        return True
    return False


input()
s = input()
print(["No", "Yes"][solve(s)])