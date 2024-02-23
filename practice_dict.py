cabinet = {3: "유재석", 100: "정준하"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# print(cabinet[5])     # error 이후 내용 출력하지 않음
print(cabinet.get(5))   # None이 표시된 후 이후 내용 출력
print(cabinet.get(5, "사용 가능"))
print("hi")

print(3 in cabinet)     # True
print(5 in cabinet)     # False

cabinet = {"A-3": "유재석", "B-100": "정준하"}
print(cabinet["A-3"])
print(cabinet["B-100"])

print(cabinet)
cabinet["A-3"]="김종국"
cabinet["C-20"]="조세호"
print(cabinet)

# 삭제
del cabinet["A-3"]
print(cabinet)

# key값만 출력
print(cabinet.keys())

# value값만 출력
print(cabinet.values())

# key, value 한쌍으로 출력
print(cabinet.items())

# 비우기
cabinet.clear()
print(cabinet)