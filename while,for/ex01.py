#while : 조건이 맞으면 반복 // 내가 몇 번 반복해야할 지 모를 때
#for : 내가 요청한 만큼 순서대로 반복 // 내가 몇 번 반복해야하는지 알 때

#while 조건:

hit = 0
while hit < 10:
    hit += 1
    print(f"나무를 {hit}번 찍었습니다.")
    if hit == 10:
        print("나무가 쓰러졌습니다.")