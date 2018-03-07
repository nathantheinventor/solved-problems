dial, first, second, last = map(int, input().split())
while (dial, first, second, last) != (0,0,0,0):
    ans = 720 # two full turns
    tmp = (dial + 40 - first) % 40
    ans += tmp * 9
    ans += 360 # 1 full turn
    tmp = (second + 40 - first) % 40
    ans += tmp * 9
    tmp = (second + 40 - last) % 40
    ans += tmp * 9
    print(ans)
    dial, first, second, last = map(int, input().split())