import random

# 코드를 작성하세요.

answer = random.randint(1, 20)
guess = 0

for i in range(4, 0, -1):
    guess = input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: ".format(i))
    if int(guess)>answer:
        print("Down")
    elif int(guess)<answer:
        print("Up")
    else:
        print("축하합니다. {}번만에 숫자을 맞추셨습니다.".format(4-i))

if guess!=answer:
    print("아쉽습니다. 정답은 {}였습니다.".format(answer))