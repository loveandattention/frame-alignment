import redis  # 导入redis 模块
import config
import json

pool = redis.ConnectionPool(host=config.host, port=config.port, decode_responses=True, password=config.password)
my_redis = redis.Redis(connection_pool=pool)


# 将数据保存到Redis中
def save_to_redis(mock_data_game):
    for game in mock_data_game:
        my_redis.set(game, json.dumps(mock_data_game[game]))
        my_redis.sadd(mock_data_game[game]["edition"], mock_data_game[game]["id"])


# 获取所有的对局信息
def get_all_game_data():
    games_data = {}
    for game in my_redis.keys("game:*"):
        games_data[game] = json.loads(my_redis.get(game))
    return games_data


# 清空数据库
def flush_db():
    my_redis.flushdb()


# 获取指定版本的对局信息
def get_edition_game_data(edition):
    games_data = {}
    for game_id in my_redis.smembers(edition):
        game = "game:" + game_id
        games_data[game] = json.loads(my_redis.get(game))
    return games_data
