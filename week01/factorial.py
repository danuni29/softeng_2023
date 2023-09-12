def fact(num):
    fact_result = 1
    for i in range(1, num+1):
        fact_result = fact_result * i

    return fact_result


def main():
    num = int(input("숫자를 입력하세요: "))

    print(f"{num}! 은 {fact(num)} 입니다")

if __name__ == '__main__':
    main()