---
tableofcontents: 1
---

# Monitorizar AzerothCore con Grafana

## Software requerido

1. [Influx DB](https://www.influxdata.com/products/influxdb-overview/) - un almacenamiento de datos de series temporales.

2. [Grafana](https://grafana.com/) - un constructor de gráficos y dashboards para visualizar métricas de series temporales.

{% include note.html content="While we do support sending metrics, and connecting to Influx DB v2, our Grafana dashboard setups do not. Therefore, to visualize the data with Grafana you do need to run Infux DB v1. However, you can use [Chronograf](#additional-visualizations-and-metrics-collection) to visualize it, but you need to set that up yourself. " %}

{% include note.html content="We do not support Influx DB v3." %}

### Instalar Influx DB

1. Descarga e instala InfluxDB versión 1.x desde https://portal.influxdata.com/downloads/ para tu sistema operativo. (La versión 2.x no está soportada actualmente.)

2. Inicia InfluxDB

3. Crea un usuario y una base de datos en InfluxDB usando la CLI de Influx y ejecutando los comandos de abajo:

```sql
CREATE DATABASE worldserver
CREATE USER grafana WITH PASSWORD 'grafana'
GRANT READ ON worldserver TO grafana
```

4. El token que obtienes tras crear un usuario es muy importante, tanto en grafana como en la configuración del worldserver.

### Instalar Grafana

1. Descarga e instala Grafana desde https://grafana.com/docs/grafana/latest/installation/

2. Abre el dashboard en http://localhost:3000

3. Inicia sesión con el usuario *admin* y la contraseña *admin* (los valores por defecto se pueden cambiar en el archivo .ini de Grafana. En versiones más nuevas de Grafana se te pedirá que lo cambies en el primer inicio de sesión.)

4. Pasa el ratón sobre el engranaje y selecciona Data Sources

5. Busca InfluxDB y selecciónalo.

6. Rellena los datos requeridos de abajo.

```
Name: Influx
Type: InfluxDB
Url: http://localhost:8086
Access: Server
Database: worldserver User: grafana Password: grafana
```

1. Pulsa Save & Test, lo que debería darte una casilla verde que dice "Data source is working".

1. Pasa el ratón sobre el + y selecciona Import e importa cada archivo .json desde [/apps/grafana de AzerothCore](https://github.com/azerothcore/azerothcore-wotlk/tree/master/apps/grafana).

### Configurar AzerothCore

1. Edita el archivo worldserver.conf

1. Establece `Metric.Enable` = 1

1. Edita `Metric.ConnectionInfo` con los detalles de conexión (p. ej. "127.0.0.1;8086;worldserver")

1. Inicia el worldserver; el dashboard debería empezar a recibir valores ahora.

## Métricas implementadas y planificadas

Métricas implementadas (✔) y planificadas (❌):

### Orientadas a lo técnico

* Tráfico de red I/O
    * Paquetes enviados ❌
    * Paquetes recibidos ✔
    * Ping medio ❌
    * Tráfico entrante ❌
    * Tráfico saliente ❌
* Tiempo de actualización de la sesión del mundo ✔
* Tiempo de actualización del mapa ✔
* Cargas/descargas de mapas ✔
* Consultas MMap ✔
* Recuento de consultas asíncronas de BD en cola ✔
* Uptime del servidor ✔ (mediante los eventos de inicialización y apagado del mundo)
* Conexiones activas ❌
* Conexiones en cola ❌

### Orientadas al juego

* Jugadores online ✔
* Inicios de sesión por hora/día/semana, etc. ✔
* Correos enviados ❌
* Uso de la casa de subastas ❌
* Niveles de personaje ❌
* Oro ganado/gastado ❌
* Colas de LFG ❌

Nos gustaría recibir ayuda para implementar estas y otras métricas; siéntete libre de enviarnos un [pull request](https://github.com/azerothcore/azerothcore-wotlk/pulls).

## Añadir nuevas métricas

Hay dos tipos de métricas que se pueden registrar: valores y eventos.

Los valores corresponden a mediciones de una cierta cantidad, como el número de jugadores online o el tiempo del update diff.

Los eventos son algo que ocurre en un instante de tiempo, p. ej., un inicio de sesión de un jugador, el apagado del worldserver, etc...

Para registrar nuevas métricas, llama a `METRIC_EVENT` o `METRIC_VALUE` y añade un nuevo gráfico al dashboard.

`METRIC_EVENT(category, title, description)`

- **category**: cadena arbitraria, tabla donde se almacenan los valores y eventos. Por convención, los logs de eventos deberían llevar el sufijo "_events".

- **title**: nombre del log de evento.

- **description**: información adicional sobre un evento de log.

`METRIC_VALUE(category, value)`

- **category**: cadena arbitraria, tabla donde se almacenan los valores y eventos. Por convención, los logs de eventos deberían llevar el sufijo "_value".

- **value**: una medición; puede tener uno de los siguientes tipos: bool, std::string, float, double, o cualquier tipo integral (int, int32, uint, etc...).

**Ejemplos**

```cpp
// Registering player logins: in WorldSession::HandlePlayerLogin(LoginQueryHolder* holder)
METRIC_EVENT("player_events", "Login", pCurrChar->GetName());
  
// Logging the update diff time: in World::Update(uint32 diff)
METRIC_VALUE("update_time_diff", diff);
```

## Lectura adicional

Aprende más sobre InfluxDB y Grafana:

* [Web de InfluxDB](https://influxdata.com/time-series-platform/influxdb/)
* [Documentación de InfluxDB (v1.8)](https://docs.influxdata.com/influxdb/v1.8/)
* [Web de Grafana](http://grafana.org/)
* [Documentación de Grafana](http://docs.grafana.org/)
* [Demo en vivo de Grafana](http://play.grafana.org/)
* [Añadir InfluxDB a Grafana](http://docs.grafana.org/datasources/influxdb/)

## InfluxDB v2

1. Descarga InfluxDB v2
2. Inicia InfluxDB
3. Ve a http://127.0.0.1:8086
4. Crea el usuario
```
Username: grafana
Password: grafana
Initial Organization Name: Grafana
Initial Bucket Name: worldserver
```

[Usa por ejemplo Chronograf para visualizar los datos.](#additional-visualizations-and-metrics-collection)

## Visualizaciones adicionales y recopilación de métricas

InfluxDB forma parte de un conjunto mayor de proyectos de [InfluxData](https://www.influxdata.com/) que se integran muy bien con la BD:

- [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/) se puede usar para recopilar métricas del sistema como CPU, I/O, uso de memoria y otros servicios como MySQL, para mostrar esta información junto a las métricas de AC.

- [Chronograf](https://www.influxdata.com/time-series-platform/chronograf/) es una alternativa a Grafana para graficar y visualizar métricas de series temporales.

- [Kapacitator](https://www.influxdata.com/time-series-platform/kapacitor/) es capaz de procesar datos en streaming de InfluxDB para proporcionar alertas, disparar eventos, detectar anomalías o transformar datos.
