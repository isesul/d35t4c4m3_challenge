
Makefile:
```
install              Install dependencies
deploy               Deploy project (migrate database)
run                  Run project server development
createuser           Create user (as superuser)
createdefaultuser    Create user default (as superuser)
```

# Challenge

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
- [ ] Utilizar Vue.js, Django APIRest Framework.

# Todo

## Features definition

### Administrative functions
- [A1]: CRUD travel routes
- [A2]: CRUD buses
- [A3]: CRUD bus drivers
- [A4]: CRUD passengers
- [A5]: Assign driver to bus
- [A6]: Assign passengers to travel


### Public functions
- [B1]: Buy tickets
- [B2]: Sell tickets
- [B3]: Can list routes with their average passengers number.
- [B4]: Filter buses on a route with more than a certain N% (percentage number) of their capacity sold.

## Role definition
- Admin: 
    - Can: All
- TicketSeller:
    - Can: A6, B2, B3, B4
- Passenger
    - Can: B1

