function playerCountsSelection(th) {
    var playerCounts = th.innerText;
    $.ajax({
        url: "playerCounts?playerCounts=" + playerCounts,
        method: "GET",
        success: function (result) {
            var games = result["games"];
            if (games == null || games.length === 0) {
                alert("数据为空")
            } else {
                let str = "";

                for (let game in games) {
                    let playersName = "";
                    for (var player of games[game].players) {
                        playersName += player.name + " "
                    }
                    str += "<tr><td>" + games[game].id +
                        "</td><td>" + playersName +
                        "</td><td>" + games[game].server +
                        "</td><td>" + games[game].startTime +
                        "</td><td>" + games[game].durationTime +
                        "</td><td>" + games[game].isConsistent +
                        "</td><td>" + "<a href=\"javascript:void(0)\" onclick=\"gameDetails(this)\" id=\"" + games[game].id + "\">查看详情</a>" + "</td></tr>"
                }

                $("#gamesTable").html(str)
            }
        },
    })
}