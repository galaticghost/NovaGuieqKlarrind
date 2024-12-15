function somadora(n,n2,myFunction){
    const resultado = n + n2;
    myFunction(resultado);
}

function birus(resultado){
    document.getElementById("buela").innerHTML = resultado;
}

somadora(1,2,birus);

let promessa = new Promise(function(resolve,reject){
    let g = 6;

    if (g == 2){
        resolve("Pica");
    } else {
        reject("qua,qua,qua,quaaa");
    }
});

promessa.then(
    function(value) {birus(value);},
    function(error) {birus(error);}
);