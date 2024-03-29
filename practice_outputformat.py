# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬, 10자리 공간 확보
print("{0: >10}".format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸 _로 채움
print("{0:_<10}".format(500))
# 세자리마다 콤마를 찍어주기
print("{0:,}".format(100000000000))
# 세자리마다 콤마를 찍어주기, +- 부호도 붙여주기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))
# 세자리마다 콤마를 찍어주기, 부호 추가, 자리수 확보, 빈칸 ^로 채움
print("{0:^<+30,}".format(100000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리 수까지만 표시(셋째자리에서 반올림)
print("{0:.2f}".format(5/3))

# 순서:빈자리, 정렬, 부호, 빈자리, 콤마