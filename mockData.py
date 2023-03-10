mock_data_game = {
    "game:1": {"id": 1,
               "playerCounts": 1,
               "players": [{"name": "aaa", "appEdition": "0.666", "os": "Android", "osEdition": "11.4",
                            "deviceName": "xiaomi", "deviceType": "x50", "deviceId": "did", "stopFrame": "8000"},
                           {"name": "aaa2", "appEdition": "0.666", "os": "Android", "osEdition": "11.4",
                            "deviceName": "xiaomi", "deviceType": "x50", "deviceId": "did",
                            "stopFrame": "8000"}],
               "server": "QA服",
               "startTime": "st1",
               "durationTime": "10分",
               "isConsistent": False,
               "edition": "4001",
               "playCounts": 1,
               "inconsistentCounts": 1
               },
    "game:2": {"id": 2,
               "playerCounts": 2,
               "players": [{"name": "bbb", "appEdition": "0.666", "os": "Android", "osEdition": "11.4",
                            "deviceName": "xiaomi", "deviceType": "x50", "deviceId": "did", "stopFrame": "8000"},
                           {"name": "bbb2", "appEdition": "0.666", "os": "Android", "osEdition": "11.4",
                            "deviceName": "xiaomi", "deviceType": "x50", "deviceId": "did",
                            "stopFrame": "8000"}],
               "server": "公共服",
               "startTime": "st2",
               "durationTime": "8分6秒",
               "isConsistent": True,
               "edition": "4001",
               "playCounts": 2,
               "inconsistentCounts": 2
               },
    "game:3": {"id": 3,
               "playerCounts": 3,
               "players": [{"name": "ccc", "appEdition": "0.666", "os": "Android", "osEdition": "11.4",
                            "deviceName": "xiaomi", "deviceType": "x50", "deviceId": "did", "stopFrame": "8000"},
                           {"name": "ccc2", "appEdition": "0.666", "os": "Android", "osEdition": "11.4",
                            "deviceName": "xiaomi", "deviceType": "x50", "deviceId": "did",
                            "stopFrame": "8000"}],
               "server": "公共服",
               "startTime": "st3",
               "durationTime": "10分",
               "isConsistent": True,
               "edition": "4002",
               "playCounts": 3,
               "inconsistentCounts": 3
               },
    "game:4": {"id": 4,
               "playerCounts": 4,
               "players": [{"name": "ddd", "appEdition": "0.666", "os": "Android", "osEdition": "11.4",
                            "deviceName": "xiaomi", "deviceType": "x50", "deviceId": "did", "stopFrame": "8000"},
                           {"name": "ddd2", "appEdition": "0.666", "os": "Android", "osEdition": "11.4",
                            "deviceName": "xiaomi", "deviceType": "x50", "deviceId": "did",
                            "stopFrame": "8000"}],
               "server": "公共服",
               "startTime": "st4",
               "durationTime": "10分",
               "isConsistent": True,
               "edition": "4002",
               "playCounts": 4,
               "inconsistentCounts": 4
               },
    "game:5": {"id": 5,
               "playerCounts": 5,
               "players": [{"name": "eee", "appEdition": "0.666", "os": "Android", "osEdition": "11.4",
                            "deviceName": "xiaomi", "deviceType": "x50", "deviceId": "did", "stopFrame": "8000"},
                           {"name": "eee2", "appEdition": "0.666", "os": "Android", "osEdition": "11.4",
                            "deviceName": "xiaomi", "deviceType": "x50", "deviceId": "did",
                            "stopFrame": "8000"}],
               "server": "公共服",
               "startTime": "st5",
               "durationTime": "10分",
               "isConsistent": True,
               "edition": "4003",
               "playCounts": 5,
               "inconsistentCounts": 5
               },
    "game:6": {"id": 6,
               "playerCounts": 6,
               "players": [{"name": "fff", "appEdition": "0.666", "os": "Android", "osEdition": "11.4",
                            "deviceName": "xiaomi", "deviceType": "x50", "deviceId": "did", "stopFrame": "8000"},
                           {"name": "fff2", "appEdition": "0.666", "os": "Android", "osEdition": "11.4",
                            "deviceName": "xiaomi", "deviceType": "x50", "deviceId": "did",
                            "stopFrame": "8000"}],
               "server": "公共服",
               "startTime": "st6",
               "durationTime": "10分",
               "isConsistent": True,
               "edition": "4003",
               "playCounts": 6,
               "inconsistentCounts": 6
               }
}

