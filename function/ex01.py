#미리 만들어 놓고 나중에 필요할 때 가져다 쓰기 위해 만들어진 기능

#def 함수 이름(재료):

def add(a, b):
    return a + b

print(add(3,5))

print("--------------------------------------------------------")

def intro(name, age, sex = 5):
    print(f"나의 이름은 {name}이고 나이는 {age}살 입니다.")
    if sex == 5:
        print("그리고 저는 남자입니다.")
    else:
        print("그리고 저는 여자입니다.")

intro("지상혁", 23)