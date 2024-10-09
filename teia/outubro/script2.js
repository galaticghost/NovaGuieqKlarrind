function dinheiro(dinero){
    return dinero * 100;
}

console.log(dinheiro(2.5));

function isPalindromo(str){
    if (str.toLowerCase() === str.split("").reverse().join("").toLowerCase()) {
        return true;
    }
    else {
        return false;
    }
}

console.log(isPalindromo("Bola"));
console.log(isPalindromo("Kayak"));

function wordsToNumbers(numeros){
    if (Number.isInteger(numeros)){
        switch (numeros.toLowerCase()){
            case "zero":
                return 0;
            case "um":
                return 1;
            case "dois":
                return 2;
            case "três":
                return 3;
            case "quatro":
                return 4;
            case "cinco":
                return 5;
            case "seis":
                return 6;
            case "sete":
                return 7;
            case "oito":
                return 8;
            case "nove":
                return 9;
            default:
                return "Número inválido";
        }
    }
    else if (Array.isArray(numeros)) {
        let arrayNumeros = [];

        for (numero of numeros){
            switch (numero){
                case "zero":
                    arrayNumeros.push(0);
                    break;
                case "um":
                    arrayNumeros.push(1);
                    break;
                case "dois":
                    arrayNumeros.push(2);
                    break;
                case "três":
                    arrayNumeros.push(3);
                    break;
                case "quatro":
                    arrayNumeros.push(4);
                    break;
                case "cinco":
                    arrayNumeros.push(5);
                    break;
                case "seis":
                    arrayNumeros.push(6);
                    break;
                case "sete":
                    arrayNumeros.push(7);
                    break;
                case "oito":
                    arrayNumeros.push(8);
                    break;
                case "nove":
                    arrayNumeros.push(9);
                    break;
                default:
                    return "Número inválido";
            }
        }
        return arrayNumeros;
    }
    else {
        return null;
    }
}

console.log(wordsToNumbers(["oito","sete"]));