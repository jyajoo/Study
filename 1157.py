#단어 찾기

word = input().upper()

alphabet = {} #딕셔너리

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