from rich import print
from hw03.hw03_gui_ex import simple_gui_input

def fact(num):
    if num == 1:
        return 1


    # fact_result = 1
    # for i in range(1, num+1):
    #     fact_result = fact_result * i

    return num * fact(num-1)   # 재귀함수


def main():
    num = int(simple_gui_input("숫자를 입력하세요: "))

    print(f"[b red]{num}![/b red] 은 [b cyan]{fact(num)}[/b cyan] 입니다")

if __name__ == '__main__':
    main()