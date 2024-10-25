const objetox = {
    nome:"Bolamen",
    nacionalidade:"China",
    bola:true,
    idade:34,
    xina: function(a){
        return a * 5;
    }
};

function showJoe(objetct){
    let ola = 0;
    for (let chaina in objetct){
        ola += 1;
        console.log("UNO DOS " + " " + ola + " " + objetct[chaina]);
    }
}

console.log(3.352.toFixed(1));

showJoe(objetox); 
