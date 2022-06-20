var num = 1;
var q = {
    1: { "title": "나는 친구를 사귈 때,<br> 어떤 편이지?", "type": "EI", "A": "안녕! 이름이 뭐야??<br> 먼저 말을 걸어본다.", "B": "누군가 먼저 다가오진 않을까?<br> 하며 잠시 기다린다." },
    2: { "title": "어? 여기 와봤던 곳이네!<br> 근데 어디로 갔었더라?", "type": "SN", "A": "잘못 들렸다가 길 잃으면 시간 아까워,<br>지도 찾아보자!", "B": "오른쪽 길이었던 것 같아<br>구경도 할 겸 가보자고~!" },
    3: { "title": "와 너 진짜 잘했다!!<br>열심히 안 하는 것 같았는데,<br>재능 쩐다.. 멋져!", "type": "TF", "A": "아 별거 아니야 (내심 매우 행복해한다.)", "B": "아 고마워!<br> (근데 나 열심히 했는데....ㅎ..ㅎㅎ..)" },
    4: { "title": "우리 강릉 여행 갈래?<br> 바다 보고 싶어!", "type": "JP", "A": "숙소와 가고 싶은 곳을 찾으며<br> 거리도 살펴본다.", "B": "여기도 가고 싶고, 저기도 가고 싶고,,<br> 엥 야 대박 저기 갈래??" },

    5: { "title": "시험이 다가오는데<br> 공부가 손에 잡히질 않네,,", "type": "SN", "A": "어떤 공부 방법이 좋을까..?<br> 저번 시험엔 뭐가 나왔지?", "B": "아 시험 왜 있냐.<br> 시험 끝나고 놀이공원도 가고,<br> 와 자전거 타고 싶다!!" },
    6: { "title": "친구가 갑작스레<br> 약속을 취소했다.", "type": "EI", "A": "앗, 카톡  창을 켜서<br> 만날 사람을 구해본다.", "B": "아쉽긴 한데, 어쩔 수 없지. ㅠㅠ<br> (행복하게 침대에 눕는다)" },
    7: { "title": "아 전에 했던 말 사실은,,,,<br> (친구가 선의의 거짓말을<br> 했다는 것을 털어두었다.)", "type": "TF", "A": "그래도 사실대로 말해줬어야지..", "B": "하.. 그래<br> 그래도 나를 배려해서 그랬던 거니까" },
    8: { "title": "과제가 주어졌다.<br> 두둥탁!", "type": "JP", "A": "뭐부터 하면 좋을까?<br> (살펴보며, 순서를 정한다.)", "B": "아 과제,,<br> 일단 자료나 좀 찾아봐야겠다." },

    9: { "title": "너랑 나,<br> 좀 잘 안 맞는 것 같아.", "type": "TF", "A": "왜 그렇게 생각하는데? 이유가 뭐야?", "B": ".........(상처받는다)" },
    10: { "title": "연인과의 데이트,<br> 이번엔 뭘 할까?", "type": "EI", "A": "여기 인테리어도 예쁘고<br> 사진 건지고 싶어! 갈래?", "B": "에어컨 시원하게 틀고<br> 아이스크림 먹으면서 영화 보자!!" },
    11: { "title": "노래나 들어볼까?<br> 뭐 듣지~?", "type": "SN", "A": "멜로디 좋다~ 하트 꾹!", "B": "이 노래 좋다~ 가사랑 같이 봐야겠다." },
    12: { "title": "구매하기 전<br> 나에게 더 중요한 것은??", "type": "JP", "A": "1점짜리 리뷰", "B": "5점짜리 리뷰" }
}

