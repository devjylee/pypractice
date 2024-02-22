domain="http://www.naver.com"

index=domain.index(".")
index2=domain.index(".",index+1)
pwd=domain[index+1:index2]
pwd=pwd[0:3]+str(len(pwd))+str(pwd.count("e"))+"!"
print(pwd)