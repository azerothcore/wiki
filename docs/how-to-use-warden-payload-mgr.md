# How to use the Warden Payload Manager

The WardenPayloadMgr is responsible for maintaining custom payloads used by modules.
This allows users to send custom lua payloads up to a size of 512 bytes to the game client.

Some of the things you can achieve with this is:
- Interaction with the client interface (add custom frames)
- Access to client CVars
- Access to protected lua functions.

Opening up many possiblilties for a patch-less custom server.

## Accessing the Payload Manager

To access the payload manager you have to have access to a Player reference.

**Example(C++):**
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
Typically you would store the payloadId somewhere and not generate a new one every login.

## Writing a Payload Addon Listener
There is a limited amount of payload ids available so it is advised to create a payload listener that is sent to the client on login.

**Example(Lua):**
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
To send a payload now to the client you would need to send an addon message to the player with the prefix `wlrx`, message type `WHISPER` and the sender/receiver as the players GUID.

**Example(C++):**
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
The addon message has a limit to about 255 characters so you may have to chunk your message up into multiple packets.

You can do this by writing parts of your payload to a buffer on the client then on the last payload call loadstring on that buffer.

If you need to communicate back to the server you can use [SendAddonMessage](https://wowwiki-archive.fandom.com/wiki/API_SendAddonMessage) and capture the result using one of the message hooks:

**Example(Lua):**
```lua
SendAddonMessage("wltx", "ping", "WHISPER", UnitName('player'));
```

**Example(C++):**
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

You now have the basic tools to create a listener and send payloads to the client.