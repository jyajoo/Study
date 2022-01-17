#수 정렬하기 2
#? 시간초과, 수 정렬하기(2750)과 같은 코드.
n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))
num.sort()
print(*num, sep = "\n")
###################################
#수 정렬하기 2_2
import sys
n = sys.stdin.readline()
num = []
for _ in range(int(n)):
    num.append(int(sys.stdin.readline().rstrip()))

num.sort()
print(*num, sep = "\n")