battleData = [{
    'gameId': 'aaa',
    'playerNames': 'xxx xxx2 xxx3',
    'playerList': [
        {"playerId": "101", 'playerName': "xxx", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4',
         'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000", "battleId": "aaa"},
        {"playerId": "102", 'playerName': "xxx2", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4',
         'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000", "battleId": "aaa"},
        {"playerId": "103", 'playerName': "xxx3", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4',
         'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000", "battleId": "aaa"}],
    'serverName': '甜食服',
    'version': 1.1,
    'startTime': '10000',
    'duration': '100',
    'consistStatus': True,
    'playCounts': 1,
    'inconsistentFrameCounts': 2
}, {
    'gameId': 'bbb',
    'playerNames': 'yyy yyy2 yyy3',
    'playerList': [
        {"playerId": "201", 'playerName': "yyy", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4',
         'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000", "battleId": "bbb"},
        {"playerId": "202", 'playerName': "yyy2", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4',
         'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000", "battleId": "bbb"},
        {"playerId": "203", 'playerName': "yyy3", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4',
         'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000", "battleId": "bbb"}],
    'serverName': '深海服',
    'version': 1.2,
    'startTime': '20000',
    'duration': '200',
    'consistStatus': False,
    'playCounts': 1,
    'inconsistentFrameCounts': 2
}, {
    'gameId': 'ccc',
    'playerNames': 'zzz zzz2 zzz3',
    'playerList': [
        {"playerId": "301", 'playerName': "zzz", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4',
         'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000", "battleId": "ccc"},
        {"playerId": "302", 'playerName': "zzz2", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4',
         'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000", "battleId": "ccc"},
        {"playerId": "303", 'playerName': "zzz3", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4',
         'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000", "battleId": "ccc"}],
    'serverName': '甜食服',
    'version': 1.3,
    'startTime': '30000',
    'duration': '300',
    'consistStatus': True,
    'playCounts': 1,
    'inconsistentFrameCounts': 2
}, {
    'gameId': 'ddd',
    'playerNames': 'mmm mmm2 mmm3',
    'playerList': [
        {"playerId": "401", 'playerName': "mmm", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4',
         'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000", "battleId": "ddd"},
        {"playerId": "402", 'playerName': "mmm2", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4',
         'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000", "battleId": "ddd"},
        {"playerId": "403", 'playerName': "mmm3", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4',
         'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000", "battleId": "ddd"}],
    'serverName': '甜食服',
    'version': 1.1,
    'startTime': '10000',
    'duration': '100',
    'consistStatus': True,
    'playCounts': 1,
    'inconsistentFrameCounts': 2
}, {
    'gameId': 'eee',
    'playerNames': 'mmm mmm2 mmm3',
    'playerList': [
        {"playerId": "401", 'playerName': "mmm", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4',
         'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000", "battleId": "eee"},
        {"playerId": "402", 'playerName': "mmm2", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4',
         'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000", "battleId": "eee"},
        {"playerId": "403", 'playerName': "mmm3", 'appEdition': '0.0.0', 'os': "Android", 'osEdition': '11.4',
         'deviceName': 'xiaomi',
         'deviceEdition': 'x50', 'deviceId': 'did', 'stopFrame': "8000", "battleId": "eee"}],
    'serverName': '甜食服',
    'version': 1.1,
    'startTime': '10000',
    'duration': '100',
    'consistStatus': True,
    'playCounts': 1,
    'inconsistentFrameCounts': 2
}]
