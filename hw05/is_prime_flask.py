from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def first_page():
    return """
<!DOCTYPE html>
<html lang="kr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form method="GET" action="/is_prime">
        <h2>소수인지 판별해드립니다~</h2>
        <label>숫자를 입력하세요 :
            <input type="text" name="num">
        </label>
        <button type="submit">출력</button>
    </form>
</body>
</html>
"""

@app.route("/is_prime")
def is_prime():
    num = int(request.args.get('num'))
    resp = ""

    if num < 2:
        if num % 10 in [2, 4, 5, 9]:     # 는
            resp += f"{num}는 소수가 아닙니다"
            return resp
        else:
            resp += f"{num}은 소수가 아닙니다"
            return resp

    for i in range(2, num):
        if num % i == 0:
            if num % 10 in [2, 4, 5, 9]:  # 는
                resp += f"{num}는 소수가 아닙니다"
                return resp
            else:
                resp += f"{num}은 소수가 아닙니다"
                return resp

    resp += f"{num}은 소수입니다"
    return resp

app.run(host="0.0.0.0")