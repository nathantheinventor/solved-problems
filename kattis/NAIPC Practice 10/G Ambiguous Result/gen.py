import random
for _ in range(1500):
    tmp = str(random.randint(0,5))
    for _ in range(99):
        tmp += random.choice(["*", "+"])
        tmp += str(random.randint(0,5))
    print(tmp)
print("END")