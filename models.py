from exts import db


class Battle(db.Model):
    __tablename__ = "battles"

    game_id = db.Column(db.String(255), primary_key=True)
    player_names = db.Column(db.String(255))
    server_name = db.Column(db.String(255))
    version = db.Column(db.String(255))
    start_time = db.Column(db.String(255))
    duration = db.Column(db.String(255))
    consist_status = db.Column(db.Boolean)
    play_counts = db.Column(db.Integer)
    inconsistent_frame_counts = db.Column(db.Integer)
    replayData = db.Column(db.LargeBinary)

    # players = db.relationship("Player", back_populates="battle")

    def battleToDict(self):
        return {"gameId": self.game_id, "playerNames": self.player_names, "version": self.version,
                "serverName": self.server_name, "startTime": self.start_time, "duration": self.duration,
                "consistStatus": self.consist_status, "playCounts": self.play_counts,
                "inconsistentFrameCounts": self.inconsistent_frame_counts}


class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player_id = db.Column(db.String(255))
    name = db.Column(db.String(255))
    app_edition = db.Column(db.String(255))
    os = db.Column(db.String(255))
    os_edition = db.Column(db.String(255))
    device_name = db.Column(db.String(255))
    device_edition = db.Column(db.String(255))
    device_id = db.Column(db.String(255))
    stop_frame = db.Column(db.Integer)

    battle_id = db.Column(db.String(255))

    # battle_id = db.Column(db.Integer, db.ForeignKey("battle.id"))
    # battle = db.relationship("Battle", back_populates="players")

    # 定义索引
    __table_args__ = (db.Index('idx_player_id', 'player_id'), )

    def playerToDict(self):
        return {"playerName": self.name, "appEdition": self.app_edition, "os": self.os,
                "osEdition": self.os_edition, "deviceName": self.device_name,
                "deviceEdition": self.device_edition,
                "deviceId": self.device_id, "stopFrame": self.stop_frame, "id": self.id}
