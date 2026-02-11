import { Component } from "@angular/core";
import { CardContent } from "./conteudo";

@Component({
    selector: "app-cartas",
    standalone: true,
    imports: [CardContent],
    template: `<section>
    <h1>Cartas</h1>
    <div>Barra</div>
    <div>
        <card-content/>

    </div>
    </section>`
})
export class Cartas {
    index: number = 2;
}