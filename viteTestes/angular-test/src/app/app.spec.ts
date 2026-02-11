import { TestBed } from '@angular/core/testing';
import { App2 } from './app';

describe('App', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [App2],
    }).compileComponents();
  });

  it('should create the app', () => {
    const fixture = TestBed.createComponent(App2);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it('should render title', async () => {
    const fixture = TestBed.createComponent(App2);
    await fixture.whenStable();
    const compiled = fixture.nativeElement as HTMLElement;
    expect(compiled.querySelector('h1')?.textContent).toContain('Hello, angular-test');
  });
});
