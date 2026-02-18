import { Component, input, computed } from "@angular/core";
import { DecimalPipe } from "@angular/common";

@Component({
    selector: "progress-bar",
    standalone: true,
    imports: [DecimalPipe],
    styleUrl: "./progress.css",
    template: `
    <span class="progress-bar" [style.width.%]="percentage()">    
        <progress 
            [value]="percentage()"
            max="100"
        ></progress> 
        {{percentage() | number: '1.0-0' }}% 
    </span>

    <span class="card-total">{{index() + 1}} de {{cardLength()}}</span>`
})
export class ProgressBar {
    index = input(0);
    cardLength = input(1);
    percentage = computed(() =>
        ((this.index() + 1) * 100 / this.cardLength()).toFixed(0)
    );
}