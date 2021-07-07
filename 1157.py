# 단어 공부

word = input().upper()

alphabet = {}  # 딕셔너리

for i in word:
    if i in alphabet:
        alphabet[i] += 1

    else:
        alphabet[i] = 1
result = []
for key, value in alphabet.items():
    if value == max(alphabet.values()):
        result.append(key)

if len(result) >= 2:
    print("?")

else:
    print(result[0])

############################################
# 단어 공부_2
# from collections import Counter

a = dict(Counter(input().upper()))
result = []
for i in a.keys():
    if a[i] == max(a.values()):
        result.append(i)

if len(result) > 1:
    print("?")
else:
    print(result[0])
