const arrey = ["bola","men","satanismo"];
console.log(arrey);

arrey.pop();

console.log(arrey);

arrey.unshift("Homens");
console.log(arrey.indexOf("men"));
console.log(arrey);
arrey.shift();
console.log(arrey);


// Bolamen

const xina = {
    nome: "Xinamen",
    pais: "China",
    bolajoe: true,
    every: function(){
        alert(this.bolajoe+" "+this.pais+" "+this.nome);
    }
};

console.log(xina.bolajoe);
xina.every();

