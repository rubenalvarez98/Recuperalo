import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'folder/Inbox',
    pathMatch: 'full'
  },
  {
    path: 'folder/:id',
    loadChildren: () => import('./folder/folder.module').then( m => m.FolderPageModule)
  },
  {
    path: 'registrar',
    loadChildren: () => import('./folder/registrar/registrar.module').then( m => m.RegistrarPageModule)
  },
  {
    path: 'buscar',
    loadChildren: () => import('./folder/buscar/buscar.module').then( m => m.BuscarPageModule)
  },
  {
    path: 'perfil',
    loadChildren: () => import('./folder/perfil/perfil.module').then( m => m.PerfilPageModule)
  },
  {
    path: 'archivo',
    loadChildren: () => import('./folder/archivo/archivo.module').then( m => m.ArchivoPageModule)
  }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
