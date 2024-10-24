const datas = document.getElementById("clickers");
const dias = document.getElementById("datas");
const wa = document.getElementById("idade");

function getDatas(){
    if (dias.value === ''){
        alert('Insira um data');
    }
    else{
        alert(dias.value);
        wa.innerHTML = dias.value;
        calculateIdadei();
    }
}

function calculateIdadei(){
    
}

datas.addEventListener("click",getDatas);