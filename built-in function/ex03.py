str(3) #string : 문자로 변환

for i in range(1, 11, 3):
    print(i)

for i in range(10, 0, -1):
    print(i)

list(range(10)) #0~9까지

round(4.6) #반올림함수

print(sorted([1,4,3,2])) #정렬

a = [1,2,3]
b = [4,5,6]

#3이상 가능
for i,j in zip(a, b):
    print(i, j)

type('abc')