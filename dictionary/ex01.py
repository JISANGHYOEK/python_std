#이름 : 홍길동, 생일 : 5월20일
#연관배열 or 해시
#KEY : VALUE / 딕셔너리는 KEY값 기준
a = {'이름' : '홍길동', '생일' : '5월 15일', '성별' : '남자', '사는 곳' : '수월', '핸드폰번호' : '01012345678', '혈액형' : 'A형'}

print(a)
print('이름' in a)
print('홍길동' in a)

print(a['이름'])
a['이름'] = '지상혁'
print(a['이름'])

a['이상형'] = '장원영'
print(a)

del a['핸드폰번호']
print(a)

print("---------------------------------")

print(a.keys())
print(a.values())
print(a.items())