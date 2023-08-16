#구글 검색 : python 달력

import calendar

print(calendar.calendar(2025))
print(calendar.weekday(2025, 12, 31)) #0이 월요일

print("----------------------------------------------------------------")

from calendar import weekday #calendar 라이브러리로부터 weekday 함수만 가져옴 용량 조절의 용이
from calendar import weekday as wd # weekday함수를 wd라는 이름으로 사용하겠다
print(wd(2025, 12, 31))
