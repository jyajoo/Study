p = document.getElementById('text')
btn = document.getElementById('btn')
function click() {
    setTimeout(() => {
        p.innerHTML = "모각코";
        btn.innerHTML = "010-XXXX-XXXX"
    }, 2000);
    
}

btn.addEventListener('click', click)
