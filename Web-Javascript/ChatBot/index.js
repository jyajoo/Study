var chat = document.getElementsByClassName('answer');
var body = document.getElementsByTagName('body');
var app = document.getElementById('typed');
var app2 = document.getElementById('teach');
var n = 0;
var follow = 0;
var key = 0;
var question = "";
var answer = "";

var typewriter = new Typewriter(app, {
    loop: false
});
var typewriter2 = new Typewriter(chat[0], {
    loop: false
})
var typewriter3 = new Typewriter(app2, {
    loop: false
});

var json = [
    {
        "question": "안녕",
        "answer": "안녕!!"
    },
    {
        "question": "이름",
        "answer": "스누피라고 해!"
    }
];

typewriter.callFunction(function (state) {
    state.elements.cursor.style.display = "none"
    })
    .start();

typewriter3.callFunction(function (state) {
    state.elements.cursor.style.display = "none"
    })
    .start();

chatText("안녕! 하고 싶은 말 있니?");

function check_text() {
    var value = document.getElementById("console").value;
    console.log(value);

    if (key == 1) {
        if (value.includes("그래")) {
            chatText("대답을 입력해줘!");
            key = 2;
        }
        else {
            chatText("안녕! 하고 싶은 말 있니?");
            key = 0;
        }
        return;
    }   

    if (key == 2) {
        answer = value;
        push_join();
        return;
    }


    if (value.includes("뭐해") || value.includes("뭐하고")) {
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
            body[0].style.backgroundImage = "url('/ChatBot/snoopy.webp')";
            chatText("다시 누울래. 너도 이리 누워");
            n = 0;
        }
    }
    else if (value.includes("하늘")) {
        chatText("매일 하늘을 눈에 담고 있어");
        body[0].style.backgroundImage = "url('/ChatBot/snoopy.webp')";
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
        for (let i = 0; i < json.length; i++){
            if (value.includes(json[i].question)) {
                chatText(json[i].answer);
                return;
            }
        }
        chatText("응? 뭐라고? 말을 가르쳐줘");

        typewriter.pauseFor(4500)
            .typeString("키워드를 참고해보세요!")
            .pauseFor(4000)
            .deleteAll()
            .callFunction(function (state) {
                state.elements.cursor.style.display = "none"
            })
            .start();
        typewriter3.pauseFor(4500)
            .typeString("말을 가르치고 싶다면 " + '"' + "그래" + '"' + " 입력")
            .pauseFor(3500)
            .deleteAll()
            .callFunction(function (state) {
                state.elements.cursor.style.display = "none"
            })
            .start();
        key = 1;
        question = value;
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

function push_join() {
    json.push({ question: `${question}`, answer: `${answer}` });

    chatText("말을 배웠어 고마워!");
    key = 0;
}