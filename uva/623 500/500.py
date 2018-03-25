facts = [1]
tmp = 1
for i in range(1, 1002):
    tmp *= i
    facts.append(tmp)

n = int(input())
while True:
    print("{}!".format(n))
    print(facts[n])
    
    try:
        n = int(input())
    except:
        break