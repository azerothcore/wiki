---
tableofcontents: 1
---

# 使用 Grafana 监控 AzerothCore

## 所需软件

1. [Influx DB](https://www.influxdata.com/products/influxdb-overview/) - 一种时序数据存储。

2. [Grafana](https://grafana.com/) - 用于可视化时序指标的图表与仪表盘构建工具。

{% include note.html content="虽然我们支持发送指标并连接 Influx DB v2，但我们的 Grafana 仪表盘配置并不支持。因此，要使用 Grafana 可视化数据，你确实需要运行 Influx DB v1。不过，你可以使用 [Chronograf](#additional-visualizations-and-metrics-collection) 进行可视化，但这需要你自行配置。" %}

{% include note.html content="我们不支持 Influx DB v3。" %}

### 安装 Influx DB

1. 从 https://portal.influxdata.com/downloads/ 下载并安装适用于你操作系统的 InfluxDB 1.x 版本。（目前不支持 2.x 版本。）

2. 启动 InfluxDB

3. 使用 Influx CLI 执行以下命令，在 InfluxDB 中创建用户和数据库：

```sql
CREATE DATABASE worldserver
CREATE USER grafana WITH PASSWORD 'grafana'
GRANT READ ON worldserver TO grafana
```

4. 创建用户后获得的 token 非常重要，无论对于 grafana 还是 worldserver 配置都是如此。

### 安装 Grafana

1. 从 https://grafana.com/docs/grafana/latest/installation/ 下载并安装 Grafana

2. 打开仪表盘 http://localhost:3000

3. 使用用户名 *admin* 和密码 *admin* 登录（默认值可以在 Grafana 的 .ini 文件中修改。在较新版本的 Grafana 中，首次登录时会提示你修改密码。）

4. 悬停齿轮图标并选择 Data Sources（数据源）

5. 搜索 InfluxDB 并选择。

6. 填写以下所需数据。

```
Name: Influx
Type: InfluxDB
Url: http://localhost:8086
Access: Server
Database: worldserver User: grafana Password: grafana
```

1. 点击 Save & Test（保存并测试），应会出现一个显示 "Data source is working"（数据源工作正常）的绿色勾选框。

1. 悬停 + 并选择 Import（导入），然后从 [AzerothCore 的 /apps/grafana](https://github.com/azerothcore/azerothcore-wotlk/tree/master/apps/grafana) 导入每个 .json 文件。

### 配置 AzerothCore

1. 编辑 worldserver.conf 文件

1. 设置 `Metric.Enable` = 1

1. 编辑 `Metric.ConnectionInfo` 填写连接信息（例如 "127.0.0.1;8086;worldserver"）

1. 启动 worldserver，仪表盘应开始接收数值。

## 已实现和计划中的指标

已实现（✔）和计划中（❌）的指标：

### 技术相关

* I/O 网络流量
    * 发送的数据包 ❌
    * 接收的数据包 ✔
    * 平均延迟 ❌
    * 流入流量 ❌
    * 流出流量 ❌
* 世界会话更新耗时 ✔
* 地图更新耗时 ✔
* 地图加载/卸载 ✔
* MMap 查询 ✔
* 数据库异步查询排队数量 ✔
* 服务器运行时间 ✔（通过世界初始化和世界关闭事件）
* 活跃连接数 ❌
* 排队连接数 ❌

### 游戏相关

* 在线玩家数 ✔
* 每小时/每天/每周等的登录次数 ✔
* 已发送邮件数 ❌
* 拍卖行使用量 ❌
* 角色等级 ❌
* 金币收入/支出 ❌
* LFG 队列 ❌

我们希望得到帮助来实现这些及其他指标，欢迎给我们发送[拉取请求](https://github.com/azerothcore/azerothcore-wotlk/pulls)。

## 添加新指标

可以记录的指标有两种：数值（values）和事件（events）。

数值（Values）对应于某一数量的测量值，例如在线玩家数或更新间隔（update diff）时间。

事件（Events）是在某一瞬间发生的事情，例如玩家登录、worldserver 关闭等。

要记录新指标，请调用 `METRIC_EVENT` 或 `METRIC_VALUE`，并在仪表盘上添加新图表。

`METRIC_EVENT(category, title, description)`

- **category**：任意字符串，存储数值和事件的表。按照惯例，事件日志应以 "_events" 作为后缀。

- **title**：事件日志的名称。

- **description**：关于日志事件的附加信息。

`METRIC_VALUE(category, value)`

- **category**：任意字符串，存储数值和事件的表。按照惯例，事件日志应以 "_value" 作为后缀。

- **value**：一个测量值，可以是以下类型之一：bool、std::string、float、double 或任何整数类型（int、int32、uint 等）。

**示例**

```cpp
// 记录玩家登录：在 WorldSession::HandlePlayerLogin(LoginQueryHolder* holder) 中
METRIC_EVENT("player_events", "Login", pCurrChar->GetName());
  
// 记录更新间隔时间：在 World::Update(uint32 diff) 中
METRIC_VALUE("update_time_diff", diff);
```

## 延伸阅读

深入了解 InfluxDB 和 Grafana：

* [InfluxDB 官网](https://influxdata.com/time-series-platform/influxdb/)
* [InfluxDB 文档 (v1.8)](https://docs.influxdata.com/influxdb/v1.8/)
* [Grafana 官网](http://grafana.org/)
* [Grafana 文档](http://docs.grafana.org/)
* [Grafana 在线演示](http://play.grafana.org/)
* [将 InfluxDB 添加到 Grafana](http://docs.grafana.org/datasources/influxdb/)

## InfluxDB v2

1. 下载 InfluxDB v2
2. 启动 InfluxDB
3. 访问 http://127.0.0.1:8086
4. 创建用户
```
Username: grafana
Password: grafana
Initial Organization Name: Grafana
Initial Bucket Name: worldserver
```

[例如使用 Chronograf 来可视化数据。](#additional-visualizations-and-metrics-collection)

## 附加的可视化与指标采集 {#additional-visualizations-and-metrics-collection}

InfluxDB 是 [InfluxData](https://www.influxdata.com/) 一系列相互集成良好的项目中的一员：

- [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/) 可用于采集系统指标，如 CPU、I/O、内存使用情况以及其他服务（如 MySQL），以便将这些信息显示在 AC 指标旁边。

- [Chronograf](https://www.influxdata.com/time-series-platform/chronograf/) 是 Grafana 的替代方案，用于绘制和可视化时序指标。

- [Kapacitator](https://www.influxdata.com/time-series-platform/kapacitor/) 能够处理来自 InfluxDB 的流式数据，以提供警报、触发事件、检测异常或转换数据。
