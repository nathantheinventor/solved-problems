input()
sentence = input().split()

correctTranslations = {w: 0 for w in sentence}
translations = {w: 0 for w in sentence}
trans = {}
for _ in range(int(input())):
    d, e, c = input().split()
    if d not in translations:
        translations[d] = 0
    translations[d] += 1
    
    if c == "correct":
        if d not in correctTranslations:
            correctTranslations[d] = 0
        correctTranslations[d] += 1
    
    trans[d] = e

totalTrans = 1
correctTrans = 1
for word in sentence:
    totalTrans *= translations[word]
    correctTrans *= correctTranslations[word]

if totalTrans == 1:
    ans = []
    for word in sentence:
        ans.append(trans[word])
    
    print(" ".join(ans))
    
    if correctTrans == 0:
        print("incorrect")
    else:
        print("correct")
else:
    print(correctTrans, "correct")
    print(totalTrans - correctTrans, "incorrect")
