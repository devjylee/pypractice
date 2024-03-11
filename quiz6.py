def std_weight(height, gender):
    if gender=="남자":
        weight=(height/100)*(height/100)*22
    else:
        weight=(height/100)*(height/100)*21
    print("키 {0}cm {1}의 표준 체중은 {2:.2f}kg입니다.".format(height, gender, weight))

std_weight(164,"여자")
std_weight(194,"남자")