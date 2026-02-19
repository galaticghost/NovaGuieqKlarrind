import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { Component } from "@angular/core";
//import { Teste } from "./primeirosTestes/teste";
import { Cartas } from "./cartas/cartas";

@Component({
  selector: "app-root",
  standalone: true,
  styleUrl: "styles.css",
  imports: [Cartas],
  template: `<app-cartas class="app-cartas">`
})
class App { }

bootstrapApplication(App, appConfig)
  .catch((err) => console.error(err));
