import redisMgr
from app import app
from mockData import mock_data_game, battleData
from exts import db
from models import Battle, Player


# # 清空Redis中的所有数据
# redisMgr.flush_db()

# # 将数据保存到Redis中
# redisMgr.save_to_redis(mock_data_game)

# # 获取所有的对局信息
# games_data = redisMgr.get_all_game_data()
# print(games_data)
# print(type(games_data))
# print(type(games_data["game:4"]))
# print(type(games_data["game:4"]["players"]))
# for game in games_data:
#     print(game)
#     print(games_data[game])
#     print(games_data[game]["edition"])


# print(redisMgr.get_edition_game_data("4001"))

# print(redisMgr.get_id_game_data("1"))

# print(redisMgr.get_player_counts_game_data(1))


# MySQL test
# 将battleData保存到MySQL中
def battleAdd(battleData):
    for battleItem in battleData:
        battle = Battle(game_id=battleItem["gameId"], player_names=battleItem["playerNames"],
                        server_name=battleItem["serverName"], version=battleItem["version"],
                        start_time=battleItem["startTime"],
                        duration=battleItem["duration"], consist_status=battleItem["consistStatus"],
                        play_counts=battleItem["playCounts"],
                        inconsistent_frame_counts=battleItem["inconsistentFrameCounts"])
        for playerItem in battleItem["playerList"]:
            player = Player(player_id=playerItem["playerId"], name=playerItem["playerName"], app_edition=playerItem["appEdition"], os=playerItem["os"],
                            os_edition=playerItem["osEdition"], device_name=playerItem["deviceName"],
                            device_edition=playerItem["deviceEdition"], device_id=playerItem["deviceId"],
                            stop_frame=playerItem["stopFrame"], battle_id=playerItem["battleId"])
            db.session.add(player)
        db.session.add(battle)
        db.session.commit()


with app.app_context():
    battleAdd(battleData)
