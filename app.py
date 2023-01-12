from flask import Flask, render_template, request
import redisMgr

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    games = redisMgr.get_all_game_data()
    return render_template("index.html", games=games)


@app.route('/edition')
def games_with_edition():
    edition = request.args.get("edition")
    games = redisMgr.get_edition_game_data(edition)
    return render_template("index.html", games=games)


if __name__ == '__main__':
    app.run()
