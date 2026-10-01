---
redirect_from: "/cn/Emotes"
---

# 表情（Emotes）

[`返回:DBC`](dbc-index)

该 DBC 文件包含 NPC 可以使用的表情。

[如何将 DBC 数据导入数据库](how-to-import-dbc-data-in-db)

## 结构

| 列  | 类型  | 注释                                                                                                                        |
| --- | ----- | --------------------------------------------------------------------------------------------------------------------------- |
| 1   | long  | 表情的 ID。必须唯一。                                                                                                       |
| 2   | str   | 表情的描述性名称。                                                                                                          |
| 3   | long  | 引用 [此 DBC 文件](http://collab.kpsn.org/display/tc/AnimationData) 中的 ID。这是要播放的动画的 ID。                        |
| 4   | flags |                                                                                                                             |
| 5   | flags |                                                                                                                             |
| 6   | long  |                                                                                                                             |
| 7   | long  | 引用 [此 DBC 文件](http://collab.kpsn.org/display/tc/SoundEntries) 中的 ID。这是播放动画时要播放的音效的 ID。               |

该 DBC 文件的结构信息取自[此处](https://web.archive.org/web/20161130074340/http://www.pxr.dk/wowdev/wiki/index.php?title=Emotes.dbc)和[此处](https://wowdev.wiki/DB/Emotes)。如需了解没有注释的列的相关信息，请参阅[该页面](https://web.archive.org/web/20161130074340/http://www.pxr.dk/wowdev/wiki/index.php?title=Emotes.dbc)或[此处](https://wowdev.wiki/DB/Emotes)。

## 内容

当使用 *.npc playemote \#* 命令测试下列 NPC 表情时，NPC 通常会持续播放指定的表情。而通过例如 SAI 脚本播放表情时，NPC 使用表情的方式可能会有所不同。

| ID  | 表情名称                          | 注释                                                   |
| --- | --------------------------------- | ------------------------------------------------------ |
| 0   | ONESHOT_NONE                        | NPC 恢复到其正常的站立状态。                            |
| 1   | ONESHOT_TALK(DNR)                   | NPC 播放一次说话表情。                                  |
| 2   | ONESHOT_BOW                         | NPC 播放一次鞠躬表情。                                  |
| 3   | ONESHOT_WAVE(DNR)                   | NPC 播放一次挥手表情。                                  |
| 4   | ONESHOT_CHEER(DNR)                  | NPC 播放一次欢呼表情。                                  |
| 5   | ONESHOT_EXCLAMATION(DNR)            | NPC 播放一次惊叹表情。                                  |
| 6   | ONESHOT_QUESTION                    | NPC 播放一次疑问表情。                                  |
| 7   | ONESHOT_EAT                         | NPC 播放一次进食表情。                                  |
| 10  | STATE_DANCE                         | NPC 持续播放跳舞表情。                                  |
| 11  | ONESHOT_LAUGH                       | NPC 播放一次大笑表情。                                  |
| 12  | STATE_SLEEP                         |                                                        |
| 13  | STATE_SIT                           |                                                        |
| 14  | ONESHOT_RUDE(DNR)                   |                                                        |
| 15  | ONESHOT_ROAR(DNR)                   |                                                        |
| 16  | ONESHOT_KNEEL                       |                                                        |
| 17  | ONESHOT_KISS                        |                                                        |
| 18  | ONESHOT_CRY                         |                                                        |
| 19  | ONESHOT_CHICKEN                     |                                                        |
| 20  | ONESHOT_BEG                         |                                                        |
| 21  | ONESHOT_APPLAUD                     |                                                        |
| 22  | ONESHOT_SHOUT(DNR)                  |                                                        |
| 23  | ONESHOT_FLEX                        |                                                        |
| 24  | ONESHOT_SHY(DNR)                    |                                                        |
| 25  | ONESHOT_POINT(DNR)                  |                                                        |
| 26  | STATE_STAND                         |                                                        |
| 27  | STATE_READYUNARMED                  |                                                        |
| 28  | STATE_WORK_SHEATHED                 |                                                        |
| 29  | STATE_POINT(DNR)                    |                                                        |
| 30  | STATE_NONE                          |                                                        |
| 33  | ONESHOT_WOUND                       |                                                        |
| 34  | ONESHOT_WOUNDCRITICAL               |                                                        |
| 35  | ONESHOT_ATTACKUNARMED               |                                                        |
| 36  | ONESHOT_ATTACK1H                    |                                                        |
| 37  | ONESHOT_ATTACK2HTIGHT               |                                                        |
| 38  | ONESHOT_ATTACK2H_LOOSE              |                                                        |
| 39  | ONESHOT_PARRYUNARMED                |                                                        |
| 43  | ONESHOT_PARRYSHIELD                 |                                                        |
| 44  | ONESHOT_READYUNARMED                |                                                        |
| 45  | ONESHOT_READY1H                     |                                                        |
| 48  | ONESHOT_READYBOW                    |                                                        |
| 50  | ONESHOT_SPELLPRECAST                |                                                        |
| 51  | ONESHOT_SPELLCAST                   |                                                        |
| 53  | ONESHOT_BATTLEROAR                  |                                                        |
| 54  | ONESHOT_SPECIALATTACK1H             |                                                        |
| 60  | ONESHOT_KICK                        |                                                        |
| 61  | ONESHOT_ATTACKTHROWN                |                                                        |
| 64  | STATE_STUN                          |                                                        |
| 65  | STATE_DEAD                          |                                                        |
| 66  | ONESHOT_SALUTE                      |                                                        |
| 68  | STATE_KNEEL                         |                                                        |
| 69  | STATE_USESTANDING                   |                                                        |
| 70  | ONESHOT_WAVE_NOSHEATHE              |                                                        |
| 71  | ONESHOT_CHEER_NOSHEATHE             |                                                        |
| 92  | ONESHOT_EAT_NOSHEATHE               |                                                        |
| 93  | STATE_STUN_NOSHEATHE                |                                                        |
| 94  | ONESHOT_DANCE                       |                                                        |
| 104 | ONESHOT_WHISTLE                     |                                                        |
| 113 | ONESHOT_SALUTE_NOSHEATH             |                                                        |
| 133 | STATE_USESTANDING_NOSHEATHE         |                                                        |
| 153 | ONESHOT_LAUGH_NOSHEATHE             |                                                        |
| 173 | STATE_WORK                          |                                                        |
| 193 | STATE_SPELLPRECAST                  |                                                        |
| 213 | ONESHOT_READYRIFLE                  |                                                        |
| 214 | STATE_READYRIFLE                    |                                                        |
| 233 | STATE_WORK_MINING                   |                                                        |
| 234 | STATE_WORK_CHOPWOOD                 |                                                        |
| 253 | STATE_APPLAUD                       |                                                        |
| 254 | ONESHOT_LIFTOFF                     |                                                        |
| 273 | ONESHOT_YES(DNR)                    |                                                        |
| 274 | ONESHOT_NO(DNR)                     |                                                        |
| 275 | ONESHOT_TRAIN(DNR)                  |                                                        |
| 293 | ONESHOT_LAND                        |                                                        |
| 313 | STATE_AT_EASE                       |                                                        |
| 333 | STATE_READY1H                       |                                                        |
| 353 | STATE_SPELLKNEELSTART               |                                                        |
| 373 | STAND_STATE_SUBMERGED               |                                                        |
| 374 | ONESHOT_SUBMERGE                    |                                                        |
| 375 | STATE_READY2H                       |                                                        |
| 376 | STATE_READYBOW                      |                                                        |
| 377 | ONESHOT_MOUNTSPECIAL                |                                                        |
| 378 | STATE_TALK                          |                                                        |
| 379 | STATE_FISHING                       |                                                        |
| 380 | ONESHOT_FISHING                     |                                                        |
| 381 | ONESHOT_LOOT                        |                                                        |
| 382 | STATE_WHIRLWIND                     |                                                        |
| 383 | STATE_DROWNED                       |                                                        |
| 384 | STATE_HOLD_BOW                      |                                                        |
| 385 | STATE_HOLD_RIFLE                    |                                                        |
| 386 | STATE_HOLD_THROWN                   |                                                        |
| 387 | ONESHOT_DROWN                       |                                                        |
| 388 | ONESHOT_STOMP                       |                                                        |
| 389 | ONESHOT_ATTACKOFF                   |                                                        |
| 390 | ONESHOT_ATTACKOFFPIERCE             |                                                        |
| 391 | STATE_ROAR                          |                                                        |
| 392 | STATE_LAUGH                         |                                                        |
| 393 | ONESHOT_CREATURE_SPECIAL            |                                                        |
| 394 | ONESHOT_JUMPLANDRUN                 |                                                        |
| 395 | ONESHOT_JUMPEND                     |                                                        |
| 396 | ONESHOT_TALK_NOSHEATHE              |                                                        |
| 397 | ONESHOT_POINT_NOSHEATHE             |                                                        |
| 398 | STATE_CANNIBALIZE                   |                                                        |
| 399 | ONESHOT_JUMPSTART                   |                                                        |
| 400 | STATE_DANCESPECIAL                  |                                                        |
| 401 | ONESHOT_DANCESPECIAL                |                                                        |
| 402 | ONESHOT_CUSTOMSPELL01               |                                                        |
| 403 | ONESHOT_CUSTOMSPELL02               |                                                        |
| 404 | ONESHOT_CUSTOMSPELL03               |                                                        |
| 405 | ONESHOT_CUSTOMSPELL04               |                                                        |
| 406 | ONESHOT_CUSTOMSPELL05               |                                                        |
| 407 | ONESHOT_CUSTOMSPELL06               |                                                        |
| 408 | ONESHOT_CUSTOMSPELL07               |                                                        |
| 409 | ONESHOT_CUSTOMSPELL08               |                                                        |
| 410 | ONESHOT_CUSTOMSPELL09               |                                                        |
| 411 | ONESHOT_CUSTOMSPELL10               |                                                        |
| 412 | STATE_EXCLAIM                       |                                                        |
| 413 | STATE_DANCE_CUSTOM                  |                                                        |
| 415 | STATE_SIT_CHAIR_MED                 |                                                        |
| 416 | STATE_CUSTOM_SPELL_01               |                                                        |
| 417 | STATE_CUSTOM_SPELL_02               |                                                        |
| 418 | STATE_EAT                           |                                                        |
| 419 | STATE_CUSTOM_SPELL_04               |                                                        |
| 420 | STATE_CUSTOM_SPELL_03               |                                                        |
| 421 | STATE_CUSTOM_SPELL_05               |                                                        |
| 422 | STATE_SPELLEFFECT_HOLD              |                                                        |
| 423 | STATE_EAT_NO_SHEATHE                |                                                        |
| 424 | STATE_MOUNT                         |                                                        |
| 425 | STATE_READY2HL                      |                                                        |
| 426 | STATE_SIT_CHAIR_HIGH                |                                                        |
| 427 | STATE_FALL                          |                                                        |
| 428 | STATE_LOOT                          |                                                        |
| 429 | STATE_SUBMERGED                     |                                                        |
| 430 | ONESHOT_COWER(DNR)                  |                                                        |
| 431 | STATE_COWER                         |                                                        |
| 432 | ONESHOT_USESTANDING                 |                                                        |
| 433 | STATE_STEALTH_STAND                 |                                                        |
| 434 | ONESHOT_OMNICAST_GHOUL (W/SOUND     |                                                        |
| 435 | ONESHOT_ATTACKBOW                   |                                                        |
| 436 | ONESHOT_ATTACKRIFLE                 |                                                        |
| 437 | STATE_SWIM_IDLE                     |                                                        |
| 438 | STATE_ATTACK_UNARMED                |                                                        |
| 439 | ONESHOT_SPELLCAST (W/SOUND)         |                                                        |
| 440 | ONESHOT_DODGE                       |                                                        |
| 441 | ONESHOT_PARRY1H                     |                                                        |
| 442 | ONESHOT_PARRY2H                     |                                                        |
| 443 | ONESHOT_PARRY2HL                    |                                                        |
| 444 | STATE_FLYFALL                       |                                                        |
| 445 | ONESHOT_FLYDEATH                    |                                                        |
| 446 | STATE_FLY_FALL                      |                                                        |
| 447 | ONESHOT_FLY_SIT_GROUND_DOWN         |                                                        |
| 448 | ONESHOT_FLY_SIT_GROUND_UP           |                                                        |
| 449 | ONESHOT_EMERGE                      |                                                        |
| 450 | ONESHOT_DRAGONSPIT                  |                                                        |
| 451 | STATE_SPECIALUNARMED                |                                                        |
| 452 | ONESHOT_FLYGRAB                     |                                                        |
| 453 | STATE_FLYGRABCLOSED                 |                                                        |
| 454 | ONESHOT_FLYGRABTHROWN               |                                                        |
| 455 | STATE_FLY_SIT_GROUND                |                                                        |
| 456 | STATE_WALKBACKWARDS                 |                                                        |
| 457 | ONESHOT_FLYTALK                     |                                                        |
| 458 | ONESHOT_FLYATTACK1H                 |                                                        |
| 459 | STATE_CUSTOMSPELL08                 |                                                        |
| 460 | ONESHOT_FLY_DRAGONSPIT              |                                                        |
| 461 | STATE_SIT_CHAIR_LOW                 |                                                        |
| 462 | ONE_SHOT_STUN                       |                                                        |
| 463 | ONESHOT_SPELLCAST_OMNI              |                                                        |
| 465 | STATE_READYTHROWN                   |                                                        |
| 466 | ONESHOT_WORK_CHOPWOOD               |                                                        |
| 467 | ONESHOT_WORK_MINING                 |                                                        |
| 468 | STATE_SPELL_CHANNEL_OMNI            |                                                        |
| 469 | STATE_SPELL_CHANNEL_DIRECTED        |                                                        |
| 470 | STAND_STATE_NONE                    |                                                        |
| 471 | STATE_READYJOUST                    |                                                        |
| 473 | STATE_STRANGULATE                   |                                                        |
| 474 | STATE_READYSPELLOMNI                |                                                        |
| 475 | STATE_HOLD_JOUST                    |                                                        |
| 476 | ONESHOT_CRY (JAINA PROUDMOORE ONLY) |                                                        |
