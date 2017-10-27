errors  =  " 1234567890-=wertyuiop[]\\sdfghjkl;'xcvbnm,./!@#$%^&*()_+WERTYUIOP{}|SDFGHJKL:\"XCVBNM<>?"
correct = " `1234567890-qwertyuioP[]asdfghjkL;zxcvbnM,.~!@#$%^&*()_QWERTYUIOP{}ASDFGHJKL:ZXCVBNM<>"

s = input()
while True:
    ans = ""
    for c in s:
        ans += correct[errors.index(c)]
    print(ans)
    
    try:
        s = input()
    except:
        exit(0)