#[문제]
#정수 N개로 이루어진 수열 A와 정수 X가 주어진다.
#이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

n, x = input("input N, X : ").split()
n = int(n)
x = int(x)

# listA = []
# listA = input("input list A : ").split()
listA = map(int, input("input list A : ").split())

listA = list(listA)
# for i in range(n) :
#     listA[i] = int(listA[i])

# listA = list(map(int, listA))

for i in range(n) :
    if listA[i] < x :
        print(listA[i], end = " ")
