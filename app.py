from flask import Flask, render_template, request, jsonify
from sqlalchemy import and_

import redisMgr
import config
import logging
from exts import db
from flask_migrate import Migrate
from models import Battle, Player
from base64 import b64decode
import pickle
from dbImp import mysqlImp
from base64 import b64encode


app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{config.USERNAME}:{config.PASSWORD}@{config.HOSTNAME}:{config.PORT}/{config.DATABASE}?charset=utf8"

db.init_app(app)
migrate = Migrate(app, db)


# 测试连接是否成功
# with app.app_context():
#     with db.engine.connect() as conn:
#         s = sqlalchemy.text("select 1")
#         re = conn.execute(s)
#         print(re.fetchone())


@app.after_request
def apply_caching(response):
    # 因为前端是另一个端口，访问flask后台的是跨域访问，所以在所有response中增加cors配置，允许跨域
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    response.headers.add("Access-Control-Allow-Methods", "GET,HEAD,OPTIONS,POST,PUT")
    response.headers.add("Access-Control-Allow-Headers", "*")
    return response


@app.route('/home', methods=['GET', 'POST'])
def home():
    app.logger.info("flask home")
    return '<h1>Home</h1>'


@app.route('/uploadBattle', methods=['POST'])
def uploadBattle():
    app.logger.info("uploadBattle")
    logging.info(request.data)
    uploadInfo = pickle.loads(b64decode(request.data))
    logging.info(uploadInfo)

    game_id = uploadInfo['battleId']
    player_names = [x['name'] for x in uploadInfo['playerInfos']]
    server_name = uploadInfo['serverName']
    version = uploadInfo['version']
    start_time = uploadInfo['startTs']
    duration = uploadInfo['duration']
    consist_status = uploadInfo['consistStatus']
    play_counts = len(uploadInfo['playerInfos'])
    inconsistent_frame_counts = uploadInfo['inconsistentFrameCounts']
    replay_info = pickle.dumps(uploadInfo['replay'])  # bytes type

    player_infos = uploadInfo['playerInfos']

    logging.info(f'game_id: {game_id}, player_names: {player_names}, server_name: {server_name}, version: {version}, '
                 f'start_time: {start_time}, duration: {duration}, consist_status: {consist_status}, '
                 f'play_counts: {play_counts}, inconsistent_frame_counts: {inconsistent_frame_counts}, '
                 f'player_infos: {player_infos}')
    uploadInfo['replay'] = replay_info
    mysqlImp.addBattleData(uploadInfo)
    # recordFile、battleId、playerId、ts、serverName、version、duration、consist
    return 'uploadBattle Return'


@app.route('/downloadBattle', methods=['GET'])
def downloadBattle():
    app.logger.info("downloadBattle")
    game_id = request.args.get('battleId')
    logging.info(f'czx downloadBattle {game_id}')
    battleData = mysqlImp.getBattleData(game_id)
    if not battleData:
        return jsonify({
            'error': f'no battle data {game_id}'
        })
    replayData = pickle.loads(battleData.replayData)

    return jsonify({
        'startInfo': b64encode(replayData['startInfo']).decode(),
        'frameInfo': replayData['frameInfo'],
        'game_id': game_id
    })

@app.route('/gameInfos')
def games_all_info():  # put application's code here
    games = redisMgr.get_all_game_data()
    return render_template("index.html", games=games)


@app.route('/edition')
def games_with_edition():
    edition = request.args.get("edition")
    games = redisMgr.get_edition_game_data(edition)
    return jsonify({"code": 200, "message": "", "games": games})


@app.route('/user/info', methods=['GET', 'OPTIONS'])
def getUserInfo():
    userInfo = {
        "id": '4291d7da9005377ec9aec4a71ea837f',
        'name': 'KsGamer',
        'username': 'admin',
        'password': '',
        'avatar': '/avatar2.jpg',
        'status': 1,
        'telephone': '',
        'lastLoginIp': '27.154.74.117',
        'lastLoginTime': 1534837621348,
        'creatorId': 'admin',
        'createTime': 1497160610259,
        'merchantCode': 'TLif2btpzg079h15bk',
        'deleted': 0,
        'roleId': 'admin',
        'role': {}
    }
    roleObj = {
        'id': 'admin',
        'name': '管理员',
        'describe': '拥有所有权限',
        'status': 1,
        'creatorId': 'system',
        'createTime': 1497160610259,
        'deleted': 0,
        'permissions': [
            {
                'permissionId': 'dashboard',
                'permissionName': '仪表盘',
                'actions':
                    '[{"action":"add","defaultCheck":false,"describe":"新增"},{"action":"query","defaultCheck":false,"describe":"查询"},{"action":"get","defaultCheck":false,"describe":"详情"},{"action":"update","defaultCheck":false,"describe":"修改"},{"action":"delete","defaultCheck":false,"describe":"删除"}]',
                'actionEntitySet': [
                    {
                        'action': 'add',
                        'describe': '新增',
                        'defaultCheck': False
                    },
                    {
                        'action': 'query',
                        'describe': '查询',
                        'defaultCheck': False
                    },
                    {
                        'action': 'get',
                        'describe': '详情',
                        'defaultCheck': False
                    },
                    {
                        'action': 'update',
                        'describe': '修改',
                        'defaultCheck': False
                    },
                    {
                        'action': 'delete',
                        'describe': '删除',
                        'defaultCheck': False
                    }
                ],
                'actionList': [],
                'dataAccess': []
            }
        ]
    }
    userInfo['role'] = roleObj
    return jsonify({
        'result': userInfo,
    })


