def encrypt(msg, letter):
    diff = ord(letter) - ord("a")
    ans = ""
    for c in msg:
        tmp = ord(c) - ord("a")
        tmp += diff
        tmp %= 26
        ans += chr(tmp + ord("a"))
    return ans

for _ in range(int(input())):
    cypher = input().split()
    plain = input()
    ans = ""
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if encrypt(plain, letter) in cypher:
            ans += letter
    print(ans)