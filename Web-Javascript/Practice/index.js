var h1 = document.getElementsByTagName('h1');
var cnt = 0;
var result = "";
var letter = ['코', "드", "메", "이", "트", "!"];
var colors = ['red', 'orange', 'green', 'blue', 'purple', 'pink']

function go() {
    result += letter[cnt];
    h1[0].style.color = colors[cnt]
    h1[0].innerHTML = result
    cnt++;
    if (cnt == 6) {
        cnt = 0;
        result = "";
    }
}