# Uso de memoria

### Uso de memoria de AzerothCore

AzerothCore está basado en SunwellCore (un fork de TC). SunwellCore era un servidor público con más de 4000 jugadores en línea, y se aseguraron de que su núcleo pudiera manejar tal cantidad de jugadores fácilmente. La lectura de datos desde ram es mucho más rápida que la lectura del disco duro (hay sistemas enteros basados en este principio). Esa es una de las razones por las cuales hay un mayor uso de la ram.

#### Requisitos de RAM

| Número de jugadores | Requisitos mínimos de RAM |
|---------------------|---------------------------|
| 1-5                 |   4 GB                    |
| 10                  |   6 GB                    |
| 100                 |  16 GB                    |
| >100                | >16 GB                    |

Recomendamos por lo menos 16 GB, ya que el servidor irá almacenando en caché los mapas del mundo a medida que los jugadores los exploren, lo que finalmente supone un uso de al menos 11 GB de RAM.

Significa que aunque tengas pocos jugadores conectados, en el momento cuando exploren cualquier mapa, éste nunca se descargará de la RAM hasta el reinicio. Así que después de bastante tiempo, todos los mapas se cargarán, ocupando más RAM.
Es una elección estructural que garantiza un "alto rendimiento" en caso de un uso intensivo.

![ram](https://i.imgur.com/X3GBBbD.jpg)