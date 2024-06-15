document.addEventListener("DOMContentLoaded", function () {
    var buttonMain = document.getElementById("buttonMain");
    if (buttonMain) {
        buttonMain.addEventListener("click", function (e) {
            window.location.href = "/";
        });
    }

    var buttonDM = document.getElementById("buttonDM");
    if (buttonDM) {
        buttonDM.addEventListener("click", function (e) {
            window.location.href = "/dms/receivedDM";
        });
    }

    var buttonMypage = document.getElementById("buttonMypage");
    if (buttonMypage) {
        buttonMypage.addEventListener("click", function (e) {
            window.location.href = "/users/mypage";
        });
    }

    var buttonLogout = document.getElementById("buttonLogout");
    if (buttonLogout) {
        buttonLogout.addEventListener("click", function (e) {
            window.location.href = "/";
        });
    }
});
