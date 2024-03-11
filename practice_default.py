# def profile(name, age, main_lang):
#     print("이름: {0}\t 나이: {1}\t 주 사용언어:{2}"\
#           .format(name, age, main_lang))
    
# profile("농담곰", 20, "파이썬")
# profile("퍼그", 25, "자바")

def profile(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t 나이: {1}\t 주 사용언어:{2}"\
          .format(name, age, main_lang))
    
profile("농담곰")
profile("퍼그")

