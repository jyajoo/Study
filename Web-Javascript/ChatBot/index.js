var chat = document.getElementsByTagName('p');
var body = document.getElementsByTagName('body');
var n = 0;
var follow = 0;

function check_text() {
    var value = document.getElementById("console").value;
    console.log(value);

    if (value.includes("안녕")) {
        chat[0].innerHTML = "안녕!!";
    }
    else if (value.includes("이름")) {
        chat[0].innerHTML = "스누피라고 해!";
    }
    else if (value.includes("뭐해") || value.includes("뭐하고")) {
        chat[0].innerHTML = "하늘을 보고 있어~";
    }
    else if (value.includes("안아")) {
        if (n == 0) {
            chat[0].innerHTML = "그랭";
            body[0].style.backgroundImage = "url('/ChatBot/snoopy2.png')";
            n++;
        }
        else if (n == 1) {
            chat[0].innerHTML = "이미 안아주고 있는 걸?";
            n++;
        }
        else {
            body[0].style.backgroundImage = "url('/ChatBot/snoopy.webp')"
            chat[0].innerHTML = "다시 누울래. 너도 이리 누워";
            n = 0;
        }
    }
    else if (value.includes("하늘")) {
        chat[0].innerHTML = "매일 하늘을 눈에 담고 있어";
        body[0].style.backgroundImage = "url('/ChatBot/snoopy.webp')"
    }
    else if (value.includes("따라해")) {
        follow++;
    }
    else if (value.includes("그만")) {
        chat[0].innerHTML = "그래 그만하자~!";
        follow = 0;
    }

    if (follow > 0) {
        chat[0].innerHTML = value + " 짠!";
    }
}

