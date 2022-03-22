var chat = document.getElementsByTagName('p')

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
}
