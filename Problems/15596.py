#정수 N개의 합
def solve(a):
    ans = 0
    for i in range(len(a)):
        ans += a[i]
    return ans

#sum함수 이용 가능
#def solve(a):
    #return sum(a)