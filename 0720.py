def max_number(num: int):  # 數字由大到小
    s_num = str(num).zfill(4)  # 把數字變字串 位數永遠是4位
    r_num = ""  # 空字串暫存答案
    for i in range(4):
        r_num += max(s_num)
        s_num = s_num.replace(max(s_num), "", 1)  # 用max找出最小的數字,丟掉空字串r_num
    return int(r_num)


def min_number(num: int):  # 數字由小到大
    s_num = str(num).zfill(4)  # 把數字變字串 位數永遠是4位
    r_num = ""  # 空字串暫存答案
    for i in range(4):
        r_num += min(s_num)
        s_num = s_num.replace(min(s_num), "", 1)  # 用min找出最小的數字,丟掉空字串r_num
    return int(r_num)


def black_hole_number(num: int):
    answers = []  # 用於儲存答案
    answers.append(num)  # 把num塞到answers裡面
    while num != 6174 and num != 0:
        l_number = min_number(num)
        b_number = max_number(num)
        ans = b_number - l_number
        answers.append(ans)  # 將答案加入陣列中
        num = ans
    return answers  # 將答案return


if __name__ == "__main__":
    print(black_hole_number(123))  # <-- return 到這邊！
