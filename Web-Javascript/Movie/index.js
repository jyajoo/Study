var poster = document.getElementsByClassName('poster');
var iframe = document.getElementsByTagName('iframe');
var movie = document.getElementsByClassName('movie');
var content = document.getElementsByClassName('content');
var a = document.getElementsByTagName('a');

function one() {
    poster[0].src = "poster/weather child.jpg";
    iframe[0].src = "https://www.youtube.com/embed/ILQl1Q4jizc?start=17";
    movie[0].innerHTML = "&lt; 날씨의 아이 &gt;";
    content[0].innerHTML = "장르 : 애니메이션<br>" +
        "상영 시간 : 112분<br>" +
        "국내 등급 : 15세 관람가<br>" +
        "<br>" +
        "“이제 비는 그치고, 우리의 세상이 빛나기 시작할 거야”<br>" +
        "비가 그치지 않던 어느 여름 날, 가출 소년 ‘호다카’는 수상한 잡지사에 취직하게 되고" +
        "비밀스러운 소녀 ‘히나’를 우연히 만난다.<br>" +
        "“지금부터 하늘이 맑아질 거야”<br>" +
        "그녀의 기도에 거짓말같이 빗줄기는 멈추고, 사람들의 얼굴에 환한 빛이 내려온다.<br>" +
        "하지만, 맑음 뒤 흐림이 찾아오듯 두 사람은 엄청난 세계의 비밀을 마주하게 되는데…";
    a[0].href = "https://movie.naver.com/movie/bi/mi/basic.naver?code=181114"
    a[1].href = "https://www.netflix.com/search?q=%EB%82%A0%EC%94%A8%EC%9D%98&jbv=81172898"
}

function two() {
    poster[0].src = "poster/Arrietty.jpg";
    iframe[0].src = "https://play-tv.kakao.com/embed/player/cliplink/302398792?service=player_share";
    movie[0].innerHTML = "&lt; 마루 밑 아리에티 &gt;";
    content[0].innerHTML = "장르 : 애니메이션, 판타지<br>" +
        "상영 시간 : 94분<br>" +
        "국내 등급 : 전체 관람가<br>" +
        "<br>" +
        "10cm 소녀 아리에티, 마루 위 인간 세상으로 뛰어들다!<br>" +
        "교외에 위치한 오래된 저택의 마루 밑에는 인간들의 물건을 몰래 빌려 쓰며 살아가는 소인들이 살고 있다.<br>"+
        "그들 세계의 철칙은 인간에게 정체를 들키면 그 집을 당장 떠나야 한다는 것!<br>" +
        "14살이 된 10cm 소녀 아리에티는 부모님의 도움 없이 홀로 마루 위 인간 세상으로 뛰어든다.<br>" +
        "빨래집게로 머리를 질끈 묶으면 작업 준비 완료! 작업 첫 날, 인간 소년 쇼우에게 정체를 들키다!";
    a[0].href = "https://movie.naver.com/movie/bi/mi/basic.naver?code=73301"
    a[1].href = "https://www.netflix.com/search?q=%EB%A7%88%EB%A3%A8%20%EB%B0%91&jbv=70216227"
}

function three() {
    poster[0].src = "poster/totoro.jpg";
    iframe[0].src = "https://www.youtube.com/embed/yrqmx630BIA?start=15";
    movie[0].innerHTML = "&lt; 이웃집 토토로 &gt;";
    content[0].innerHTML = "장르: 애니메이션, 가족, 판타지 <br>" +
        "상영 시간 : 87분 <br>" +
        "국내 등급 : 전체 관람가<br>" +
        "<br>" +
        "숲속에 살고 있는 특별한 친구를 만났다!<br>" +
        "<br>" +
        "도시를 떠나 시골로 이사 온 ‘사츠키’와 ‘메이’는 우연히 숲속에 살고 있는 신비로운 생명체 ‘토토로’를 만나 신비한 모험을 함께 한다.<br>" +
        "그러던 어느 날, 어머니의 병원에서 위태로운 소식이 도착하고 언니 ‘사츠키’가 정신없이 아빠에게 연락을 취하는 와중에<br>" +
        "‘메이’가 행방불명 되는데…";
    a[0].href = "https://movie.naver.com/movie/bi/mi/basic.naver?code=18781"
    a[1].href = "https://www.netflix.com/search?q=%ED%86%A0%ED%86%A0%EB%A1%9C&jbv=60032294"
}