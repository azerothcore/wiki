# Cómo usar el Warden Payload Manager

El WardenPayloadMgr es responsable de mantener los payloads personalizados usados por los módulos.
Esto permite a los usuarios enviar payloads lua personalizados de hasta un tamaño de 512 bytes al cliente del juego.

Algunas de las cosas que puedes lograr con esto son:
- Interacción con la interfaz del cliente (añadir frames personalizados)
- Acceso a las CVars del cliente
- Acceso a funciones lua protegidas.

Abriendo muchas posibilidades para un servidor personalizado sin parches.

## Acceder al Payload Manager

Para acceder al payload manager tienes que tener acceso a una referencia de Player.

**Ejemplo (C++):**
```cpp
void OnLogin(Player* player) override
{
	if (!player)
	{
		return;
	}
	
	Warden* warden = player->GetSession()->GetWarden();
	if (!warden)
	{
		return;
	}
	
	WardenPayloadMgr* payloadMgr = warden->GetPayloadMgr();
	if (!payloadMgr)
	{
		return;
	}

	std::string sPayload = "message('Hello World!');";
	uint16 payloadId = payloadMgr->RegisterPayload(sPayload);
	payloadMgr->QueuePayload(payloadId);
}
```
Normalmente almacenarías el payloadId en algún sitio y no generarías uno nuevo en cada login.

## Escribir un Payload Addon Listener
Hay una cantidad limitada de payload ids disponibles, así que se aconseja crear un payload listener que se envíe al cliente en el login.

**Ejemplo (Lua):**
```lua
local luaFrame = CreateFrame('Frame');
luaFrame:RegisterEvent('CHAT_MSG_ADDON');
luaFrame:SetScript('OnEvent', function(self, event, ...)
  local prefix, lua, msgType, unit = ...;
  if event == 'CHAT_MSG_ADDON' and prefix == 'wlrx' and msgType == 'WHISPER' and unit == UnitName('player') then
    forceinsecure();
    loadstring(lua)();
  end
end);
```
Para enviar ahora un payload al cliente necesitarías enviar un mensaje de addon al jugador con el prefijo `wlrx`, el tipo de mensaje `WHISPER` y el emisor/receptor siendo el GUID del jugador.

**Ejemplo (C++):**
```cpp
WorldPacket CreateAddonPacket(std::string const& prefix, std::string const& msg, ChatMsg msgType, Player* player)
{
    WorldPacket data;

    std::string fullMsg = prefix + "\t" + msg;
    size_t len = fullMsg.length();

    data.Initialize(SMSG_MESSAGECHAT, 1 + 4 + 8 + 4 + 8 + 4 + 1 + len + 1);
    data << uint8(msgType); //Type
    data << uint32(LANG_ADDON); //Lang
    data << uint64(player->GetGUID().GetRawValue()); //SenderGUID
    data << uint32(0); //Flags
    data << uint64(player->GetGUID().GetRawValue()); //ReceiverGUID
    data << uint32(len + 1); //MsgLen
    data << fullMsg; //Msg
    data << uint8(0);

    return data;
}

std::string myPayload = "message('Hello World!');";
WorldPacket payloadPacket = CreateAddonPacket("wlrx", myPayload, CHAT_MSG_WHISPER, player);
player->SendDirectMessage(&payloadPacket);
```
El mensaje de addon tiene un límite de unos 255 caracteres, así que puede que tengas que trocear tu mensaje en varios paquetes.

Puedes hacer esto escribiendo partes de tu payload en un buffer del cliente y luego, en el último payload, llamar a loadstring sobre ese buffer.

Si necesitas comunicarte de vuelta con el servidor puedes usar [SendAddonMessage](https://wowwiki-archive.fandom.com/wiki/API_SendAddonMessage) y capturar el resultado usando uno de los message hooks:

**Ejemplo (Lua):**
```lua
SendAddonMessage("wltx", "ping", "WHISPER", UnitName('player'));
```

**Ejemplo (C++):**
```cpp
std::vector<std::string> Split(const std::string& s, char delimiter)
{
    std::vector<std::string> tokens;
    std::string token;
    std::istringstream tokenStream(s);
    while (std::getline(tokenStream, token, delimiter))
    {
        tokens.push_back(token);
    }
    return tokens;
}

void PlayerScript::OnBeforeSendChatMessage(Player* player, uint32& type, uint32& lang, std::string& msg)
{
    if (!player)
    {
        return;
    }

    if (type != CHAT_MSG_WHISPER)
    {
        return;
    }

    if (lang != LANG_ADDON)
    {
        return;
    }

    auto data = Split(msg, '\t');

    auto prefix = data[0];
    auto event = data[1];

    if (prefix != "wltx")
    {
        return;
    }

    LOG_INFO("module", "Received addon event: '{}'", event);
    
    std::string myPayload = "print('Pong!');";
    WorldPacket payloadPacket = CreateAddonPacket("wlrx", myPayload, CHAT_MSG_WHISPER, player);
    player->SendDirectMessage(&payloadPacket);
}

//Output: Received addon event: 'ping'.
```

Ahora tienes las herramientas básicas para crear un listener y enviar payloads al cliente.
