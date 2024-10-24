const datas = document.getElementById("clickers");
const dias = document.getElementById("datas");
const wa = document.getElementById("idade");

function getDatas(){
    let aniversario = dias.value
    if (aniversario === ''){
        alert('Insira um data');
    }
    else{
        let diasHoje = new Date();
        let resposta = calculateIdadei(diasHoje,aniversario);
        wa.innerHTML = "Você tem " + resposta + " anos.";
    }
}

function calculateIdadei(diasHoje,aniversario){
    diasHoje = diasHoje.toISOString().split('T')[0]
    diasHoje = diasHoje.split('-');
    console.log(diasHoje);
    aniversario = aniversario.split('-');
    let idade = diasHoje[0] - aniversario[0];
    if (diasHoje[1] < aniversario[1]){
        return idade -1;
    } else if (diasHoje[1] === aniversario[1]){
        if (diasHoje[2] < aniversario[2]){
            return idade - 1;
        }
    }
    return idade;
}

datas.addEventListener("click",getDatas);