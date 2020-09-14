#왜 영어만 읽히냐
with open('data/example.txt', 'r') as f:
    for line in f:
        print(line.strip())

#text에 띄어쓰기 들어가면 한 칸 띄어서 출력된다.
# strip: 문자열 앞 뒤의 white space를 제거해준다.
print("    \n      test    \n".strip())

# 'w': 덮어쓰기
# 'a': 뒤에 추가하기
#with open('data/newfile.txt', 'w') as f:
#    f.write("Hello world!\n")
#    f.write("I'm jiwoo!\n")

while True:
    with open('data/vocabulary.txt', 'a') as f:
        english = input("영어 단어를 입력하세요: ")
        if english == "q":
            break

        f.write(english + ": ")
        korean = input("한국어 뜻을 입력하세요: ")

        if korean == "q":
            break

        f.write(korean + "\n")