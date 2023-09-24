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
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <title>Document</title>
</head>
<body>
    <form id="form_id" action="javascript:post_query()">
        <h2>소수인지 판별해드립니다.</h2>
        <label>숫자를 입력하세요 :
            <input type="text" name="num">
        </label>
        <button type="submit">출력</button>
    </form>
    <div id="results", style="color:blue; text-decoration:underline" ></div>


<script>
function post_query() {
    $.ajax({
        type: "GET",
        url: "http://192.168.0.28:5000/is_prime",
        data: $("#form_id").serialize(),  <!--id는 #으로 시작-->
        success: update_result,
        dataType: "html"
});
}
function update_result(data) {
    $("#results").html(data);
}

</script>
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