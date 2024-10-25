const p = document.getElementById("modafoca");
const f = document.getElementById("fundo");
const conts = document.getElementById("counter");
const button = document.getElementById("bottao");
const aaaa = document.querySelectorAll(".aaa")
const end = document.getElementById("acabo");

let fundo = document.body;
let contador = 0;
function trocaTexto(){
    p.innerHTML = "Bolas";

}

function trocaFundo(){
    a = randomIntFromInterval(0,255);
    b = randomIntFromInterval(0,255);
    c = randomIntFromInterval(0,255);
    fundo.style.backgroundColor = "rgb("+a+","+b+","+c+")";
}

function trocaCor(sadf){
    a = randomIntFromInterval(0,255);
    b = randomIntFromInterval(0,255);
    c = randomIntFromInterval(0,255);
    sadf.style.color = "rgb("+a+","+b+","+c+")";
}

function trocaTexto2(){
    p.innerHTML = "O modafoca Twelve Men";
}

function counterGuiltyGear(){
    contador += 1;
    conts.innerHTML = contador;
}

function randomIntFromInterval(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}
let olhar = true
function ver(){
    if (olhar){
    document.getElementById("div-do-bola").style.display = "None";
    } else {
        document.getElementById("div-do-bola").style.display = "Block";
    }
    olhar = !olhar
}

function helpme(){
    for (asd of aaaa){
        trocaCor(asd);
    }
}

p.onclick = trocaTexto;
f.onclick = trocaFundo;
button.onclick = counterGuiltyGear;
document.getElementById("botaodobola").onclick = ver;

document.getElementById("aa").onclick = helpme;

function addLista(){
    const ueli = document.getElementById("charlos");
    const carlis = document.createElement("li");
    carlis.innerText = "FUNCIONA POR FAVOR";
    ueli.appendChild(carlis);
}

const boton = document.getElementById("bolajoedois");

boton.onclick = addLista;

const lista = document.getElementById("lista");

function countLista(){
    let xsd = lista.children.length;
    document.getElementById("listaconta").innerText = xsd;
}
end.onclick = countLista;
