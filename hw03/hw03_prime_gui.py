
from rich import print
from hw03.hw03_gui_ex import simple_gui_input


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def main():
    num = int(simple_gui_input("숫자를 입력하세요"))
    if is_prime(num) is True:
        print(f"{num}은 [b purple]소수입니다.[/b purple]")

    else:
        print(f"{num}은 [b purple]소수가 아닙니다.[/b purple]")

if __name__ == '__main__':
    main()