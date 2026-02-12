import { Component, input } from "@angular/core";

@Component({
    selector: "card-content",
    standalone: true,
    template: `
    <p>@if (!showAnswer()){
        {{ pergunta() }}
        } @else {
        {{ resposta() }}
        }
    </p>
    `
})
export class CardContent {
    showAnswer = input(false);
    pergunta = input("");
    resposta = input("");
}