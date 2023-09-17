def main():
    dan = 19

    filename = "./index.html"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("<html>\n")
        f.write('<meta charset="utf-8">\n')
        f.write("<body>\n")
        f.write(f"<h2>구구단 {dan}단</h2>\n")
        f.write("<div>\n")

        for i in range(1, 10):
            f.write(f"{dan:2d} * {i:2d} = {dan * i:3d}<br>\n")

        f.write("</div>\n")
        f.write("</body>\n")
        f.write("</html>\n")

if __name__ == '__main__':
    main()