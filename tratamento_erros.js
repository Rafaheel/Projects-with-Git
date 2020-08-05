

var video = Array()

video[1] = Array()
video[1]['nome'] = 'Vingadores'
video [1]['categoria'] = 'Aventura'



function getVideo(params) {
    try {
        console.log(video[0] ['nome'])
    }
    catch (erro) {
        tratarErro (erro)
        console.log('Agora sim podemos tratar esse erro')
        throw new Error('Testando o Throw')
    }    
    finally {
        console.log('Sempre passa por aqui (try / catch)')
    }
    console.log('Aplicação não morreu')
}  

getVideo(video)


function tratarErro(e) {
    console.log('Testando a função de erro')
    
}