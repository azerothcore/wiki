# 如何使用 Warden 负载管理器

WardenPayloadMgr 负责维护模块使用的自定义负载（payload）。
这允许用户向游戏客户端发送最大 512 字节的自定义 lua 负载。

你可以用它实现的一些事情有：
- 与客户端界面交互（添加自定义框架）
- 访问客户端 CVars
- 访问受保护的 lua 函数。

为无补丁（patch-less）的自定义服务器开启了许多可能性。

## 访问负载管理器

要访问负载管理器，你必须能够获得一个 Player 引用。

**示例（C++）：**
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
通常你会将 payloadId 存储在某处，而不是每次登录都生成一个新的。

## 编写负载插件监听器
可用的负载 ID 数量有限，因此建议创建一个负载监听器，在登录时发送给客户端。

**示例（Lua）：**
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
现在要向客户端发送负载，你需要向玩家发送一条前缀为 `wlrx`、消息类型为 `WHISPER`、发送者/接收者为玩家 GUID 的插件消息。

**示例（C++）：**
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
插件消息大约有 255 个字符的限制，所以你可能需要将消息分块成多个数据包。

你可以通过在客户端将负载的一部分写入缓冲区，然后在最后一个负载调用时对该缓冲区执行 loadstring 来实现这一点。

如果你需要与服务器通信，可以使用 [SendAddonMessage](https://wowwiki-archive.fandom.com/wiki/API_SendAddonMessage)，并使用其中一个消息钩子捕获结果：

**示例（Lua）：**
```lua
SendAddonMessage("wltx", "ping", "WHISPER", UnitName('player'));
```

**示例（C++）：**
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

你现在已经拥有了创建监听器并向客户端发送负载的基本工具。
