# 입력으로 1개의 정수 N 이 주어진다.
# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

# [제약사항]
# N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)

# [입력]
# 입력으로 정수 N 이 주어진다.

# [출력]
# 정수 N 의 모든 약수를 오름차순으로 출력한다.
import math

a=int(input())
alist=[]

for i in range(1,int(math.sqrt(a))+1):
    if a%i == 0:
        alist.append(i)
        alist.append(a//i)
    # print(i)

alist=sorted(alist)

for i in range(len(alist)):
    print(alist[i], end=' ')

