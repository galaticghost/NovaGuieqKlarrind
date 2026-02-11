import { Component, signal, WritableSignal } from "@angular/core";

type Conteudo = {
    pergunta: string,
    resposta: string
}

@Component({
    selector: "card-content",
    standalone: true,
    template: `
    <p>@if (!showAnswer()){
        {{ currentCard.pergunta }}
        } @else {
        {{ currentCard.resposta }}
        }
    </p>
    <button [disabled]="isPrevBtnValid()"(click)='prev()'>Anterior</button>
    <button (click)='toggleAnswer()'>{{ showAnswer() ? "Esconder resposta" : "Mostrar resposta" }}</button>
    <button [disabled]="isNextBtnValid()" (click)='next()'>Próximo</button> 
    `
})
export class CardContent {
    showAnswer: WritableSignal<boolean> = signal(false);
    index: WritableSignal<number> = signal(0);

    toggleAnswer(): void {
        if (this.showAnswer() === false) {
            this.showAnswer.set(true);
        } else {
            this.showAnswer.set(false);
        }
    }

    prev(): void {
        this.showAnswer.set(false);
        this.index.update((num) => num - 1);
    };
    next(): void {
        this.showAnswer.set(false);
        this.index.update((num) => num + 1);
    };
    //todo
    isPrevBtnValid(): boolean {
        if (this.index() === 0) {
            return true;
        } else {
            return false;
        }
    }
    //todo
    isNextBtnValid(): boolean {
        if (this.index() === 0) {
            return false;
        } else {
            return true;
        }
    }

    conteudo: Array<Conteudo> = [
        {
            pergunta: "xinamen",
            resposta: "xina2?"
        },
        {
            pergunta: "xina22men",
            resposta: "xina2ss?"
        },
    ];

    get currentCard(): Conteudo {
        return this.conteudo[this.index()];
    }
}