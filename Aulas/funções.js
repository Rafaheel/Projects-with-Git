

function soma() {
    var resultado = 0
    for(var i in arguments) {
        resultado += arguments
        console.log(arguments[i])
    }     

    return resultado
}

console.log(soma(7,5,3.2))