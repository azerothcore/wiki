# account

[<-返回至:Auth](database-auth)

**`account` 表**

`table-no-description`

**表结构**

| Field                             | Type           | Attributes | Key | Null | Default           | Extra          | Comment       |
| --------------------------------- | -------------- | ---------- | --- | ---- | ----------------- | -------------- | ------------- |
| [id](#id)                         | INT            | UNSIGNED   | PRI | NO   |                   | AUTO_INCREMENT | 标识符        |
| [username](#username)             | VARCHAR(32)    |            | UNI | NO   | ''                |                |               |
| [salt](#salt)                     | BINARY(32)     |            |     | NO   |                   |                |               |
| [verifier](#verifier)             | BINARY(32)     |            |     | NO   |                   |                |               |
| [session_key](#sessionkey)        | BINARY(40)     |            |     | YES  |                   |                |               |
| [totp_secret](#totpsecret)        | VARBINARY(100) |            |     | YES  |                   |                |               |
| [email](#email)                   | VARCHAR(255)   |            |     | NO   | ''                |                |               |
| [reg_mail](#regmail)              | VARCHAR(255)   |            |     | NO   | ''                |                |               |
| [joindate](#joindate)             | TIMESTAMP      |            |     | NO   | CURRENT_TIMESTAMP |                |               |
| [last_ip](#lastip)                | VARCHAR(15)    |            |     | NO   | 127.0.0.1         |                |               |
| [last_attempt_ip](#lastattemptip) | VARCHAR(15)    |            |     | NO   | 127.0.0.1         |                |               |
| [failed_logins](#failedlogins)    | INT            | UNSIGNED   |     | NO   | 0                 |                |               |
| [locked](#locked)                 | TINYINT        | UNSIGNED   |     | NO   | 0                 |                |               |
| [lock_country](#lockcountry)      | VARCHAR(2)     |            |     | NO   | 00                |                |               |
| [last_login](#lastlogin)          | TIMESTAMP      |            |     | YES  |                   |                |               |
| [online](#online)                 | INT            | UNSIGNED   |     | NO   | 0                 |                |               |
| [expansion](#expansion)           | TINYINT        | UNSIGNED   |     | NO   | 2                 |                |               |
| [Flags](#flags)                   | INT            | UNSIGNED   |     | NO   | 0                 |                | 账号标志     |
| [mutetime](#mutetime)             | BIGINT         |            |     | NO   | 0                 |                |               |
| [mutereason](#mutereason)         | VARCHAR(255)   |            |     | NO   | ''                |                |               |
| [muteby](#muteby)                 | VARCHAR(50)    |            |     | NO   | ''                |                |               |
| [locale](#locale)                 | TINYINT        | UNSIGNED   |     | NO   | 0                 |                |               |
| [os](#os)                         | VARCHAR(3)     |            |     | NO   | ''                |                |               |
| [recruiter](#recruiter)           | INT            | UNSIGNED   |     | NO   | 0                 |                |               |
| [totaltime](#totaltime)           | INT            | UNSIGNED   |     | NO   | 0                 |                |               |

## 字段说明

### id

唯一的账号 ID。

### username

用户的账号名。

**注意：** 用户名长度限制为 20 个字符，且没有字符限制。

### salt

salt 是一个密码学上随机的 32 字节值。

### verifier

verifier 由 salt 以及用户的用户名（全大写）和密码（全大写）派生而来。

要得到 verifier，你需要计算：

1. 计算 `h1 = SHA1("USERNAME:PASSWORD")`，其中代入的是转换为大写后的用户名和密码。

2. 计算 `h2 = SHA1(salt || h1)`，其中 || 表示拼接（即 PHP 中的 . 运算符）。

**注意：** `salt` 和 `h1` 都是二进制，而不是十六进制字符串！

3. 将 `h2` 视为小端序的整数（第一个字节为最低有效位）。

4. 计算 `(g ^ h2) % N`。

**注意：** `g` 和 `N` 是在 WoW 实现中固定的参数。

`g = 7`

`N = 0x894B645E89E1535BBDAD5B8B290650530801B18EBFBF5E8FAB3C82872A3E9BB7`

5. 将结果转换回小端序的字节数组。

#### 针对 PHP 实现

请确保 PHP GMP 扩展已加载！取消 php.ini 中 `extension=gmp` 的注释。

[CalculateSRP6Verifier.php](https://gist.github.com/Treeston/db44f23503ae9f1542de31cb8d66781e)

[GetSRP6RegistrationData.php](https://gist.github.com/Treeston/40b99dd71f55d55c68857919088b2e41)

[VerifySRP6Login.php](https://gist.github.com/Treeston/34d9249fb467dddc11b2568e74f8cb1e)

### session\_key

用于加密当前已认证会话的会话密钥。登录时填充，退出时清除。

### totp\_secret

验证器（authenticator）密钥。

该密钥可以通过 Google Authenticator API、第三方 TOTP 生成器生成，或手动指定（必须是符合 Base32 规范的 16 个字符的表达式）。

关于 Google Authenticator API 的维基百科实现链接。

<http://en.wikipedia.org/wiki/Google_Authenticator#Implementations>

### email

与此账号关联的电子邮件地址。

### reg\_mail

与此账号关联的注册电子邮件地址。

### joindate

账号创建时的日期。

### last\_ip

登录该账号的人最后使用的 IP。

### failed\_logins

在该账号上尝试的失败登录次数。

### locked

布尔值 0 或 1，控制账号是否已被锁定。可以通过 ".account lock" GM 命令控制。如果已锁定（1），用户只能使用其 [last_ip][11] 登录。如果未锁定（0），用户可以从任何 IP 登录，如果 IP 不同，其 last_ip 将被更新。".Ban account" 不会锁定账号。

### last\_login

账号最后登录的日期。

### totaltime

玩家在其所有角色上花费的总游戏时间。包括那些已不在数据库中的已删除角色。
以 Unix 时间存储。

### online

布尔值 0 或 1，控制账号当前是否已登录并在线。

### expansion

整数 0、1 或 2，控制登录该账号的客户端是否拥有资料片。（例如，如果客户端是 TBC，但 expansion 设置为 0，则它将无法进入外域等。）

| 值    | 资料片                        |
| ----- | ------------------------------ |
| 0     | 经典旧世                        |
| 1     | 燃烧的远征 (TBC)                |
| 2     | 巫妖王之怒 (WotLK)              |

### Flags

| 名称                              | 描述                           | 位值      |
| --------------------------------- | ------------------------------ | --------- |
| ACCOUNT_FLAG_GM                   | 账号是 GM                      | 1         |
| ACCOUNT_FLAG_NOKICK               | AFK 时不会被强制下线            | 2         |
| ACCOUNT_FLAG_COLLECTOR            | 典藏版（创建角色时赠送新手礼品券） | 4         |
| ACCOUNT_FLAG_TRIAL                | 试玩账号                       | 8         |
| ACCOUNT_FLAG_CANCELLED            | 未知                           | 16        |
| ACCOUNT_FLAG_IGR                  | Internet Game Room（网吧？）    | 32        |
| ACCOUNT_FLAG_WHOLESALER           | 未知                           | 64        |
| ACCOUNT_FLAG_PRIVILEGED           | 未知                           | 128       |
| ACCOUNT_FLAG_EU_FORBID_ELV        | 未知                           | 256       |
| ACCOUNT_FLAG_EU_FORBID_BILLING    | 未知                           | 512       |
| ACCOUNT_FLAG_RESTRICTED           | 未知                           | 1024      |
| ACCOUNT_FLAG_REFERRAL             | 招募好友（推荐人或被推荐人）    | 2048      |
| ACCOUNT_FLAG_BLIZZARD             | 未知                           | 4096      |
| ACCOUNT_FLAG_RECURRING_BILLING    | 未知                           | 8192      |
| ACCOUNT_FLAG_NOELECTUP            | 未知                           | 16384     |
| ACCOUNT_FLAG_KR_CERTIFICATE       | 韩国证书？                     | 32768     |
| ACCOUNT_FLAG_EXPANSION_COLLECTOR  | TBC 典藏版                     | 65536     |
| ACCOUNT_FLAG_DISABLE_VOICE        | 无法加入语音聊天               | 131072    |
| ACCOUNT_FLAG_DISABLE_VOICE_SPEAK  | 无法在语音聊天中发言           | 262144    |
| ACCOUNT_FLAG_REFERRAL_RESURRECT   | 复活卷轴                       | 524288    |
| ACCOUNT_FLAG_EU_FORBID_CC         | 未知                           | 1048576   |
| ACCOUNT_FLAG_OPENBETA_DELL        | Dell XPS WoW 版促销            | 2097152   |
| ACCOUNT_FLAG_PROPASS              | 未知                           | 4194304   |
| ACCOUNT_FLAG_PROPASS_LOCK         | Pro Pass（竞技场锦标赛）       | 8388608   |
| ACCOUNT_FLAG_PENDING_UPGRADE      | 未知                           | 16777216  |
| ACCOUNT_FLAG_RETAIL_FROM_TRIAL    | 未知                           | 33554432  |
| ACCOUNT_FLAG_EXPANSION2_COLLECTOR | WotLK 典藏版                   | 67108864  |
| ACCOUNT_FLAG_OVERMIND_LINKED      | 与 Battle.net 账号关联         | 134217728 |
| ACCOUNT_FLAG_DEMOS                | 未知                           | 268435456 |
| ACCOUNT_FLAG_DEATH_KNIGHT_OK      | 允许创建死亡骑士。当账号首次满足 `CharacterCreating.MinLevelForHeroicCharacter` 要求时自动设置；一旦设置，将覆盖该要求。 | 536870912 |
| ACCOUNT_FLAG_S2_REQUIRE_IGR       | 未知（与星际争霸 II 相关？）    | 1073741824 |
| ACCOUNT_FLAG_S2_TRIAL             | 未知（与星际争霸 II 相关？）    | 2147483648 |

### mutetime

账号解除禁言的时间，以 Unix 时间表示。要查看禁言何时到期，可以使用以下查询：

```sql
SELECT FROM_UNIXTIME(`mutetime`);
```

### mutereason

禁言的原因。

### muteby

执行 .mute 命令并施加禁言、拥有相应权限的角色名。

### locale

登录该账号的客户端所使用的语言区域。如果已配置并向世界服务器添加了多种语言区域数据，世界服务器将向客户端返回相应的语言区域字符串。

| ID  | 语言    |
| --- | ------- |
| 0   | enUS    |
| 1   | koKR    |
| 2   | frFR    |
| 3   | deDE    |
| 4   | zhCN    |
| 5   | zhTW    |
| 6   | esES    |
| 7   | esMX    |
| 8   | ruRU    |

### os

存储有关客户端操作系统的信息。由 Warden 系统使用。

- Win
- Mac

### recruiter

另一个账号的账号 ID。用于招募好友系统。参见 [account.id][1]
