import redis  # 导入redis 模块
import config

pool = redis.ConnectionPool(host=config.host, port=config.redis_port, decode_responses=True, password=config.password)
my_redis = redis.Redis(connection_pool=pool)


# 将数据保存到Redis中
def save_to_redis(mock_data_game):
    for game in mock_data_game:
        my_redis.hmset(game, mock_data_game[game])
        my_redis.sadd(mock_data_game[game]["edition"], mock_data_game[game]["id"])


# 获取所有的对局信息
def get_all_game_data():
    games_data = {}
    for game in my_redis.keys("game:*"):
        games_data[game] = my_redis.hgetall(game)
    return games_data


# 获取指定ID的对局信息
def get_game_details(game_id):
    return my_redis.hgetall(game_id)


# 清空数据库
def flush_db():
    my_redis.flushdb()


# 获取指定版本的对局信息
def get_edition_game_data(edition):
    games_data = {}
    for game_id in my_redis.smembers(edition):
        for game in my_redis.keys("game:" + game_id + "*"):
            games_data[game] = my_redis.hgetall(game)
    return games_data
