alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] in alphabet:
            s[i] = chr(ord(s[i]) + 3)
    s = s[::-1]
    for i in range(len(s) // 2, len(s)):
        s[i] = chr(ord(s[i]) - 1)
    return "".join(s)

for _ in range(int(input())):
    print(encrypt(input()))