
Makefile:
```
install              Install dependencies
deploy               Deploy project (migrate database)
run                  Run project server development
createuser           Create user (as superuser)
createdefaultuser    Create user default (as superuser)
```

## Features:
- [ ] permitir que se ingresen diversos trayectos.
- [ ] Cada trayecto tendrá varios buses asignados a distintos horarios.
- [ ] Cada bus tendrá un solo chofer y varios pasajeros asignados a sus asientos.
- [ ] Todos los buses tienen la misma capacidad de 10 pasajeros sentados.
- [ ] Los asientos son numerados y se reservan para cada pasajero.
- [ ] El sistema debe soportar el ingreso de pasajeros a un trayecto y horario en particular
- [ ] Asignación de choferes a sus respectivos buses.

## Forms Views:
- [ ] CRUD pasajeros, choferes, trayectos, buses.
- [ ] Listar los trayectos junto a su promedio de pasajeros.
- [ ] Filtrar a todos los buses de un trayecto con más del N % de su capacidad vendida.
- [ ] Para la implementación hay que utilizar el Django y su ORM.

## Restrictions
- [x] Utilizar Vue.js, Django APIRest Framework.