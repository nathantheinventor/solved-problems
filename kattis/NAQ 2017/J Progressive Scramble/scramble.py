def myord(ch):
    if ch == ' ':
        return 0
    else:
        return ord(ch) - ord('a') + 1

def mychr(ch):
    if ch == 0:
        return ' '
    else:
        return chr(ch + ord('a') - 1)

for _ in range(int(input())):
    data = input()
    type = data[0]
    data = [myord(x) for x in data[2:]]
    if type == 'e':
        for i in range(1, len(data)):
            data[i] += data[i - 1]
        for i in range(len(data)):
            data[i] = data[i] % 27
    else:
        for i in range(1, len(data)):
            while data[i] < data[i - 1]:
                data[i] += 27
        for i in range(len(data) - 1, 0, -1):
            data[i] -= data[i - 1]
    data = [mychr(x) for x in data]
    print(''.join(data))