from collections import deque

num = int(input())
answers = [0 for _ in range(num+1)]
queue = deque([])

for _ in range(num-1):
    n1, n2 = map(int, input().split())
    queue.append((n1,n2))

while queue:
    n1, n2 = queue.popleft()
    if n1 == 1 or answers[n1] != 0:
        answers[n2] = n1
    elif n2 == 1 or answers[n2] != 0:
        answers[n1] = n2
    else:
        queue.append((n1,n2))

for i in range(2, len(answers)):
    print(answers[i])