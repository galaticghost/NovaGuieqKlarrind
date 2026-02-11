import { Component } from "@angular/core";

@Component({
    selector: "event",
    standalone: true,
    template: `<input type="text" (keyup.shift)="updateField($event)" />`
})
export class Event2 {
    updateField(event: any): void {
        console.log('The user pressed Shift in the text field.');
    }
}