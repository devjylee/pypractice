# for report_num in range(1, 51):
#     report_file=open(str(report_num)+"주차.txt", "w", encoding="utf8")
#     print("- "+str(report_num)+"주차 주간보고 -", file=report_file)
#     print("부서: ", file=report_file)
#     print("이름: ", file=report_file)
#     print("업무요약: ", file=report_file)
#     report_file.close()

for report_num in range(1, 51):
    with open(str(report_num)+"주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0}주차 주간보고 -".format(report_num))
        report_file.write("\n부서: ")
        report_file.write("\n이름: ")
        report_file.write("\n업무요약: ")