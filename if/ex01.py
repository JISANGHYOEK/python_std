#if 조건
money = True

#항상 if와 else를 같이 쓸 필요는 없다.
#if문 아래에 elif문은 무한대로 사용할 수 있다.

if money == True:
    print("taxi")
else:
    print("walk")

money = 2000
card = 1

if money >= 3000 or card == 1:
    print("taxi")
else:
    print("walk")

box = ['paper', 'cellphone', ' money']

if 'money' in box:
    print("taxi")
elif card == 1:
    print("taxi")
else:
    print("walk")