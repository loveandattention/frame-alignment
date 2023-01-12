import redisMgr
from mockData import mock_data_game

# 清空Redis中的所有数据
redisMgr.flush_db()

# 将数据保存到Redis中
redisMgr.save_to_redis(mock_data_game)

# 获取所有的对局信息
games_data = redisMgr.get_all_game_data()

for game in games_data:
    print(game)
    print(games_data[game])
    print(games_data[game]["edition"])