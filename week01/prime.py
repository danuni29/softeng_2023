def is_prime(num):
    divisor = []
    for i in range(1, num+1):
        if num % i == 0:
            divisor.append(i)

    if len(divisor) == 2:
        return True
    else:
        return False

def main():
    num = 3
    if is_prime(num) is True:
        print(f"{num}은 소수입니다.")

    else:
        print(f"{num}은 소수가 아닙니다.")

if __name__ == '__main__':
    main()