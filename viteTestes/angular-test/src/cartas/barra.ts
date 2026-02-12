import { Component, input, numberAttribute, signal, computed } from "@angular/core";
import { DecimalPipe } from "@angular/common";

@Component({
    selector: "barra",
    standalone: true,
    imports: [DecimalPipe],
    template: `<div>
    <progress 
        [value]="percentage()"
        max="100"
    > 
    </progress>
    <span> {{percentage() | number: '1.0-0' }}% </span>
    <span>{{index() + 1}} de {{cardLength()}}</span>
    </div>`
})
export class Barra {
    index = input(0);
    cardLength = input(1);
    percentage = computed(() =>
        (this.index() + 1) * 100 / this.cardLength()
    );
}