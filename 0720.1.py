def black_hole_number(num: int):
    def max_number(num: int):
        s_num: str(num)
        r_num = ""
        for i in range(4):
            r_num += max(s_num)
            s_num = s_num.replace(max(s_num), "", 1)
        return int(r_num)

    def min_number(num: int):
        s_num: str(num)
        r_num = ""
        for i in range(4):
            r_num += min(s_num)
            s_num = s_num.replace(min(s_num), "", 1)
        return int(r_num)

    def cableck(num: int):
        while num != 6174 or num != 0:
            l_number = min_number(num)
            b_number = max_number(num)
            ans = b_number - l_number
            print(ans)
