#부녀회장이 될테야
t = int(input())
result = []
for _ in range(t):
    k = int(input())
    n = int(input())

    people = [i+1 for i in range(n)]
    for i in range(k):
        for j in range(1, n):
            people[j] = people[j-1] + people[j]

    print(people[-1])