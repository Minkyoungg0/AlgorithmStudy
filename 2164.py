from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

arr = [(i+1) for i in range(N)]
arr = deque(arr)
while len(arr) > 1:
    arr.popleft()          # 첫 번째 카드 버림
    tmp = arr.popleft()
    arr.append(tmp)  # 그 다음 카드를 맨 뒤로 보냄

print(*arr)

# while (True):
#     if len(arr) == 1:
#         break
#     arr = deque(arr)
#     arr.popleft() # 첫 번째 제거
#     tmp = arr[0]
#     for i in range(len(arr)-1):
#         arr[i] = arr[i+1]
#     arr[-1] = tmp

