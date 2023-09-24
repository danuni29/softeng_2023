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
        <h2>구구단 출력하기</h2>
        <label>단 :
            <input type="text" name="dan">
        </label>
        <button type="submit">출력</button>
    </form>
    <div id="results", style="color:blue; text-decoration:underline" ></div>


<script>
function post_query() {
    $.ajax({
        type: "GET",
        url: "http://10.55.7.67:5000/gugu",
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


@app.route("/gugu")
def gugudan():
    dan = int(request.args.get('dan'))
    resp = ""
    resp += "<html>\n"
    resp += '<meta charset="utf-8">\n'
    resp += "<body>\n"
    resp += f"<h2>구구단 {dan}단</h2>\n"
    resp += "<div>\n"

    for i in range(1, 10):
        resp += f"{dan:2d} * {i:2d} = {dan * i:3d}<br>\n"
    resp += "</div>\n"
    resp += "</body>\n"
    resp += "</html>\n"


    return resp

app.run(host="0.0.0.0")