# @app.route('/battleList', methods=['GET'])
# def getBattleList():
#     versionList = [float(x) for x in request.args.getlist('version[]')]
#     serverNameList = request.args.getlist('serverName[]')
#     pageNo = request.args.get('pageNo')
#     pageSize = request.args.get('pageSize')
#     app.logger.info(f'battleList args is:  version: {versionList}, serverName: {serverNameList}, '
#                     f'pageNo: {pageNo}, pageSize: {pageSize}')
#
#     # 后面需要迭代为根据version、serverName等去服务器查找，并且要设置索引
#     # 目前直接筛选
#     validBattleData = battleData
#     if versionList:
#         validBattleData = [x for x in validBattleData if x['version'] in versionList]
#     if serverNameList:
#         validBattleData = [x for x in validBattleData if x['serverName'] in serverNameList]
#
#     retData = {
#         "pageSize": 2,
#         "pageNo": 1,
#         "totalCount": 100,
#         "totalPage": 10,
#         "data": validBattleData
#     }
#     return jsonify({
#         'result': retData
#     })


# 迭代为数据库交互
@app.route('/battleList', methods=['GET'])
def getBattleList():
    versionList = [float(x) for x in request.args.getlist('version[]')]
    serverNameList = request.args.getlist('serverName[]')
    pageNo = request.args.get('pageNo')
    pageSize = request.args.get('pageSize')
    app.logger.info(f'battleList args is:  version: {versionList}, serverName: {serverNameList}, '
                    f'pageNo: {pageNo}, pageSize: {pageSize}')

    if versionList and serverNameList:
        validBattleData = Battle.query.filter(
            and_(Battle.version.in_(versionList), Battle.server_name.in_(serverNameList)))
    elif versionList:
        validBattleData = Battle.query.filter(Battle.version.in_(versionList))
    elif serverNameList:
        validBattleData = Battle.query.filter(Battle.server_name.in_(serverNameList))
    else:
        validBattleData = Battle.query.all()

    jsonBattleData = [battle.battleToDict() for battle in validBattleData]

    retData = {
        "pageSize": int(pageSize),
        "pageNo": int(pageNo),
        "totalCount": len(jsonBattleData),
        "totalPage": len(jsonBattleData) / int(pageSize),
        "data": jsonBattleData
    }
    return jsonify({
        'result': retData
    })


# @app.route('/battleDetail', methods=['GET'])
# def getBattleDetail():
#     battleId = request.args.get('battleId')
#
#     versionList = [float(x) for x in request.args.getlist('version[]')]
#     serverNameList = request.args.getlist('serverName[]')
#     pageNo = request.args.get('pageNo')
#     pageSize = request.args.get('pageSize')
#     app.logger.info(f'battleList args is:  version: {versionList}, serverName: {serverNameList}, '
#                     f'pageNo: {pageNo}, pageSize: {pageSize}')
#
#     validBattleData = []
#
#     for item in battleData:
#         if item['id'] == battleId:
#             validBattleData.append(item)
#
#     if len(validBattleData) == 0:
#         retData = {
#             "pageSize": 2,
#             "pageNo": 1,
#             "totalCount": 1,  # totalCount设置为1让分页功能不显示
#             "totalPage": 10,
#             "data": []
#         }
#         return jsonify({
#             'result': retData
#         })
#
#     retData = {
#         "pageSize": 2,
#         "pageNo": 1,
#         "totalCount": 1,  # totalCount设置为1让分页功能不显示
#         "totalPage": 10,
#         "data": validBattleData
#     }
#     return jsonify({
#         'result': retData
#     })


