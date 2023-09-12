from rich import print
from hw03.hw03_gui_ex import simple_gui_input



def f2c(temp):
    return (temp - 32) * 5/9


def c2f(temp):
    return (temp * 1.8) + 32

def main():

    temp_f = int(simple_gui_input("화씨를 섭씨로 변환해드려요 \n변환할 온도를 입력하세요"))
    print(f"[bold blue]{temp_f}F => {f2c(temp_f):.1f}℃[/bold blue]", ":fire:")



    temp_c = int(simple_gui_input("섭씨를 화씨로 변환해드려요 \n변환할 온도를 입력하세요"))
    print(f"[bold blue]{temp_c}℃ => {c2f(temp_c):.1f}F[/bold blue]", ":fire:")



if __name__ == '__main__':
    main()