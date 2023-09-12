from rich import print
from hw03.hw03_gui_ex import simple_gui_input

def is_even(num):
    return num % 2 ==0

def main():


    evens = [x for x in range(1,101) if is_even(x)]

    print(f"1부터 100까지의 합은 [bold cyan]{sum(evens)}[/bold cyan] 입니다")

if __name__ == '__main__':
    main()