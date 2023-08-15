#문자열 전용함수
#문자열.함수이름()

print("I eat {} apples".format(3))
print("I eat {} apples and {} oranges".format(3,5))

print("-----------------------------------------")

a = 'python is too fun'

print(a.count('o'))
print(a.find('i')) #a에서 i가 어디에 있는지
print(a.find('z'))

print(".".join('abcde'))

print("-----------------------------------------")

b = '     hello     '
print(b.lstrip())
print(b.rstrip())
print(a.replace("python","java"))
print(a.split()) #리스트 : 데이터를 모아놓는 곳

c = "python:is:too:fun"
print(c.split(':'))
