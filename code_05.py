L = [64, 72, 83, 72, 54]
x = 72


def solution(L, x):
    answer = []
    for i in range(len(L)):
        if L[i] == x:
            answer.append(i)
        if x not in L :
            answer = [-1]
            
    
    return answer