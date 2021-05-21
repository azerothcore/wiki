## Introduction

Azerothcore has 4 ways of interfacing with the world server.

- In Game
- The Console
- Telnet (RA)
- HTTP (SOAP)

The in game menus and the console are pretty self explanatory, however you are not always able to administer the server locally nor do the first two options provide many opportunities for automation. If you want to provide a way to access your server remotely, or let software manage it then you have two options.

## Choosing the Correct Protocol

### Remote Access

Remote access is basically a telnet connection and has all of the downsides a telnet connection brings. These would be:
- Data is sent over cleartext which can be intercepted easily.
- You use distinct sessions, meaning you open and close a connection each time.
- It can be difficult to parse the return since it just returns what you would see in the CLI

However, it has upsides as well, namely:
- It is simple with little overhead.
- It is well established and documented.
- Platform independent.

Remote access is good for running on a local server, and accessing it securely over SSH to send it commands. Its simplicity is its strength. On top of that it is built in to most machines without any configuration needed.

### SOAP

It stands for simple object access protocol and is a format for sharing structured data between machines. It is a common xml analogue to ReST and json, and lets two pieces of software interact with each other despite running on different code bases, languages, and operating systems. Lets get on to the weaknesses.

- No default encoding meaning that you can get away with almost anything. Some people may see it as a bonus but it can be confusing.
- Little security

And its strengths.

- XML is a well established format supported in most programming languages.
- Uses standard HTTP

In a more simplified format: SOAP for websites, telnet for command line.

## Using the Protocol of Choice

### Setup

1. Both protocols must be enabled via the [worldserver config files](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/worldserver/worldserver.conf.dist#L2756). 
2. When they are enabled, in order to authorize access to the database, you need to find the `account_access` table in the auth database and make sure the realmID of your user is -1 (meaning all realms).
3. When that is done you are set up to use telnet and SOAP

### Access
#### Telnet

Due to it's ubiquity telnet is easy to use from almost anywhere. 

1. open up a terminal session (or PuTTY) and type in `telnet localhost 3443`
2. Enter your username and password.

#### Soap

Soap works using standard HTTP POST. The entire post payload is XML.

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

The response will look like this:

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

Error response looks like this

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

You need to authenticate by putting the username and password in the URI like this: `http://soapuser:abcd1234@localhost:7878/` (this is also known as "basic auth")

setting request header `Content-Type: application/xml` is not needed. For now.

## Code Examples

<details>
    <summary>PHP</summary>
	
using built-in [SoapClient](https://www.php.net/manual/en/class.soapclient.php)

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
    <summary>NodeJS</summary>
	
using [xml2js](https://www.npmjs.com/package/xml2js) to parse the response. Please make sure to sanitize the inputs.
	
```javascript
function AzerothCore_Soap(command){
    return new Promise((resolve, reject)=>{
	var req = http.request(<http.ClientRequestArgs>{
	    port: 7878,
	    method: "POST",
	    hostname: "localhost",
	    auth: "soapuser:abcd1234",
	    headers: { 'Content-Type': 'application/xml' }
	}, res=>{
	    res.on('data', async d => {
		var xml = await xml2js.parseStringPromise(d.toString());

		var body = xml["SOAP-ENV:Envelope"]["SOAP-ENV:Body"][0];
		var fault = body["SOAP-ENV:Fault"];
		if(fault){
		    resolve({
			faultCode  : fault[0]["faultcode"][0],
			faultString: fault[0]["faultstring"][0],
		    });
		    return;
		}
		var response = body["ns1:executeCommandResponse"];
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
