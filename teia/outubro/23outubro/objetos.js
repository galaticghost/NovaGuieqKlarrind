const objeto = {};
const objetox = {
    nome:"Bolamen",
    nacionalidade:"China",
    bola:true,
    idade:34,
    xina: function(a){
        return a * 5;
    }
};

console.log(objeto + " " + objetox.xina(3.5));

function showJoe(objetct, and){
    let ola = 0;
    for (let chaina in objetct){
        ola += 1;
        console.log("UNO DOS " + and + " " + ola + " " + objetct[chaina]);
    }
}

console.log(3.352.toFixed(1));

showJoe(objetox,"QUAUQUQUU");