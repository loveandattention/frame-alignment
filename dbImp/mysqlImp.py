from exts import db
from models import Battle, Player


def battleAdd(battleData):
    for battleItem in battleData:
        battle = Battle(game_id=battleItem["gameId"], player_names=battleItem["playerNames"],
                        server_name=battleItem["serverName"], version=battleItem["version"],
                        start_time=battleItem["startTime"],
                        duration=battleItem["duration"], consist_status=battleItem["consistStatus"],
                        play_counts=battleItem["playCounts"],
                        inconsistent_frame_counts=battleItem["inconsistentFrameCounts"])
        for playerData in battleItem["playerList"]:
            player = Player(name=playerData["playerName"], app_edition=playerData["appEdition"], os=playerData["os"],
                            os_edition=playerData["osEdition"], device_name=playerData["deviceName"],
                            device_edition=playerData["deviceEdition"], device_id=playerData["deviceId"],
                            stop_frame=playerData["stopFrame"])
            battle.players.append(player)
        db.session.add(battle)
        db.session.commit()


def addBattleData(battleData):
    battle = Battle(
        game_id=battleData['battleId'],
        player_names=";".join([x['name'] for x in battleData['playerInfos']]),
        server_name=battleData["serverName"],
        version=battleData["version"],
        start_time=battleData["startTs"],
        duration=battleData["duration"],
        consist_status=battleData["consistStatus"],
        play_counts=len(battleData["playerInfos"]),
        inconsistent_frame_counts=battleData["inconsistentFrameCounts"],
        replayData=battleData["replay"],
    )
    for playerData in battleData['playerInfos']:
        player = Player(
            player_id=playerData['id'],
            name=playerData["name"],
            app_edition=playerData["appEdition"],
            os=playerData["os"],
            os_edition=playerData["osEdition"],
            device_name=playerData["deviceName"],
            device_edition=playerData["deviceEdition"],
            device_id=playerData["deviceId"],
            stop_frame=playerData.get("stopFrame", 0),
            battle_id=battleData['battleId'],
        )

        db.session.add(player)

    db.session.add(battle)
    db.session.commit()
