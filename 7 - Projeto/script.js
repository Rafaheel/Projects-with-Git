function insert(num) {
    document.form.textview.value = document.form.textview.value + num
}

function equal() {
    var exp = document.form.textview.value;
    if (exp) {
        document.form.textview.value = eval(exp)
    }

}

function clean() {
    document.form.textview.value = "";
}


function back() {
    var exp = document.form.textview.value;
    document.form.textview.value = exp.substring(0, exp.length - 1);

}


function relogio() {
    var data = new Date();
    var hora = data.getHours();
    var min = data.getMinutes();
    var seg = data.getSeconds();

    if (hora < 10) {
        hora = '0' + hora;
    }
    if (min < 10) {
        min = '0' + min;
    }
    if (seg < 10) {
        seg = '0' + seg;
    }

    var horas = hora + ':' + min + ':' + seg;
    document.getElementById('rel').value = horas;

}
var tempo = setInterval(relogio, 1000);