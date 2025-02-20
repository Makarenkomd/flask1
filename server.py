from flask import Flask

app = Flask(__name__)


@app.route('/')
def index0():
    return "Миссия Колонизация Марса"

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/start')
def start():
    s = "<html>" + "<br>".join(map(str, list(range(1, 11))[::-1])) +"<br>Start!</html>"
    print(s)
    return s



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')