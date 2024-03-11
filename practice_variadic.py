# 가변인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t 나이: {1}\t".format(name, age), end=" ") #end 이어서 밑에 있는 문장 출력
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름: {0}\t 나이: {1}\t".format(name, age), end=" ") #end 이어서 밑에 있는 문장 출력
    for lang in language:
        print(lang, end=" ")
    print()

profile("농담곰", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("퍼그", 25, "Kotiln", "Swift")