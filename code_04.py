L = [20, 37, 58, 72, 91]

x = 65

def solution(L, x):
    answer = []
    for i in range(len(L)):
        if L[i]>x:
            L.insert(i,x)
            break
        if L[len(L)-1] < x:
            L.append(x)
    answer= L
    return answer



