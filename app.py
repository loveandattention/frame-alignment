from flask import Flask, render_template, request, jsonify
import redisMgr
import mockData

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    games = redisMgr.get_all_game_data()
    return render_template("index.html", games=games)


@app.route('/edition')
def games_with_edition():
    edition = request.args.get("edition")
    games = redisMgr.get_edition_game_data(edition)
    return jsonify({"code": 200, "message": "", "games": games})


@app.route("/playerCounts")
def games_with_playerCounts():
    counts = request.args.get("playerCounts")
    games = redisMgr.get_player_counts_game_data(counts)
    return jsonify({"code": 200, "message": "", "games": games})


@app.route("/id")
def game_details():
    id = request.args.get("id")
    game = redisMgr.get_id_game_data(id)
    return jsonify({"code": 200, "message": "", "game": game})


if __name__ == '__main__':
    app.run()
