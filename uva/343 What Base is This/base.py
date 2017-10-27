a, b = input().strip().split()
while True:
    
    for i in range(2, 37):
        for j in range(2, 37):
            try:
                if int(a, i) == int(b, j):
                    print("{} (base {}) = {} (base {})".format(a, i, b, j))
                    break
            except:
                pass
        else:
            continue
        break
    else:
        print("{} is not equal to {} in any base 2..36".format(a, b))
            
    
    try:
        a, b = input().strip().split()
    except:
        exit(0)