alert('Olá mundo!, falo do arquivo script.js');

const jimNascimento = '27/11/1942';
const jimFalecimento = '18/09/1970';

alert(jimNascimento + " " + jimFalecimento);
console.log(jimNascimento + " " + jimFalecimento);

const nomeUsuario = prompt("Qual seu nome?");
console.log(nomeUsuario);

const fruta = prompt("Me de um nome de uma fruta")

if (fruta.toLowerCase() === 'laranja'){
    console.log("Não se esqueça de descascar?");
}
else if (fruta.toLowerCase() === 'maçã'){
    console.log("Se você tirar a casca perderá as vitaminas!");
}
else if (fruta.toLowerCase() === 'banana'){
    console.log("Já vem naturalmente embalada e é muito foda");
}
else {
    console.log("Mamao não é uma fruta, pêra não é uma fruta, abacate não é uma fruta e " + fruta + " JAMAIS SERA UMA FRTUAAAA@!@!!!!!");
};

const dinheiroQueRecebi = prompt("DIGITER UMR NUMER");
const valorDoProduto = prompt('Digite o valor do produto');
if (dinheiroQueRecebi > valorDoProduto) {
    let troco = dinheiroQueRecebi - valorDoProduto;
    alert("Tu troco é igual as " + troco);
}
else {
    alert('CADE A PORRA DO DINHERO RESTANTE?');
};

function filhoDaPutaFunction(str,indice){
    return str[indice];
};

const a = filhoDaPutaFunction('TAPORA',3);
const s = filhoDaPutaFunction('TAPORA',2)
console.log(a);
console.log(s);

function htos(hora){
    return hora * 3600;
}

const hora = htos(23);
console.log(hora)

function dinheiro(dinero){
    return "R$:" + dinero;
}

const numeros = [2,1,3,4]

function doubleNumbers(list){
    let doubleNumber = []
    for(let x of list){
        doubleNumber.push(x * 2);
    }
    return doubleNumber;
}

const doubleNumeros = doubleNumbers(numeros);

console.log(doubleNumeros);

function parOuImpar(numero){
    if ((numero % 2) === 1){
        return 'impar';
    }
    else{
        return 'par';
    }
}

const xina = parOuImpar(5);
const xina2 = parOuImpar(4);
console.log(xina + xina2);

function invertString(str){
    return str.split("").reverse().join("");
}

const futuro = invertString("FUTURO!");
console.log(futuro);

function futuro2(str,indice){
    return str.slice(indice);
}

function futuro3(str,indice){
    return str.slice(0,indice);
}

console.log(futuro2("FUturo?",2));
console.log(futuro3('FUTURO!',5));