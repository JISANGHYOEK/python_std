a = [1,2,3,4,5]
print(a[0])
print(a[-1])
print(a[3])

print("--------------------------------")

a = [1,2,3]
b = [4,5,6]

print(a + b)

print(a * 3)
print(len(a))

print("--------------------------------")

a[1]=8 #a에 첫번째에 8을 넣어라
print(a)

#데이터 삭제, 리스트 전용함수 or 키워드
a = [1,2,3,4,5]
del a[1]
print(a)

del a[2:]
print(a)

print("--------------------------------")

a = [1,3,5,4,2]
a.append(10)
print(a)

a.insert(0, 50)
print(a)

print("--------------------------------")
a = [1,3,5,4,2]
a.sort() #정렬
print(a)
a.reverse() #거꾸로
print(a)

print(a.index(1)) #위치 값 찾기

print("--------------------------------")

a = [1,3,5,4,2]
a.remove(5) #a에서 5를 삭제
print(a)

print("--------------------------------")
a = [1,2,3,4,5]
z = a.pop(0) #꺼내는 함수
print(a)
print(z)