L = ['bob','cat','spam','programmers']

print(L)

print(L[1]) #인덱스 번호


# 리스트(배열) 연산.01

#1. 원소 덧붙이기
L.append('New')

print(L)

#2. 끝에 있는 원소 꺼내기
L.pop()

print(L)

# 리스트(배열) 연산.02
#리스트가 커지면 그에 따른 시간도 늘어날 떄

#예1) 원소 삽입하기

M = [20, 37, 58, 72, 91]

M.insert(3,65) #(인덱스번호,추가할 원소)

print(M)

#예2) 원소 삭제하기

del(M[2])

print(M)


# 리스트(배열) 연산.03
# 원소 탐색하기

P = ['bob','cat','spam','programmers']

print(P.index('spam'))