# 迭代为数据库交互
@app.route('/battleDetail', methods=['GET'])
def getBattleDetail():
    battleId = request.args.get('battleId')

    versionList = [float(x) for x in request.args.getlist('version[]')]
    serverNameList = request.args.getlist('serverName[]')
    pageNo = request.args.get('pageNo')
    pageSize = request.args.get('pageSize')
    app.logger.info(f'battleList args is:  version: {versionList}, serverName: {serverNameList}, '
                    f'pageNo: {pageNo}, pageSize: {pageSize}')

    jsonBattleData = []
    battle = Battle.query.get(battleId)
    if battle:
        jsonBattleData = [battle.battleToDict()]

    retData = {
        "pageSize": 2,
        "pageNo": 1,
        "totalCount": 1,  # totalCount设置为1让分页功能不显示
        "totalPage": 10,
        "data": jsonBattleData
    }
    return jsonify({
        'result': retData
    })


# @app.route('/playerList', methods=['GET'])
# def getPlayerList():
#     battleId = request.args.get('battleId')
#
#     versionList = [float(x) for x in request.args.getlist('version[]')]
#     serverNameList = request.args.getlist('serverName[]')
#     pageNo = request.args.get('pageNo')
#     pageSize = request.args.get('pageSize')
#     app.logger.info(f'battleList args is:  version: {versionList}, serverName: {serverNameList}, '
#                     f'pageNo: {pageNo}, pageSize: {pageSize}')
#
#     validBattleData = []
#
#     for item in battleData:
#         if item['id'] == battleId:
#             validBattleData.append(item)
#
#     if len(validBattleData) == 0:
#         retData = {
#             "pageSize": 2,
#             "pageNo": 1,
#             "totalCount": 1,
#             "totalPage": 10,
#             "data": []
#         }
#         return jsonify({
#             'result': retData
#         })
#
#     retData = {
#         "pageSize": 2,
#         "pageNo": 1,
#         "totalCount": 1,
#         "totalPage": 10,
#         "data": validBattleData[0]['playerList']
#     }
#     return jsonify({
#         'result': retData
#     })


# 迭代为数据库交互
@app.route('/playerList', methods=['GET'])
def getPlayerList():
    battleId = request.args.get('battleId')

    versionList = [float(x) for x in request.args.getlist('version[]')]
    serverNameList = request.args.getlist('serverName[]')
    pageNo = request.args.get('pageNo')
    pageSize = request.args.get('pageSize')
    app.logger.info(f'battleList args is:  version: {versionList}, serverName: {serverNameList}, '
                    f'pageNo: {pageNo}, pageSize: {pageSize}')

    jsonPlayerData = []

    players = Player.query.filter_by(battle_id=battleId)
    if players:
        jsonPlayerData = [player.playerToDict() for player in players]

    retData = {
        "pageSize": 2,
        "pageNo": 1,
        "totalCount": 1,
        "totalPage": 10,
        "data": jsonPlayerData
    }
    return jsonify({
        'result': retData
    })


battleData = []
battleData.append({
    'key': '1',
    'id': '1',
    'gameId': 'aaa',
    'playerNames': 'xxx xxx2 xxx3',
    'playerList': [
        {'playerName': "xxx", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4', 'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000"},
        {'playerName': "xxx2", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4', 'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000"},
        {'playerName': "xxx3", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4', 'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000"}],
    'serverName': '甜食服',
    'version': 1.1,
    'startTime': '10000',
    'duration': '100',
    'consistStatus': True,
    'playCounts': 1,
    'inconsistentFrameCounts': 2
})
battleData.append({
    'key': '2',
    'id': '2',
    'gameId': 'bbb',
    'playerNames': 'yyy yyy2 yyy3',
    'playerList': [
        {'playerName': "yyy", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4', 'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000"},
        {'playerName': "yyy2", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4', 'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000"},
        {'playerName': "yyy3", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4', 'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000"}],
    'serverName': '深海服',
    'version': 1.2,
    'startTime': '20000',
    'duration': '200',
    'consistStatus': False,
    'playCounts': 1,
    'inconsistentFrameCounts': 2
})
battleData.append({
    'key': '3',
    'id': '3',
    'gameId': 'ccc',
    'playerNames': 'zzz zzz2 zzz3',
    'playerList': [
        {'playerName': "zzz", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4', 'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000"},
        {'playerName': "zzz2", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4', 'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000"},
        {'playerName': "zzz3", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4', 'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000"}],
    'serverName': '甜食服',
    'version': 1.3,
    'startTime': '30000',
    'duration': '300',
    'consistStatus': True,
    'playCounts': 1,
    'inconsistentFrameCounts': 2
})

if __name__ == '__main__':
    app.run(host=config.host, port=config.flask_port)