var result = {
    "INFJ": { "dog": "진돗개🐾", "explain": "자기 일을 혼자서도 척척 잘하는 당신은, <br> 충성스럽기도 하고 활기차며<br> 똑똑하기까지 한 진돗개와 어울려요.", "img": "img/jindo dog.jpg" },
    "INFP" : {"dog" : "푸들🐾", "explain" : "본인만의 스타일이 확고한 당신은, <br> 믿음이 쌓인 사람에게 한없이 신뢰하며<br> 사랑하는 푸들과 어울려요.", "img" : "img/poodle.jpg"},
    "INTJ": { "dog": "페키니즈🐾", "explain": "자존감이 높고 이상적인 당신은, <br> 도도하며 독립적이며 적응을 잘해<br> 부드러운 성격인 페키니즈와 어울려요.", "img": "img/pekingese.jpg" },
    "INTP" : {"dog" : "차우차우🐾", "explain" : "호불호가 뚜렷하고 즉흥적인 당신은, <br> 주인에게는 충신하지만,<br> 타인에게는 배타적이기도 한<br> 차우차우와 어울려요.", "img" : "img/chow.jpg"},
    
    "ISTP" : {"dog" : "비숑 프리제🐾", "explain" : "눈치가 빠르고 내 사람에게<br> 따뜻한 당신은, <br> 상황 파악이 빨라 적응력이 높고 <br> 순하고 명랑한 비숑과 어울려요.", "img" : "img/bichon.jpg"},
    "ISTJ" : {"dog" : "시베리안 허스키🐾", "explain" : "신중하고 책임감이 강한 당신은, <br> 겉보기엔 차갑지만, 마음이 넓고<br> 사회성이 강한 허스키와 어울려요.", "img" : "img/husky.jpg"},
    "ISFJ" : {"dog" : "빠삐용🐾", "explain" : "섬세하고<br> 주변 환경에 집중을 잘하는 당신은, <br> 주인과의 유대감이 깊고, <br> 행복함을 베푸는 빠빠용과 어울려요.", "img" : "img/papillon.jpg"},
    "ISFP" : {"dog" : "시바견🐾", "explain" : "인내심이 강하고<br> 조화를 좋아하는 당신은, <br> 독립적이고 민첩하며<br> 주인에게만 충성하는<br> 시바견과 어울려요.", "img" : "img/shiba dog.jpg"},

    "ENTP" : {"dog" : "프렌치 불독🐾", "explain" : "순발력이 뛰어나고<br> 재치있는 당신은, <br> 겁이 많지 않아 대범하며<br> 호기심이 많고 온순한<br> 불독과 어울려요.", "img" : "img/bulldog.jpg"},
    "ENTJ" : {"dog" : "저먼 셰퍼드🐾", "explain" : "추진력이 빠르고 솔직한 당신은, <br> 리더쉽 있는 주인에게 애정 표현이 많고 영리한 저먼 셰퍼드가 어울려요.", "img" : "img/german shepherd.jpg"},
    "ENFP" : {"dog" : "퍼그🐾", "explain" : "새로운 것을 좋아하고<br> 매력적인 당신은, <br> 질투가 많아 애교가 넘치고<br> 특유의 장난기를 가지고 있는<br> 퍼그와 어울려요.", "img" : "img/pug.jpg"},
    "ENFJ": { "dog": "골든 리트리버🐾", "explain": "온화하고 적극적이며<br> 사교성이 풍부한 당신은, <br> 사회성이 매우 좋아<br> 낯가림이 없고 해맑은<br> 골든 리트리버와 어울려요", "img": "img/retriever.jpg" },
    
    "ESTJ" : {"dog" : "보더콜리🐾", "explain" : "현실 감각이 뛰어나며<br> 지도력 있는 당신은, <br> 지능이 높고 끈기 있으며<br> 게으르지 않은 보더콜리와 어울려요.", "img" : "img/border collie.jpg"},
    "ESTP" : {"dog" : "잭 러셀 테리어🐾", "explain" : "판단력이 좋고 <br> 문제 해결 능력이 뛰어난 당신은, <br> 호기심과 활동량이 많고<br> 끈기가 강한<br> 잭 러셀 테리어와 어울려요.", "img" : "img/jack.jpg"},
    "ESFJ" : {"dog" : "닥스훈트🐾", "explain" : "정이 많고 공감 능력이 좋은 당신은, <br> 눈치도 빠르고 똑똑하며<br> 애교가 많은 닥스훈트와 어울려요.", "img" : "img/dachshund.jpg"},
    "ESFP" : {"dog" : "웰시코기🐾", "explain" : "낙천적이고<br 분위기 조성을 잘하는 당신은, <br> 훈련 이행 능력이 뛰어나고<br> 친화력이 높은 웰시코기와 어울려요.", "img" : "img/welsh corgi.jpg"}
}

function start() {
    $(".start").hide();
    $(".question").show();
    $(".banner").hide();
    $(".kakao").hide();
    next();
}

$("#A").click(function () {
    var type = $("#type").val();
    var preValue = $("#" + type).val();
    $("#" + type).val(parseInt(preValue) + 1);
    next();
});

$("#B").click(function () {
    next();
});

function next() {

    if (num > 12) {
        $(".question").hide();
        $(".result").show();
        var mbti = "";
        ($("#EI").val() < 2) ? mbti += "I" : mbti += "E";
        ($("#SN").val() < 2) ? mbti += "N" : mbti += "S";
        ($("#TF").val() < 2) ? mbti += "F" : mbti += "T";
        ($("#JP").val() < 2) ? mbti += "P" : mbti += "J";
        $("#img").attr("src", result[mbti]["img"])
        $("#dog").html(result[mbti]["dog"])
        $("#explain").html(result[mbti]["explain"])
        $(".banner").show();
        $(".kakao").show();

    } else {
        $(".progress-bar").attr("style", "width : calc(100/12*" + num + "%)");
        $("#title").html(q[num]["title"]);
        $("#type").val(q[num]["type"]);
        $("#A").html(q[num]["A"]);
        $("#B").html(q[num]["B"]);
        num++;
    }

}