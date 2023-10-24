def ascii():
    words = input()
    score = 0

    x = len(words)

    for i in range(x):
        num = ord(words[i]) - ord("@")
        score += num

    return score


print(ascii())
