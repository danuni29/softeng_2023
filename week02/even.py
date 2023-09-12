def eun_neun(num):

    num_dic = {
        0: "은", 1: "은", 2: "는", 3: "은", 4: "는", 5: "는", 6: "은", 7: "은", 8: "은", 9: "는",
    }

    return num_dic[num]

# num이 한자리 이상일때 ... 생각해야될듯..

def main():
    num = int(input("숫자를 입력하세요"))


    if num % 2 == 0:
        # if num % 10 == 2 or num % 10 == 4 or num % 10 ==5
        if num % 10 in [2, 4, 5, 9]:     # 는
            print(f"{num}는 짝수입니다")
        else:
            print(f"{num}은 짝수입니다")    # 은
    else:
        if num % 10 in [2, 4, 5, 9]:
            print(f"{num}는 홀수입니다")
        else:
            print(f"{num}은 홀수입니다")



if __name__ == '__main__':
    main()