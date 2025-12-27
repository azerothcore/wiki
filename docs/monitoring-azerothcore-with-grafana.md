---
tableofcontents: 1
---

# Monitoring AzerothCore with Grafana

## Required Software

1. [Influx DB](https://www.influxdata.com/products/influxdb-overview/) - a time-series data storage.

2. [Grafana](https://grafana.com/) - graph and a dashboard builder for visualizing time series metrics.

{% include note.html content="While we do support sending metrics, and connecting to Influx DB v2, our Grafana dashboard setups do not. Therefore, to visualize the data with Grafana you do need to run Infux DB v1. However, you can use [Chronograf](#additional-visualizations-and-metrics-collection) to visulize it, but you need to set that up yourself. " %}

{% include note.html content="We do not support Influx DB v3." %}

### Installing Influx DB

1. Download and install InfuxDB version 1.x from https://portal.influxdata.com/downloads/ for your operating system. (Version 2.x is currently not supported.)

2. Start InfuxDB

3. Create a user and a database in InfluxDB using the Influx CLI and executing the commands below:

```sql
CREATE DATABASE worldserver
CREATE USER grafana WITH PASSWORD 'grafana'
GRANT READ ON worldserver TO grafana
```

4. The token you get after creating a user is very important, both in grafana and in the worldserver config.

### Installing Grafana

1. Download and install Grafana from https://grafana.com/docs/grafana/latest/installation/

2. Open the dashboard at http://localhost:3000

3. Login with username *admin* and password *admin* (defaults can be changed in Grafana's .ini file. In newer versions of Grafana you will be prompted to change this at first login.)

4. Hover the cogwheel and select Data Sources

5. Search for InfluxDB and select.

6. Fill in the required data below.

```
Name: Influx
Type: InfluxDB
Url: http://localhost:8086
Access: Server
Database: worldserver User: grafana Password: grafana
```

1. Press Save & Test which should give you a green checkbox that says "Data source is working".

1. Hover the + and select Import and import each .json file from [AzerothCore's /apps/grafana](https://github.com/azerothcore/azerothcore-wotlk/tree/master/apps/grafana).

### Configuring AzerothCore

1. Edit the worldserver.conf file

1. Set `Metric.Enable` = 1

1. Edit `Metric.ConnectionInfo` with connection details (e.g "127.0.0.1;8086;worldserver")

1. Start worldserver, the dashboard should now start recieving values.

## Implemented and planned metrics

Implemented (✔) and planned (❌) metrics:

### Technical oriented

* I/O networking trafic
    * Packets sent ❌
    * Packets recieved ✔
    * Average ping ❌
    * Traffic in ❌
    * Traffic out ❌
* World session update time ✔
* Map update time ✔
* Map loads/unloads ✔
* MMap queries ✔
* Database async queries queued count ✔
* Server uptime ✔ (through world initialize and world shutdown events)
* Active connections ❌
* Queued connections ❌

### Game oriented

* Players online ✔
* Logins per hour/day/week etc ✔
* Mails sent ❌
* Auction house usage ❌
* Character levels ❌
* Gold earn/spend ❌
* LFG queues ❌

We'd like help implementing these and other metrics, feel free to send us a [pull request](https://github.com/azerothcore/azerothcore-wotlk/pulls).

## Adding new metrics

There are two kinds of metrics that can be logged: values and events.

Values correspond to measurements of a certain quantity, like number of online players of the update diff time.

Events are something that occurs in an instant of time, e.g, a player login, worldserver shutdown, etc...

To log new metrics, call `METRIC_EVENT` or `METRIC_VALUE` and add a new graph to the dashboard.

`METRIC_EVENT(category, title, description)`

- **category**: Arbitrary string, table where the values and events are stored. By convention, event logs should be suffixed by "_events".

- **title**: Name of the event log.

- **description**: Additional info about a log event.

`METRIC_VALUE(category, value)`

- **category**: Arbitrary string, table where the values and events are stored. By convention, event logs should be suffixed by "_value".

- **value**: A measurment, it can have one of the following types: bool, std::string, float, double, or any integral type (int, int32, uint, etc...).

**Examples**

```cpp
// Registering player logins: in WorldSession::HandlePlayerLogin(LoginQueryHolder* holder)
METRIC_EVENT("player_events", "Login", pCurrChar->GetName());
  
// Logging the update diff time: in World::Update(uint32 diff)
METRIC_VALUE("update_time_diff", diff);
```

## Additional Reading

Lean more about InfluxDB and Grafana:

* [InfluxDB website](https://influxdata.com/time-series-platform/influxdb/)
* [InfluxDB documentation (v1.8)](https://docs.influxdata.com/influxdb/v1.8/)
* [Grafana website](http://grafana.org/)
* [Grafana documentation](http://docs.grafana.org/)
* [Grafana live demo](http://play.grafana.org/)
* [Adding InfluxDB to Grafana](http://docs.grafana.org/datasources/influxdb/)

## InfluxDB v2

1. Download InfluxDB v2
2. Start InfluxDB
3. Head to http://127.0.0.1:8086
4. Create User
```
Username: grafana
Password: grafana
Initial Organization Name: Grafana
Initial Bucket Name: worldserver
```

[Use for example Chronograf to visualize the data.](#additional-visualizations-and-metrics-collection)

## Additional visualizations and metrics collection

InfluxDB is part of a bigger set of projects by [InfluxData](https://www.influxdata.com/) which integrate nicely with the DB:

- [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/) can be used to collect system metrics like CPU, I/O, memory usage and other services such as MySQL – to display this info next to the AC metrics.

- [Chronograf](https://www.influxdata.com/time-series-platform/chronograf/) is an alternative to Grafana to graph and visualize time-series metrics.

- [Kapacitator](https://www.influxdata.com/time-series-platform/kapacitor/) is able to process streaming data from InfluxDB to provide alerts, trigger events, detect anomalies or transform data.
