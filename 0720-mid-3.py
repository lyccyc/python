def black_hole_number(num):
    results = [num]
    while True:
        # 轉換成字符串，方便處理每一位數

        num_str = str(num).zfill(6)

        # 將位數由大到小排序
        num_desc = int("".join(sorted(num_str, reverse=True)))

        # 將位數由小到大排序
        num_asc = int("".join(sorted(num_str)))

        # 計算兩者的差異
        num = num_desc - num_asc

        # 將計算結果添加到結果列表中
        results.append(num)

        # 檢查是否達到循環的結果
        if num in {631764, 549945, 420876}:
            return results


if __name__ == "__main__":
    num = 12345
    print(black_hole_number(num))
