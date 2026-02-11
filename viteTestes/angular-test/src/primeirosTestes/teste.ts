import { Bola3 } from '../app/bola-test';
import { Event2 } from '../app/event2';
import { Component, signal } from '@angular/core';

@Component({
    selector: 'app-test',
    standalone: true,
    imports: [Bola3, Event2],
    template: `
  <h1>Hello {{bola}} </h1>
  @if (bola === 'angular 7') {
    <button (click)="bola = 'xinamen'">Xinamen?</button>
  } @else {
    <button (click)="bola = 'angular 7'">Xinamen?</button>
  }
  <h2> Testes {{ valor() }}</h2>
  <button (click)="xina()">sd</button>

  <app-bola3/>
  <event/>
  `
})

export class Teste {
    bola = 'angular 7';
    valor = signal('123');
    xina() {
        if (this.valor() === '123') {
            this.valor.set('234')
        } else {
            this.valor.set('123');
        }
    };
}