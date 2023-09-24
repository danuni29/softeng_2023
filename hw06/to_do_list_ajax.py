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
        <title>ToDoList</title>
        <style>
            body { background: #358; color: #fff; padding: 50px; font-family: sans-serif; }
            a { color: #fff; font-size: 40px; }

            section {
                width: 800px;
                margin: 0px auto;
            }

            .task {
                width: 400px;
            }

            .strikeout {
                text-decoration: line-through;
            }
        </style>
        <script type="text/javascript" src="http://code.jquery.com/jquery-1.11.1.min.js"></script>        
    </head>
    <body>

        <section>
            <h1>To do app</h1>

            <form>
                <input type="text" id="task" />
            </form>

            <div id="tasks">
            </div>

            <div id="done">
                <h3>Finished tasks</h3>

            </div>
        </section>

        <script>


            $('form').on('submit', function(e) {
                e.preventDefault();

                var newtask = $('#task').val();
                var task_elem = $('<div>')
                    .append('<input type="checkbox">')
                    .addClass('task')
                    .append(newtask);
                $('#tasks').append(task_elem);

                $.ajax({
                    url: '/',
                    method: 'post',
                    dataType: 'json',
                    data: {
                        task: newtask,
                    },
                    success: function(response) {
                        console.log(response);
                        console.log(JSON.stringify(response));
                    },
                });

            });
        
            $('body').on('click', 'input[type="checkbox"]', function() {
                var task = $(this).parents('.task');

                if(task.hasClass('strikeout')) {
                    task.removeClass('strikeout');
                    task.appendTo($('#tasks'));
                } else {
                    task.addClass('strikeout');
                    task.appendTo($('#done'));
                }
            });


        </script>
    </body>
</html>
"""

app.run(host="0.0.0.0")