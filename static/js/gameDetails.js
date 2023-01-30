function gameDetails(th) {
    id = th.id;

    $.ajax({
        url: "id?id=" + id,
        method: "GET",
        success: function (result) {
            var game = result["game"];

            // 对战详情
            let str1 = "";

            let playersName = "";

            for (let player of game.players) {
                playersName += player.name + " "

                str1 += "<tr><td>" + player.name +
                    "</td><td>" + player.appEdition +
                    "</td><td>" + player.os +
                    "</td><td>" + player.osEdition +
                    "</td><td>" + player.deviceName +
                    "</td><td>" + player.deviceType +
                    "</td><td>" + player.deviceId +
                    "</td><td>" + player.stopFrame +
                    "</td><td>" + "<a href=\"javascript:void(0)\" onclick=\"\">快照hash</a>" + "</td></tr>"
            }

            $("#playersTable").html(str1)

            // 对战总览
            let str2 = "";

            str2 += "<tr><td>" + game.startTime +
                "</td><td>" + game.durationTime +
                "</td><td>" + game.server +
                "</td><td>" + game.isConsistent +
                "</td><td>" + playersName + "</td></tr>"

            $("#battleTable").html(str2)

            // 回放总览
            let str3 = "";

            str3 += "<tr><td>" + game.playCounts +
                "</td><td>" + game.inconsistentCounts + "</td></tr>"

            $("#replayTable").html(str3)

        },
    })

}