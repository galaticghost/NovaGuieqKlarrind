import { Component, input } from "@angular/core";

@Component({
    selector: "card-content",
    standalone: true,
    template: `
    <p>@if (!showAnswer()){
        {{ question() }}
        } @else {
        {{ answer() }}
        }
    </p>
    `
})
export class CardContent {
    showAnswer = input(false);
    question = input("");
    answer = input("");
}