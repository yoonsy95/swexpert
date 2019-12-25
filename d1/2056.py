# 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.

# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
# 22220228 -> 2222/02/28
# ”YYYY/MM/DD”형식으로 출력하고,
# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.

# 연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
# 일은 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.

# 1월   1일 ~ 31일
# 2월   1일 ~ 28일
# 3월   1일 ~ 31일
# 4월   1일 ~ 30일
# 5월   1일 ~ 31일
# 6월   1일 ~ 30일
# 7월   1일 ~ 31일
# 8월   1일 ~ 31일
# 9월   1일 ~ 30일
# 10월  1일 ~ 31일
# 11월  1일 ~ 30일
# 12월  1일 ~ 31일

# ※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)

# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.

# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

case=int(input())


for i in range(case):
    ndate=input()
    tf=False

    if len(ndate)==8 and (int(ndate[4:6])>=1 and int(ndate[4:6])<=12):
        if (int(ndate[4:6]) in [1,3,5,7,8,10,12]) and (int(ndate[6:])>=1 and int(ndate[6:])<=31):
            tf=True
        elif (int(ndate[4:6]) in [4,6,9,11]) and (int(ndate[6:])>=1 and int(ndate[6:])<=30):
            tf=True
        elif (int(ndate[4:6]) in [2]) and (int(ndate[6:])>=1 and int(ndate[6:])<=28):
            tf=True
        
    if tf==True:
        print(f'#{i+1} {ndate[:4]}/{ndate[4:6]}/{ndate[6:]}')
    else: 
        print(f'#{i+1} -1')

