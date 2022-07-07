# Acceso remoto

## Introducción

Azerothcore tiene 4 formas de interactuar con el servidor mundial.

- En el juego
- La consola
- Telnet (RA)
- HTTP (SOAP)

Los menús del juego y la consola son bastante autoexplicativos, sin embargo no siempre se puede administrar el servidor localmente ni las dos primeras opciones ofrecen muchas oportunidades de automatización. Si quieres proporcionar una manera de acceder a tu servidor de forma remota, o dejar que el software lo administre entonces tienes dos opciones.

## Elegir el protocolo correcto

### Telnet (RA)

El acceso remoto es básicamente una conexión telnet y tiene todas las desventajas que trae una conexión telnet. Estos serían:

- Los datos se envían en texto plano, que puede ser interceptado fácilmente.
- Se utilizan sesiones distintas, lo que significa que se abre y se cierra una conexión cada vez.
- Puede ser difícil parsear el retorno ya que sólo devuelve lo que se vería en el CLI

Sin embargo, también tiene aspectos positivos, a saber:
- Es sencillo y tiene pocos gastos generales.
- Está bien establecido y documentado.
- Es independiente de la plataforma.

El acceso remoto es bueno para ejecutar en un servidor local, y acceder a él de forma segura a través de SSH para enviarle comandos. Su simplicidad es su fuerza. Además, está integrado en la mayoría de las máquinas sin necesidad de configuración.

### HTTP (SOAP)

Son las siglas de Simple Object Access Protocol y es un formato para compartir datos estructurados entre máquinas. Es un análogo común de xml a ReST y json, y permite que dos piezas de software interactúen entre sí a pesar de ejecutarse en diferentes bases de código, lenguajes y sistemas operativos. Pasemos a los puntos débiles.

- No hay codificación por defecto, lo que significa que se puede hacer casi cualquier cosa. Algunos lo ven como una ventaja, pero puede ser confuso.
- Poca seguridad

Y sus puntos fuertes.

- XML es un formato bien establecido y soportado por la mayoría de los lenguajes de programación.
- Utiliza el estándar HTTP

En un formato más simplificado: SOAP para los sitios web, telnet para la línea de comandos.

## Utilización del protocolo de elección

### Configurar

1. Ambos protocolos deben estar habilitados a través de los [archivos de configuración del servidor mundial] (https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/worldserver/worldserver.conf.dist#L2756).
2. Cuando están habilitados, para autorizar el acceso a la base de datos, es necesario encontrar la tabla `account_access` en la base de datos de autenticación y asegurarse de que el realmID de su usuario es -1 (es decir, todos los reinos).
3. Una vez hecho esto, está configurado para utilizar telnet y SOAP

### Acceda a Telnet

Debido a su ubicuidad, telnet es fácil de usar desde casi cualquier lugar.

1. abra una sesión de terminal (o PuTTY) y escriba `telnet localhost 3443`.
2. Introduzca su nombre de usuario y contraseña.

#### Acceda a Soap

Soap funciona con el estándar HTTP POST. Toda la carga útil del mensaje es XML.

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

La respuesta será así:

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
            <result>
                AzerothCore rev. 6f4f0043c2ab+ 2021-05-18 02:16:59 +0200 (master branch) (Win64, RelWithDebInfo)
                Connected players: 0. Characters in world: 0.
                Connection peak: 0.
                Server uptime: 5 second(s).
                Update time diff: 10ms, average: 10ms.
            </result>
        </ns1:executeCommandResponse>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

La respuesta al error es la siguiente

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

Tienes que autentificarte poniendo el nombre de usuario y la contraseña en el URI de la siguiente manera `http://soapuser:abcd1234@localhost:7878/` (esto también se conoce como "basic auth"). No es necesario establecer la cabecera de la solicitud `Content-Type: application/xml`. Por ahora.

## Ejemplos de códigos

<details>
<summary>PHP</summary>

Utilizando [SoapClient] incorporado(https://www.php.net/manual/en/class.soapclient.php)

```php
$connection = new SoapClient(NULL, [
    'location' => "http://{{ ip }}:{{ port }}/",
    'uri'      => 'urn:AC',
    'style'    => SOAP_RPC,
    'login'    => 'soapuser',
    'password' => 'abcd1234'
]);

echo $connection->executeCommand(new SoapParam('server info', 'command'));
```

</details>
<details>
<summary>NodeJS (TypeScript)</summary>

Utilizando [xml2js](https://www.npmjs.com/package/xml2js) para analizar la respuesta. Por favor, asegúrese de sanear las entradas.

```typescript
function AzerothCore_Soap(command) {
    return new Promise((resolve, reject) => {
        const req = http.request({
            port: 7878,
            method: "POST",
            hostname: "localhost",
            auth: "soapuser:abcd1234",
            headers: { 'Content-Type': 'application/xml' }
        }, res => {
            res.on('data', async d => {
                const xml = await xml2js.parseStringPromise(d.toString());
                const body = xml["SOAP-ENV:Envelope"]["SOAP-ENV:Body"][0];
                const fault = body["SOAP-ENV:Fault"];
                if(fault) {
                    resolve({
                        faultCode: fault[0]["faultcode"][0],
                        faultString: fault[0]["faultstring"][0],
                    });
                    return;
                }
                const response = body["ns1:executeCommandResponse"];
                if(response) {
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
