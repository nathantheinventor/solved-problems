while True:
    try:
        last = False
        ans = 0
        for c in input():
            if c in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm":
                if last == False:
                    ans += 1
                last = True
            else:
                last = False
        print(ans)
    except:
        break