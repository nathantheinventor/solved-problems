import re

consonants = "bcdfghjklmnpqrstvwxz"
vowels = "aeiou"
alphabet = "abcdefghijklmnopqrstuvwxyz"

def matches(pattern: str, word: str) -> bool:
    pattern = pattern.replace("*", ".*")
    pattern = pattern.replace("v", "[aeiouy]")
    pattern = pattern.replace("c", "[{}]".format(consonants))
    return re.match(pattern, word)

def syllables(word: str) -> int:
    word = word.lower()
    if "yy" in word:
        print(10 / 0)
    while word != "" and word[-1] not in alphabet:
        word = word[:-1]
    for c in word:
        if c not in alphabet:
            return 10 / 0
    if word == "":
        return 1
    if word[-1] == "e":
        if not matches("*cle", word):
            word = word[:-1]
    elif word[-2:] == "es":
        if not matches("*cces", word):
            word = word[:-2]
    word = word.replace("qu", "q")
    for c in consonants:
        word = word.replace(c, "c")
    for v in vowels:
        word = word.replace(v, "v")
    word = word.replace("yv", "cv")
    word = word.replace("y", "v")
    while "cc" in word:
        word = word.replace("cc", "c")
    while "vv" in word:
        word = word.replace("vv", "v")
    re.sub("v+", )
    return max(1, word.count("v"))

def flow(s: str) -> str:
    lines = [[], [], []]
    syls = [0, 0, 0]
    goal = [5, 7, 5]
    for word in s.split():
        syl = syllables(word)
        line = 0 if syls[0] < 5 else 1 if syls[1] < 7 else 2
        if syls[line] + syl <= goal[line]:
            syls[line] += syl
            lines[line].append(word)
        else:
            return s
    if syls == goal:
        return "\n".join(map(lambda line: " ".join(line), lines))
    return s

print(flow(input().strip()))
