
import random


def binary_search(k):
    high = 100
    middle = 0
    low = 0

    while low <= high:
        middle = (high+low)//2
        if middle == k:
            return middle
        elif middle > k:
            high = middle - 1
        elif middle < k:
            low = middle + 1


num = random.randint(1, 101)
if num == binary_search(num):
    print("성공")
