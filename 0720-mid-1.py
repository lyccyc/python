def get_shrimp_num(heights):
    sorted_heights = sorted(heights, reverse=True)
    n = len(heights)
    height_diff = list()
    if n % 2 == 0:
        for i in range(n // 2):
            height_diff += [sorted_heights[i] - sorted_heights[n - 1 - i]]

    else:
        del sorted_heights[n // 2]
        for i in range(n // 2):
            height_diff += [sorted_heights[i] - sorted_heights[n - 1 - i]]

    ans = sum(height_diff)
    return sorted_heights, height_diff, ans


if __name__ == "__main__":
    heights = [158, 176, 160, 175]
    print(get_shrimp_num(heights))
