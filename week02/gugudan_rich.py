from rich.panel import Panel
from rich import print
def main():
    dan = 19

    # for i in range(1, 10):
        # print(f"{dan:2d} * {i:2d} = [bold magenta]{dan * i:3d}[/bold magenta]")
    print(Panel.fit(f"구구단 [red]{dan}단!", border_style="red"))
    print(Panel.fit("\n".join(["{} * {} = {}".format(dan, i + 1, dan * (i + 1))
                               for i in range(1, 10)])))



if __name__ == '__main__':
    main()