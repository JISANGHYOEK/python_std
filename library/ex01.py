#전세계 파이썬 사용자들이 만든 유용한 프로그램들을 모아놓은 곳
#클래스 : 붕어빵을 만드는 틀 (함수와 변수들을 모아놓은 주머니)

class Bank:
    #권한을 받을 때 자동으로 실행되는 함수
    def __init__(self):
        self.money = 0
    #함수 재료 첫번째 self
    def deposit(self, a):
        self.money += a

person1 = Bank() #person1은 Bank클래스에서 제공하는 모든 서비스를 이용할 수 있는 권한
person1.deposit(50000)
person2 = Bank()
person2.deposit(30000)

print(person1.money)
print(person2.money)

person3 = Bank()
print(person3.money)

class Bank2(Bank): #Bank2는 Bank에서 제공하는 모든 서비를 상속받는다
    pass

pserson4 = Bank2()
print(pserson4.money)

#라이브러리를 이용하여 클래스를 가져옴