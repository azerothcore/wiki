---
tableofcontents: 1
---

# Monitoring AzerothCore with Grafana

## Required Software

1. [Influx DB](https://www.influxdata.com/products/influxdb-overview/) - a time-series data storage.

1. [Grafana](https://grafana.com/) - graph and a dashboard builder for visualizing time series metrics.

### Installing Influx DB

1. Download and install InfuxDB from https://portal.influxdata.com/downloads/ for your operating system.

1. Start InfuxDB

1. Create a user and a database in InfluxDB using the Influx CLI and executing the commands below:

```sql
CREATE DATABASE worldserver
CREATE USER grafana WITH PASSWORD 'grafana'
GRANT READ ON worldserver TO grafana
```

### Installing Grafana

1. Download and install Grafana from https://grafana.com/docs/grafana/latest/installation/

1. Open the dashboard at http://localhost:3000

1. Login with username *admin* and password *admin* (defaults can be changed in Grafana's .ini file)

1. Go to Data Sources → + Add Data Source

```
Name: Influx
Type: InfluxDB
Url: http://localhost:8086
Access: Server
Database: worldserver User: grafana Password: grafana
```

1. Go to Dashboards → Import and import each .json file in [AzerothCore's /apps/grafana](https://github.com/azerothcore/azerothcore-wotlk/tree/master/apps/grafana).

### Configuring AzerothCore

1. Edit the worldserver.conf file

1. Set `Metric.Enable` = 1

1. Edit `Metric.ConnectionInfo` with connection details (e.g "127.0.0.1;8086;worldserver")

1. Start worldserver, the dashboard should now start recieving values.

## Implemented and planned metrics

We'd like help implementing these and other metrics, feel free to send us a [pull request](https://github.com/azerothcore/azerothcore-wotlk/pulls).


### Technical oriented

| Metric | Implemented | Planned | Comment |
| :----- | :---------: | :-----: | :------ |
| Packets sent | | x |
| Packets recieved | | x |
| Average ping | | x |
| Traffic in | | x |
| Traffic out | | x |
| World session update time | | x |
| Map update time | | x |
| Map loads/unloads | | x |
| MMap queries | | x |
| Database async queries queued count | | x |
| Server uptime | | x | through world initialize and world shutdown events |
| Active connections | | x |
| Queued connections | | x |

### Game oriented

| Metric | Implemented | Planned | Comment |
| :----- | :---------: | :-----: | :------ |
| Players online | | x |
| Logins per hour/day/week etc | | x |
| Mails sent | | x |
| Auction house usage | | x |
| Character levels | | x |
| Gold earn/spend | | x |
| LFG queues | | x |

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

## Additional visualizations and metrics collection

InfluxDB is part of a bigger set of projects by [InfluxData](https://www.influxdata.com/) which integrate nicely with the DB:

- [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/) can be used to collect system metrics like CPU, I/O, memory usage and other services such as MySQL – to display this info next to the AC metrics.

- [Chronograf](https://www.influxdata.com/time-series-platform/chronograf/) is an alternative to Grafana to graph and visualize time-series metrics.

- [Kapacitator](https://www.influxdata.com/time-series-platform/kapacitor/) is able to process streaming data from InfluxDB to provide alerts, trigger events, detect anomalies or transform data.
