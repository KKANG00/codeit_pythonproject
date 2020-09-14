from random import randint


def generate_numbers(n):
    # 지난 과제의 코드를 붙여 넣으세요.
    numbers = []

    for i in range(0, n):

        newnum = randint(1, 45)
        while newnum in numbers:
            newnum = randint(1, 45)

        numbers.append(newnum)

    return numbers


def draw_winning_numbers():
    # 코드를 작성하세요.
    randomnumbers = sorted(generate_numbers(6))

    bonus = randint(1, 45)
    while bonus in randomnumbers:
        bonus = randint(1, 45)

    randomnumbers.append(bonus)

    return randomnumbers


print(draw_winning_numbers())


def count_matching_numbers(list_1, list_2):
    # 코드를 작성하세요.
    cnt = 0
    for i in range(0, len(list_1)):
        if list_1[i] in list_2:
            cnt += 1

    return cnt


def check(numbers, winning_numbers):
    # 코드를 작성하세요.
    matching = count_matching_numbers(numbers, winning_numbers[:6])
    bounus = count_matching_numbers(numbers, winning_numbers[6:])

    if matching == 6:
        return 1000000000
    elif matching == 5 and bounus == 1:
        return 50000000
    elif matching == 5:
        return 1000000
    elif matching == 4:
        return 50000
    elif matching == 3:
        return 5000


# 테스트
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))