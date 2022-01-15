from random import randint
import time


# 배열에 10,000개의 정수 삽입
arr = []
for _ in range(10000):
    arr.append(randint(1, 100))  # 1부터 100 사이의 랜덤 정수

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(arr)):
    min_index = i         # 가장 작은 인덱스
    for j in range(i + 1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]   # 스와이프

end_time = time.time()
print("선택 정렬 성능 측정 : ", end_time - start_time)

# 배열을 다시 무작위 데이터로 초기화
arr = []
for _ in range(10000):
    arr.append(randint(1, 100))

# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
arr.sort()

end_time = time.time()
print("기본 정렬 라이브러리 성능 측정 : ", end_time - start_time)
