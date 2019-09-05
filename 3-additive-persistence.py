# [2019-01-28] Challenge #374 [Easy] Additive Persistence


def additive_persistence(number):
    i = 0
    num = [item for item in number]  # 3 1
    while len(num) > 1:
        i += 1
        num = str(sum([int(number) for number in num]))
    return i


num = additive_persistence('199')
print(num)