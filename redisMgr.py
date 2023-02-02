import redis  # 导入redis 模块
import config
import json

pool = redis.ConnectionPool(host=config.host, port=config.redis_port, decode_responses=True, password=config.password)
my_redis = redis.Redis(connection_pool=pool)


# 将数据保存到Redis中
def save_to_redis(mock_data_game):
    for game in mock_data_game:
        my_redis.set(game, json.dumps(mock_data_game[game]))
        my_redis.sadd(mock_data_game[game]["edition"], mock_data_game[game]["id"])
        my_redis.zadd("playerCounts", mock_data_game[game]["id"], mock_data_game[game]["playerCounts"])


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


# 获取指定id的对局信息
def get_id_game_data(id):
    game = json.loads(my_redis.get("game:" + id))
    return game


# 获取指定最少玩家数量以上的对局信息
def get_player_counts_game_data(counts):
    ids = my_redis.zrangebyscore("playerCounts", counts, 999)
    games_data = {}
    for game_id in ids:
        game = "game:" + game_id
        games_data[game] = json.loads(my_redis.get(game))
    return games_data

