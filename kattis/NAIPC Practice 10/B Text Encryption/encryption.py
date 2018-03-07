n = int(input())
while n > 0:
    s = input()
    s = "".join(s.split()).upper()
    sizes = [0 for _ in range(n)]
    for i in range(len(s)):
        sizes[i % n] += 1
    
    pos = 0
    parts = []
    for size in sizes:
        parts.append(s[pos:pos+size] + " ")
        pos += size
    
    print("".join(map("".join,zip(*parts))).replace(" ", ""))
    
    n = int(input())