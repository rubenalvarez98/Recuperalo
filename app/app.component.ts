import { Component } from '@angular/core';
@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
})
export class AppComponent {
  public appPages = [
    { title: 'Registrar', url: '/registrar', icon: 'add-circle' },
    { title: 'Buscar', url: '/buscar', icon: 'search' },
    { title: 'Perfil', url: '/perfil', icon: 'person' },
    { title: 'Archivo', url: '/archivo', icon: 'folder' },

  ];

}
