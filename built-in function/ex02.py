#프로그래밍 -> 결과물(word, ppt, text, excel)

f = open('test.txt', 'wt') #write txt 새롭게 작성(wt), attach text 이어서 작성(at)

for i in range(1, 11):
    f.write(f"{i}번째줄입니다.\n")

f.close()

f = open('test.txt', 'rt') #read txt 읽기(rt)
data = f.read()
f.close()

print(data)