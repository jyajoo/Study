var h = m = s = cnt = 0;
var time;
var h1 = document.getElementsByTagName('h1');

function start() {
    if (cnt == 0) {  // start 버튼이 여러 번 눌리는 것을 방지
        timer();
        cnt++;
    }
}

function timer() {
    time = setTimeout(tick, 1000);  // 1초 뒤에 tick 함수 실행
}

function stop() {
    clearTimeout(time);   // 시간 측정 중지
    cnt = 0;
}

function reset() {
    stop();           // 시간을 중지하고 초기화 한다.
    h1[0].innerHTML = "00:00:00";
    h = m = s = time = 0;
}

function tick() {
    s++;
    if (s > 60) {
        s = 0;
        m++;
        if (m > 60) {
            m = 0;
            h++;
        }
    }

    h1[0].innerHTML = (h > 9 ? h : "0" + h) + ":"
    + (m > 9 ? m : "0" + m) + ":"
    + (s > 9 ? s : "0" + s);
    
    if (h == 99 && m == 59 && s == 59) {
        stop();
        return;
    }
    timer();
}