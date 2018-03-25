facts = ["1"]
tmp = 1
for i in range(1, 1002):
    tmp *= i
    facts.append(str(tmp))

n = int(input())
while n > 0:
    print("{}! --".format(n))
    print("   (0){: >5}    (1){: >5}    (2){: >5}    (3){: >5}    (4){: >5}".format(*[facts[n].count(str(x)) for x in range(5)]))
    print("   (5){: >5}    (6){: >5}    (7){: >5}    (8){: >5}    (9){: >5}".format(*[facts[n].count(str(x)) for x in range(5, 10)]))
    
    n = int(input())
