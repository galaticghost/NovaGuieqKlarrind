import { useState } from "react";
import { List } from "./components/List.tsx";

export default function App(){
    
    const listaInicial = ["bola","nola","cola"];
    const [lista,setLista] = useState(listaInicial);
    const [novoNome,setNovoNome] = useState("s");
    
    const xina = lista.map((nome,index) => <li key={index}>{nome}</li>);
    
    function addLista(){
        const a = lista.concat(novoNome);
        setLista(a);
        setNovoNome("s");
    }

    return (
        <div>
            <List>{xina}</List>
            <input
                type="text"
                onChange={(event) => setNovoNome(event.target.value)}
                value={novoNome}
            />
            <button onClick={addLista}>CLique</button>
        </div>
    );
}