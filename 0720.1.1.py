def black_hole_number(num: int):
    answer = []
    answer.append(num)
    while num != 0 or num != 6174:
        if num == 6174:
            return answer
        a = []
        max = 0
        min = 0
        for i in range(4):
            b = num % 10
            a.append(str(b))
            num = int(num // 10)
            list1 = sorted(a, reverse=False)  # 小到大
            list2 = sorted(a, reverse=True)  # 大到小

        for i in range(4):
            max = max * 10 + int(list2[i])
            min = min * 10 + int(list1[i])
        ans = max - min
        answer.append(ans)
        num = ans

        if num == 6174:
            return answer
            break


if __name__ == "__main__":
    print(black_hole_number(1234))  # <-- return 到這邊！
