from random import randint


def generate_numbers():
    numbers = []

    # 코드를 작성하세요.
    for i in range(0, 3):
        newnum = randint(0, 9)
        while newnum in numbers:
            newnum = randint(0, 9)

        numbers.append(newnum)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    # 코드를 작성하세요.
    for i in range(1, 4):
        num = input("{}번째 숫자를 입력하세요: ".format(i))
        while int(num) < 0 or int(num) >= 10 or int(num) in new_guess:
            if int(num) < 0 or int(num) >= 10:
                print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")

            elif int(num) in new_guess:
                print("중복되는 숫자입니다. 다시 입력하세요.")

            num = input("{}번째 숫자를 입력하세요: ".format(i))

        new_guess.append(int(num))

    return new_guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    # 코드를 작성하세요.
    for i in range(0, len(guess)):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0
correct = False

# 코드를 작성하세요.
while not correct:
    tries += 1
    guessnums = take_guess()
    s, c = get_score(guessnums, ANSWER)

    if s == 3:
        print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
    else:
        print(str(s) + "S " + str(c) + "B")
