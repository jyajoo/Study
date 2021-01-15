#알파벳 찾기

S = input()
alphabet = list(range(97, 123))

for i in alphabet:
    print(S.find(chr(i)), end = " ")

###########################################
#알파벳 찾기_2

S = list(input())
alphabet = list("abcdefghijklmnopqrstuvwxyz")
result = []

for i in range(len(alphabet)):
    if alphabet[i] in S:
        result.insert(i, S.index(alphabet[i]))
    else:
        result.insert(i, -1)

for i in result:
    print(i, end = " ")