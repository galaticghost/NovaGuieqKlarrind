const trinta = document.getElementById("listasdois");
const dois = document.getElementById("botao");
const tres = document.getElementById("boto");

function addCoisa(){
    let bola = document.createElement("li");
    bola.innerHTML = "fosad";
    bola.classList.add("AADSIJFI")
    trinta.appendChild(bola);
}

function deleteDois(){
    let sasf = document.getElementsByClassName("AADSIJFI")[0];
    sasf.remove();
}

dois.onclick = addCoisa;
tres.onclick = deleteDois;