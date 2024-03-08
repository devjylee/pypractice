from random import *

# 승객 50명
# 소요시간 5~50분
# 5~15분 사이의 승객만 매칭

# [O] 1번째 손님(소요시간: 15분)
# [X] 2번째 손님(소요시간: 50분)
# [O] 3번째 손님(소요시간: 5분)
# ...
# [X] 50번째 손님(소요시간: 16분)
# 총 탑승 승객: 2

cnt = 0 #총 탑승 승객수
for i in range(1,51):
    time = randint(5,51)
    if 5<= time <=15:
        ok="O"
        cnt=+1
    else:
        ok="X" 
    print("[{0}] {1}번째 손님(소요시간: {2}분)".format(ok,i,time))
print("총 탑승 승객:{0}".format(cnt))