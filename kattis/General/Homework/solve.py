ans = 0
for section in input().split(";"):
    if "-" in section:
        a, b = map(int, section.split("-"))
        ans += b - a + 1
    else:
        ans += 1
print(ans)
