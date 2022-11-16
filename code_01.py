import time

n = int(input("Number of element:")) #원소의 갯수 입력
haystack = [k for k in range(n)] #리스트의 길이

print("Searching for the maximum value...")

# 최대 값을 찾아내는 데 소요되는 시간을 표현하는 코드 
ts = time.time()
maximum = max(haystack)
elapsed = time.time() - ts

print("Maximum element = %d, Elapsed time = %.2f" % (maximum, elapsed)) 
# %f 실수(float)
# %d 정수(int)
# %s 문자열(str)

