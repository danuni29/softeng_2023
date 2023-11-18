import requests

def main():

    URL = "https://sobi.chonbuk.ac.kr/function/ajax.get.rest.data.php"
    data = {"code": "mobile3"}
    with open("cafeteria_menu.html", "w", encoding="UTF-8") as f:
        res = requests.post(URL, data=data)
        res.encoding = "UTF-8"
        additional_html = """<!DOCTYPE html>
        <html lang="kr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                  content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
        </head>"""
        f.write(res.text + "\n")


if __name__ == '__main__':
    main()