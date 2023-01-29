function editionSelect() {
    var edition = event.currentTarget.innerText;
    $.ajax({
        url: "edition?edition=" + edition,
        method: "GET",
        success: function (result) {
            var games = result["games"];
            if (games == null || games.length === 0) {
                alert("数据为空")
            } else {
                let str = "";

                for (let game in games) {
                    str += "<tr><td>" + games[game].id +
                        "</td><td>" + games[game].player +
                        "</td><td>" + games[game].server +
                        "</td><td>" + games[game].startTime +
                        "</td><td>" + games[game].durationTime +
                        "</td><td>" + games[game].isConsistent +
                        "</td><td>" + "查看详情" + "</td></tr>"
                }

                $("#gamesTable").html(str)
            }
        },
    })
}