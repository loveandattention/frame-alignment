from flask import Flask
from flask import render_template
import redisMgr

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    games = redisMgr.get_all_game_data()
    return render_template("index.html", games=games)


if __name__ == '__main__':
    app.run()
