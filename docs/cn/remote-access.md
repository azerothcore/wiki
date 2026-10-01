---
redirect_from: "/cn/Remote-Access"
---

# 远程访问

## 简介

AzerothCore 有 4 种与世界服务器（world server）交互的方式。

- 游戏内
- 控制台
- Telnet (RA)
- HTTP (SOAP)

游戏内菜单和控制台不言自明，但你并不总能本地管理服务器，而且前两种方式也没有提供太多自动化机会。如果你想提供远程访问服务器的方式，或让软件来管理它，那么你有两个选择。

## 选择正确的协议

### 远程访问（Remote Access）

远程访问基本上就是一个 telnet 连接，并且具有 telnet 连接带来的一切缺点。这些缺点包括：
- 数据以明文发送，很容易被截获。
- 使用独立的会话，意味着每次都要打开和关闭一个连接。
- 返回结果可能难以解析，因为它返回的只是你在 CLI 中看到的内容。

然而，它也有优点，即：
- 简单且开销小。
- 成熟且有完善的文档。
- 跨平台。

远程访问非常适合在本地服务器上运行，并通过 SSH 安全地访问它来发送命令。简单就是它的优势。此外，它内置在大多数机器中，无需任何配置。

### SOAP

SOAP 是简单对象访问协议（Simple Object Access Protocol）的缩写，是一种在机器之间共享结构化数据的格式。它是 ReST 和 json 常见的 XML 对应物，可以让两段软件尽管运行在不同的代码库、语言和操作系统上，仍能相互交互。接下来看看它的缺点。

- 没有默认编码，这意味着几乎可以随意使用任何内容。有些人可能认为这是优点，但它也可能令人困惑。
- 安全性较弱

以及它的优点。

- XML 是一种成熟且被大多数编程语言支持的格式。
- 使用标准 HTTP

用更简化的说法：网站用 SOAP，命令行用 telnet。

## 使用所选协议

### 设置

1. 两种协议都必须通过 [worldserver 配置文件](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/apps/worldserver/worldserver.conf.dist#L3122) 启用。
2. 启用后，为了授权访问数据库，你需要在 auth 数据库中找到 `account_access` 表，并确保你的用户的 realmID 为 -1（表示所有服务器）。
3. 完成上述操作后，你就可以使用 telnet 和 SOAP 了。

### 访问
#### Telnet

由于 telnet 无处不在，几乎在任何地方都很容易使用。

1. 打开一个终端会话（或 PuTTY），输入 `telnet localhost 3443`
2. 输入你的用户名和密码。

#### Soap

SOAP 使用标准的 HTTP POST 工作。整个 POST 负载都是 XML。

```xml
<SOAP-ENV:Envelope  
    xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" 
    xmlns:xsi="http://www.w3.org/1999/XMLSchema-instance" 
    xmlns:xsd="http://www.w3.org/1999/XMLSchema" 
    xmlns:ns1="urn:AC">
    <SOAP-ENV:Body>
	<ns1:executeCommand>
	    <command>server status</command>
	</ns1:executeCommand>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

响应看起来像这样：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
  xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
  xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
  xmlns:xsi="http://www.w3.org/1999/XMLSchema-instance"
  xmlns:xsd="http://www.w3.org/1999/XMLSchema"
  xmlns:ns1="urn:AC">
  <SOAP-ENV:Body>
    <ns1:executeCommandResponse>
      <result>AzerothCore rev. 6f4f0043c2ab+ 2021-05-18 02:16:59 +0200 (master branch) (Win64, RelWithDebInfo)&#xD;
Connected players: 0. Characters in world: 0.&#xD;
Connection peak: 0.&#xD;
Server uptime: 5 second(s).&#xD;
Update time diff: 10ms, average: 10ms.&#xD;
</result>
    </ns1:executeCommandResponse>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

错误响应看起来像这样

```xml
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope
  xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
  xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"
  xmlns:xsi="http://www.w3.org/1999/XMLSchema-instance"
  xmlns:xsd="http://www.w3.org/1999/XMLSchema"
  xmlns:ns1="urn:AC">
  <SOAP-ENV:Body>
    <SOAP-ENV:Fault>
      <faultcode>SOAP-ENV:Client</faultcode>
      <faultstring>Error 401: HTTP 401 Unauthorized</faultstring>
    </SOAP-ENV:Fault>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

你需要通过将用户名和密码放入 URI 来进行身份验证，如下所示：`http://soapuser:abcd1234@localhost:7878/`（这也称为"basic auth"）

目前，设置请求头 `Content-Type: application/xml` 并不是必需的。

## 代码示例

<details>
    <summary>PHP</summary>
	
使用内置的 [SoapClient](https://www.php.net/manual/en/class.soapclient.php)

```php
$conn = new SoapClient(NULL, array(
'location' => "http://{{ ip }}:{{ port }}/",
'uri'      => 'urn:AC',
'style'    => SOAP_RPC,
'login'    => 'soapuser',
'password' => 'abcd1234'
));
echo $conn->executeCommand(new SoapParam('server info', 'command'));
```
	
</details>
<details>
    <summary>NodeJS (TypeScript)</summary>
	
使用 [xml2js](https://www.npmjs.com/package/xml2js) 解析响应。请务必对输入进行消毒处理。
	
```typescript
function AzerothCore_Soap(command){
    return new Promise((resolve, reject)=>{
	const req = http.request({
	    port: 7878,
	    method: "POST",
	    hostname: "localhost",
	    auth: "soapuser:abcd1234",
	    headers: { 'Content-Type': 'application/xml' }
	}, res=>{
	    res.on('data', async d => {
		const xml = await xml2js.parseStringPromise(d.toString());

		const body = xml["SOAP-ENV:Envelope"]["SOAP-ENV:Body"][0];
		const fault = body["SOAP-ENV:Fault"];
		if(fault){
		    resolve({
			faultCode  : fault[0]["faultcode"][0],
			faultString: fault[0]["faultstring"][0],
		    });
		    return;
		}
		const response = body["ns1:executeCommandResponse"];
		if(response){
		    resolve({
			result: response[0]["result"][0]
		    });
		    return;
		}
		console.log(d.toString());
	    })
	});
	req.write(
	    '<SOAP-ENV:Envelope' +
	    ' xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"' +
	    ' xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/"' +
	    ' xmlns:xsi="http://www.w3.org/1999/XMLSchema-instance"' +
	    ' xmlns:xsd="http://www.w3.org/1999/XMLSchema"' +
	    ' xmlns:ns1="urn:AC">' +
	    '<SOAP-ENV:Body>' +
	    '<ns1:executeCommand>' +
		'<command>'+command+'</command>' +
	    '</ns1:executeCommand>' +
	    '</SOAP-ENV:Body>' +
	    '</SOAP-ENV:Envelope>'
	);
	req.end();
    });
}
```
	
</details>
