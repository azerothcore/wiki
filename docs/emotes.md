---
redirect_from: "/Emotes"
---

# Emotes

[`Back-to:DBC`](dbc-index.md)

This DBC contains emotes which can be used by NPCs.

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db.md)  

## Structure

| Column | Type  | Comment                                                                                                                                               |
|--------|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1      | long  | An ID for the emote. Must be unique.                                                                                                                  |
| 2      | str   | A descriptive name for the emote.                                                                                                                     |
| 3      | long  | Refers to an ID in [this DBC file](http://collab.kpsn.org/display/tc/AnimationData). This is the ID of the animation to play.                         |
| 4      | flags |                                                                                                                                                       |
| 5      | flags |                                                                                                                                                       |
| 6      | long  |                                                                                                                                                       |
| 7      | long  | Refers to an ID in [this DBC file](http://collab.kpsn.org/display/tc/SoundEntries). This is the ID of the sound to play when the animation is played. |

Information on the structure this DBC file was taken from [here](https://web.archive.org/web/20161130074340/http://www.pxr.dk/wowdev/wiki/index.php?title=Emotes.dbc) and [here](https://wowdev.wiki/DB/Emotes). For any information on the columns without a comment, just refer to [that page](https://web.archive.org/web/20161130074340/http://www.pxr.dk/wowdev/wiki/index.php?title=Emotes.dbc) or [here](https://wowdev.wiki/DB/Emotes).

## Content

When testing the NPC emotes listed below using the *.npc playemote \#* command, the NPC generally continuously plays the specified emote. When playing the emote through, for example, and SAI script, the NPC may use the emote differently.

| ID  | Emote name                          | Comment                                       |
|-----|-------------------------------------|-----------------------------------------------|
| 0   | ONESHOT_NONE                        | The NPC reverts to its normal standing state. |
| 1   | ONESHOT_TALK(DNR)                   | The NPC plays the talking emote once.         |
| 2   | ONESHOT_BOW                         | The NPC plays the bowing emote once.          |
| 3   | ONESHOT_WAVE(DNR)                   | The NPC plays the wave emote once.            |
| 4   | ONESHOT_CHEER(DNR)                  | The NPC plays the cheering emote once.        |
| 5   | ONESHOT_EXCLAMATION(DNR)            | The NPC plays the exclamation emote once.     |
| 6   | ONESHOT_QUESTION                    | The NPC plays the question emote once.        |
| 7   | ONESHOT_EAT                         | The NPC plays the eating emote once.          |
| 10  | STATE_DANCE                         | The NPC continuously plays the dancing emote. |
| 11  | ONESHOT_LAUGH                       | The NPC plays the laughing emote once         |
| 12  | STATE_SLEEP                         |                                               |
| 13  | STATE_SIT                           |                                               |
| 14  | ONESHOT_RUDE(DNR)                   |                                               |
| 15  | ONESHOT_ROAR(DNR)                   |                                               |
| 16  | ONESHOT_KNEEL                       |                                               |
| 17  | ONESHOT_KISS                        |                                               |
| 18  | ONESHOT_CRY                         |                                               |
| 19  | ONESHOT_CHICKEN                     |                                               |
| 20  | ONESHOT_BEG                         |                                               |
| 21  | ONESHOT_APPLAUD                     |                                               |
| 22  | ONESHOT_SHOUT(DNR)                  |                                               |
| 23  | ONESHOT_FLEX                        |                                               |
| 24  | ONESHOT_SHY(DNR)                    |                                               |
| 25  | ONESHOT_POINT(DNR)                  |                                               |
| 26  | STATE_STAND                         |                                               |
| 27  | STATE_READYUNARMED                  |                                               |
| 28  | STATE_WORK_SHEATHED                 |                                               |
| 29  | STATE_POINT(DNR)                    |                                               |
| 30  | STATE_NONE                          |                                               |
| 33  | ONESHOT_WOUND                       |                                               |
| 34  | ONESHOT_WOUNDCRITICAL               |                                               |
| 35  | ONESHOT_ATTACKUNARMED               |                                               |
| 36  | ONESHOT_ATTACK1H                    |                                               |
| 37  | ONESHOT_ATTACK2HTIGHT               |                                               |
| 38  | ONESHOT_ATTACK2H_LOOSE              |                                               |
| 39  | ONESHOT_PARRYUNARMED                |                                               |
| 43  | ONESHOT_PARRYSHIELD                 |                                               |
| 44  | ONESHOT_READYUNARMED                |                                               |
| 45  | ONESHOT_READY1H                     |                                               |
| 48  | ONESHOT_READYBOW                    |                                               |
| 50  | ONESHOT_SPELLPRECAST                |                                               |
| 51  | ONESHOT_SPELLCAST                   |                                               |
| 53  | ONESHOT_BATTLEROAR                  |                                               |
| 54  | ONESHOT_SPECIALATTACK1H             |                                               |
| 60  | ONESHOT_KICK                        |                                               |
| 61  | ONESHOT_ATTACKTHROWN                |                                               |
| 64  | STATE_STUN                          |                                               |
| 65  | STATE_DEAD                          |                                               |
| 66  | ONESHOT_SALUTE                      |                                               |
| 68  | STATE_KNEEL                         |                                               |
| 69  | STATE_USESTANDING                   |                                               |
| 70  | ONESHOT_WAVE_NOSHEATHE              |                                               |
| 71  | ONESHOT_CHEER_NOSHEATHE             |                                               |
| 92  | ONESHOT_EAT_NOSHEATHE               |                                               |
| 93  | STATE_STUN_NOSHEATHE                |                                               |
| 94  | ONESHOT_DANCE                       |                                               |
| 104 | ONESHOT_WHISTLE                     |                                               |
| 113 | ONESHOT_SALUTE_NOSHEATH             |                                               |
| 133 | STATE_USESTANDING_NOSHEATHE         |                                               |
| 153 | ONESHOT_LAUGH_NOSHEATHE             |                                               |
| 173 | STATE_WORK                          |                                               |
| 193 | STATE_SPELLPRECAST                  |                                               |
| 213 | ONESHOT_READYRIFLE                  |                                               |
| 214 | STATE_READYRIFLE                    |                                               |
| 233 | STATE_WORK_MINING                   |                                               |
| 234 | STATE_WORK_CHOPWOOD                 |                                               |
| 253 | STATE_APPLAUD                       |                                               |
| 254 | ONESHOT_LIFTOFF                     |                                               |
| 273 | ONESHOT_YES(DNR)                    |                                               |
| 274 | ONESHOT_NO(DNR)                     |                                               |
| 275 | ONESHOT_TRAIN(DNR)                  |                                               |
| 293 | ONESHOT_LAND                        |                                               |
| 313 | STATE_AT_EASE                       |                                               |
| 333 | STATE_READY1H                       |                                               |
| 353 | STATE_SPELLKNEELSTART               |                                               |
| 373 | STAND_STATE_SUBMERGED               |                                               |
| 374 | ONESHOT_SUBMERGE                    |                                               |
| 375 | STATE_READY2H                       |                                               |
| 376 | STATE_READYBOW                      |                                               |
| 377 | ONESHOT_MOUNTSPECIAL                |                                               |
| 378 | STATE_TALK                          |                                               |
| 379 | STATE_FISHING                       |                                               |
| 380 | ONESHOT_FISHING                     |                                               |
| 381 | ONESHOT_LOOT                        |                                               |
| 382 | STATE_WHIRLWIND                     |                                               |
| 383 | STATE_DROWNED                       |                                               |
| 384 | STATE_HOLD_BOW                      |                                               |
| 385 | STATE_HOLD_RIFLE                    |                                               |
| 386 | STATE_HOLD_THROWN                   |                                               |
| 387 | ONESHOT_DROWN                       |                                               |
| 388 | ONESHOT_STOMP                       |                                               |
| 389 | ONESHOT_ATTACKOFF                   |                                               |
| 390 | ONESHOT_ATTACKOFFPIERCE             |                                               |
| 391 | STATE_ROAR                          |                                               |
| 392 | STATE_LAUGH                         |                                               |
| 393 | ONESHOT_CREATURE_SPECIAL            |                                               |
| 394 | ONESHOT_JUMPLANDRUN                 |                                               |
| 395 | ONESHOT_JUMPEND                     |                                               |
| 396 | ONESHOT_TALK_NOSHEATHE              |                                               |
| 397 | ONESHOT_POINT_NOSHEATHE             |                                               |
| 398 | STATE_CANNIBALIZE                   |                                               |
| 399 | ONESHOT_JUMPSTART                   |                                               |
| 400 | STATE_DANCESPECIAL                  |                                               |
| 401 | ONESHOT_DANCESPECIAL                |                                               |
| 402 | ONESHOT_CUSTOMSPELL01               |                                               |
| 403 | ONESHOT_CUSTOMSPELL02               |                                               |
| 404 | ONESHOT_CUSTOMSPELL03               |                                               |
| 405 | ONESHOT_CUSTOMSPELL04               |                                               |
| 406 | ONESHOT_CUSTOMSPELL05               |                                               |
| 407 | ONESHOT_CUSTOMSPELL06               |                                               |
| 408 | ONESHOT_CUSTOMSPELL07               |                                               |
| 409 | ONESHOT_CUSTOMSPELL08               |                                               |
| 410 | ONESHOT_CUSTOMSPELL09               |                                               |
| 411 | ONESHOT_CUSTOMSPELL10               |                                               |
| 412 | STATE_EXCLAIM                       |                                               |
| 413 | STATE_DANCE_CUSTOM                  |                                               |
| 415 | STATE_SIT_CHAIR_MED                 |                                               |
| 416 | STATE_CUSTOM_SPELL_01               |                                               |
| 417 | STATE_CUSTOM_SPELL_02               |                                               |
| 418 | STATE_EAT                           |                                               |
| 419 | STATE_CUSTOM_SPELL_04               |                                               |
| 420 | STATE_CUSTOM_SPELL_03               |                                               |
| 421 | STATE_CUSTOM_SPELL_05               |                                               |
| 422 | STATE_SPELLEFFECT_HOLD              |                                               |
| 423 | STATE_EAT_NO_SHEATHE                |                                               |
| 424 | STATE_MOUNT                         |                                               |
| 425 | STATE_READY2HL                      |                                               |
| 426 | STATE_SIT_CHAIR_HIGH                |                                               |
| 427 | STATE_FALL                          |                                               |
| 428 | STATE_LOOT                          |                                               |
| 429 | STATE_SUBMERGED                     |                                               |
| 430 | ONESHOT_COWER(DNR)                  |                                               |
| 431 | STATE_COWER                         |                                               |
| 432 | ONESHOT_USESTANDING                 |                                               |
| 433 | STATE_STEALTH_STAND                 |                                               |
| 434 | ONESHOT_OMNICAST_GHOUL (W/SOUND     |                                               |
| 435 | ONESHOT_ATTACKBOW                   |                                               |
| 436 | ONESHOT_ATTACKRIFLE                 |                                               |
| 437 | STATE_SWIM_IDLE                     |                                               |
| 438 | STATE_ATTACK_UNARMED                |                                               |
| 439 | ONESHOT_SPELLCAST (W/SOUND)         |                                               |
| 440 | ONESHOT_DODGE                       |                                               |
| 441 | ONESHOT_PARRY1H                     |                                               |
| 442 | ONESHOT_PARRY2H                     |                                               |
| 443 | ONESHOT_PARRY2HL                    |                                               |
| 444 | STATE_FLYFALL                       |                                               |
| 445 | ONESHOT_FLYDEATH                    |                                               |
| 446 | STATE_FLY_FALL                      |                                               |
| 447 | ONESHOT_FLY_SIT_GROUND_DOWN         |                                               |
| 448 | ONESHOT_FLY_SIT_GROUND_UP           |                                               |
| 449 | ONESHOT_EMERGE                      |                                               |
| 450 | ONESHOT_DRAGONSPIT                  |                                               |
| 451 | STATE_SPECIALUNARMED                |                                               |
| 452 | ONESHOT_FLYGRAB                     |                                               |
| 453 | STATE_FLYGRABCLOSED                 |                                               |
| 454 | ONESHOT_FLYGRABTHROWN               |                                               |
| 455 | STATE_FLY_SIT_GROUND                |                                               |
| 456 | STATE_WALKBACKWARDS                 |                                               |
| 457 | ONESHOT_FLYTALK                     |                                               |
| 458 | ONESHOT_FLYATTACK1H                 |                                               |
| 459 | STATE_CUSTOMSPELL08                 |                                               |
| 460 | ONESHOT_FLY_DRAGONSPIT              |                                               |
| 461 | STATE_SIT_CHAIR_LOW                 |                                               |
| 462 | ONE_SHOT_STUN                       |                                               |
| 463 | ONESHOT_SPELLCAST_OMNI              |                                               |
| 465 | STATE_READYTHROWN                   |                                               |
| 466 | ONESHOT_WORK_CHOPWOOD               |                                               |
| 467 | ONESHOT_WORK_MINING                 |                                               |
| 468 | STATE_SPELL_CHANNEL_OMNI            |                                               |
| 469 | STATE_SPELL_CHANNEL_DIRECTED        |                                               |
| 470 | STAND_STATE_NONE                    |                                               |
| 471 | STATE_READYJOUST                    |                                               |
| 473 | STATE_STRANGULATE                   |                                               |
| 474 | STATE_READYSPELLOMNI                |                                               |
| 475 | STATE_HOLD_JOUST                    |                                               |
| 476 | ONESHOT_CRY (JAINA PROUDMOORE ONLY) |                                               |
