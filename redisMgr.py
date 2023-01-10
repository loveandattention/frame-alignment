import redis  # 导入redis 模块
import config

pool = redis.ConnectionPool(host=config.host, port=config.port, decode_responses=True, password=config.password)
my_redis = redis.Redis(connection_pool=pool)


# 将数据保存到Redis中
def save_to_redis(mock_data):
    for gameID in mock_data:
        my_redis.hmset(gameID, mock_data[gameID])


# 获取所有的对局信息
def get_all_game_data():
    game_data = {}
    for game_id in my_redis.keys("game*"):
        game_data[game_id] = my_redis.hgetall(game_id)
    return game_data


# 获取指定ID的对局信息
def get_game_details(game_id):
    return my_redis.hgetall(game_id)
