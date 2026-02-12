import { Barra } from "./barra";
import { CardContent } from "./conteudo";
import { Component, signal, WritableSignal } from "@angular/core";
import jsonData from "./conteudo.json";

type Content = {
    pergunta: string,
    resposta: string
}

@Component({
    selector: "app-cartas",
    standalone: true,
    imports: [CardContent, Barra],
    styleUrl: "./styles.css",
    template: `<section>
    <h1>Cartas</h1>
    <barra [index]="index()" [cardLength]="content.length" />
    <div>
        <card-content 
        [showAnswer]='showAnswer()'
        [pergunta]='currentCard.pergunta'
        [resposta]='currentCard.resposta'
        />
        <button [disabled]="isFirstCard()"(click)='prev()'>Anterior</button>
        <button (click)='toggleAnswer()'>{{ showAnswer() ? "Esconder resposta" : "Mostrar resposta" }}</button>
        <button [disabled]="isLastCard()" (click)='next()'>Próximo</button> 
    </div>
    </section>`
})
export class Cartas {
    showAnswer: WritableSignal<boolean> = signal(false);
    index: WritableSignal<number> = signal(0);
    content: Content[] = jsonData;

    get currentCard(): Content {
        return this.content[this.index()];
    };

    toggleAnswer(): void {
        this.showAnswer.update((answer) => answer = !answer);
    };

    prev(): void {
        console.log(jsonData);
        this.showAnswer.set(false);
        this.index.update((i) => i - 1);
    };

    next(): void {
        this.showAnswer.set(false);
        this.index.update((i) => i + 1);
    };

    isFirstCard(): boolean {
        return this.index() === 0;
    };

    isLastCard(): boolean {
        return this.index() === this.content.length - 1;
    };


}