def eun_neun(num):
    num_dic = {
        0: "은", 1: "은", 2: "는", 3: "은", 4: "는", 5: "는", 6: "은", 7: "은", 8: "은", 9: "는",
    }

    return num_dic[num]


def main():
    num = int(input("숫자를 입력하세요"))


    if num % 2 == 0:
        print(f"{num}{eun_neun(num)} 짝수입니다")
    else:
        print(f"{num}{eun_neun(num)} 홀수입니다")

# (은, 는) 구현

if __name__ == '__main__':
    main()