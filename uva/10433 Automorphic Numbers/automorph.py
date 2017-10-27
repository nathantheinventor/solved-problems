n = input()
while True:
    if str(int(n) ** 2).endswith(n):
        print("Automorphic number of {}-digit.".format(len(n)))
    else:
        print("Not an Automorphic number.")
    
    try:
        n = input()
    except:
        exit(0)