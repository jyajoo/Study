var chat = document.getElementsByTagName('p')
var body = document.getElementsByTagName('body')

function check_text() {
    var value = document.getElementById("console").value;
    console.log(value);

    if (value == "안녕") {
        chat[0].innerHTML = "안녕!!"
    }
    else if (value == "이름이 뭐야?") {
        chat[0].innerHTML = "스누피라고 해!"
    }
    else if (value == "뭐해?") {
        chat[0].innerHTML = "하늘을 보고 있어~"
    }
    else if (value == "안아줘") {
        chat[0].innerHTML = "그랭"
        body[0].style.backgroundImage = "url('/ChatBot/snoopy2.png')"
    }
}

