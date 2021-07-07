# 알파벳 찾기

S = input()
alphabet = list(range(97, 123))

for i in alphabet:
    print(S.find(chr(i)), end=" ")

###########################################
# 알파벳 찾기_2

S = list(input())
alphabet = list("abcdefghijklmnopqrstuvwxyz")
result = []

for i in range(len(alphabet)):
    if alphabet[i] in S:
        result.insert(i, S.index(alphabet[i]))
    else:
        result.insert(i, -1)

for i in result:
    print(i, end=" ")

###########################################
# 알파벳 찾기_3
s = input()

a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in a:
    for j in range(len(s)):
        if (i == s[j]):
            print(j, end=' ')
            break
    if(i not in s):
        print(-1, end=' ')
