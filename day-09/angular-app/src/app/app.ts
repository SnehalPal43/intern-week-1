import { Component, signal } from '@angular/core';
import { DashboardComponent } from './components/dashboard/dashboard';

@Component({
  selector: 'app-root',
  imports: [DashboardComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('angular-app');
}