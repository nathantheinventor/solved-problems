def hash(s:str) -> int:
    ans = 0
    for i, c in enumerate(s[::-1]):
        ans += (i + 1) ** 7 * ord(c)
    return ans

print(hash("azzb"), hash("bazz"))