# 쓰기(덮어쓰기)
score_file=open("score.txt", "w", encoding="utf8")
print("수학: 0", file=score_file)
print("영어: 50", file=score_file)
score_file.close()

# 이어쓰기
score_file=open("score.txt", "a", encoding="utf8")
score_file.write("과학: 80")
score_file.write("\n코딩: 100")
score_file.close()

# 읽기
score_file=open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

# 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
score_file=open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline())
score_file.close()

# 줄이 없을 떄까지 읽기
score_file=open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

# 리스트 형태로 저장
score_file=open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()