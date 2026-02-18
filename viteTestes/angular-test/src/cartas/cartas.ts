import { ProgressBar } from "./progress-bar";
import { CardContent } from "./card-content";
import { Component, signal, WritableSignal } from "@angular/core";
import jsonData from "./conteudo.json";

type Content = {
    question: string,
    answer: string
}

@Component({
    selector: "app-cartas",
    standalone: true,
    imports: [CardContent, ProgressBar],
    styleUrl: "./styles.css",
    template: `
    <section class="cards-app">
        <h1 class="title">Cartas</h1>
        <progress-bar class="progress-bar" [index]="index()" [cardLength]="content.length" />
        <section class="card-content">
            <card-content class="card-text"
            [showAnswer]='showAnswer()'
            [question]='currentCard.question'
            [answer]='currentCard.answer'
            />
            <div class="card-buttons">
                <button class="button" [disabled]="isFirstCard()" (click)='prev()'>Anterior</button>
                <button class="button" (click)='toggleAnswer()'>{{ showAnswer() ? "Esconder resposta" : "Mostrar resposta" }}</button>
                <button class="button" [disabled]="isLastCard()" (click)='next()'>Próximo ></button> 
            </div>
        </section>
    </section>
    `
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