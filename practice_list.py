subway1 = 10
subway2 = 20
subway3 = 30

# 정수 리스트
subway = [10, 20, 30]
print(subway)

# 문자열 리스트
subway = ["유재석", "조세호", "박명수"]
print(subway)

# 몇번째에 있는지 찾기
print(subway.index("조세호"))

# 뒤에 추가
subway.append("하하")
print(subway)

# 삽입
subway.insert(1, "정형돈")
print(subway)

# 뒤에서부터 꺼내기
print(subway.pop())
print(subway)

# 중복 세기
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 숫자 정렬
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 숫자 뒤집기
num_list.reverse()
print(num_list)

# 리스트 비우기
num_list.clear()
print(num_list)

# 다양한 자료형
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)