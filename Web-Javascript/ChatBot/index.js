var chat = document.getElementsByClassName('answer');
var body = document.getElementsByTagName('body');
var n = 0;
var follow = 0;

var app = document.getElementById('typed');
var typewriter = new Typewriter(app, {
    loop: false
});

var typewriter2 = new Typewriter(chat[0], {
    loop: false
})

typewriter.callFunction(function (state) {
    state.elements.cursor.style.display = "none"
    })
    .start();

chatText("안녕! 하고 싶은 말 있니?")

function check_text() {
    var value = document.getElementById("console").value;
    console.log(value);

    if (value.includes("안녕")) {
        chatText("안녕!!")
    }
    else if (value.includes("이름")) {
        chatText("스누피라고 해!")
    }
    else if (value.includes("뭐해") || value.includes("뭐하고")) {
        chatText("하늘을 보고 있어~");
    }
    else if (value.includes("안아")) {
        if (n == 0) {
            chatText("그랭");
            body[0].style.backgroundImage = "url('/ChatBot/snoopy2.png')";
            n++;
        }
        else if (n == 1) {
            chatText("이미 안아주고 있는 걸?");
            n++;
        }
        else {
            body[0].style.backgroundImage = "url('/ChatBot/snoopy.webp')"
            chatText("다시 누울래. 너도 이리 누워");
            n = 0;
        }
    }
    else if (value.includes("하늘")) {
        chatText("매일 하늘을 눈에 담고 있어");
        body[0].style.backgroundImage = "url('/ChatBot/snoopy.webp')"
    }
    else if (value.includes("따라해")) {
        chatText("그래 알겠어!");
        follow = 1;
    }
    else if (follow == 1) {
        if (value.includes("그만")) {
            chatText("그래 그만하자~!");
            follow = 0;
        }
        else {
            chatText(value + " 짠!");
        }
    }
    else {
        chatText("응? 뭐라고?");

        typewriter.typeString("키워드를 참고해보세요!")
            .pauseFor(500)
            .deleteAll()
            .callFunction(function (state) {
                state.elements.cursor.style.display = "none"
            })
            .start();
    }
    
}

function chatText(x) {
    typewriter2
        .deleteAll()
        .typeString(x)
        .pauseFor(500)
        .callFunction(function (state) {
            state.elements.cursor.style.display = "none"
        })
        .start();
}
