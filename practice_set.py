# set
# 중복 불가, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)       # {1,2,3}

java = {"이지윤", "장정원", "임근홍"}
python = set(["이지윤", "도인선"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합잡합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

python.add("최시경")
print(python)

java.remove("장정원")
print(java)