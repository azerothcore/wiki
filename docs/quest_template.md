# quest\_template

[<-Back-to:World](database-world.md)

**Table: quest\_template**

Contains all basic definitions of available quests.

## **Structure**

| Field                           | Type         | Attribute | Key | Null | Default | Extra | Comment |
|---------------------------------|--------------|-----------|-----|------|---------|-------|---------|
| [ID][1]                         | mediumint(8) | unsigned  | PRI | NO   | 0       |       |         |
| [QuestType][2]                  | tinyint(3)   | unsigned  |     | NO   | 2       |       |         |
| [QuestLevel][3]                 | smallint(6)  |           |     | NO   | 1       |       |         |
| [MinLevel][4]                   | tinyint(3)   | unsigned  |     | NO   | 0       |       |         |
| [QuestSortID][5]                | smallint(6)  |           |     | NO   | 0       |       |         |
| [QuestInfoID][6]                | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [SuggestedGroupNum][7]          | tinyint(3)   | unsigned  |     | NO   | 0       |       |         |
| [RequiredFactionId1][8]         | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredFactionId2][9]         | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredFactionValue1][10]     | mediumint(9) |           |     | NO   | 0       |       |         |
| [RequiredFactionValue2][11]     | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardNextQuest][12]           | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardXPDifficulty][13]        | tinyint(3)   | unsigned  |     | NO   | 0       |       |         |
| [RewardMoney][14]               | int(11)      |           |     | NO   | 0       |       |         |
| [RewardBonusMoney][15]          | int(10)      | unsigned  |     | NO   | 0       |       |         |
| [RewardDisplaySpell][16]        | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardSpell][17]               | int(11)      |           |     | NO   | 0       |       |         |
| [RewardHonor][18]               | int(11)      |           |     | NO   | 0       |       |         |
| [RewardKillHonor][19]           | float        |           |     | NO   | 0       |       |         |
| [StartItem][20]                 | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [Flags][21]                     | int(10)      | unsigned  |     | NO   | 0       |       |         |
| [RequiredPlayerKills][22]       | tinyint(3)   | unsigned  |     | NO   | 0       |       |         |
| [RewardItem1][23]               | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardAmount1][24]             | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardItem2][25]               | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardAmount2][26]             | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardItem3][27]               | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardAmount3][28]             | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardItem4][29]               | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardAmount4][30]             | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [ItemDrop1][31]                 | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [ItemDropQuantity1][32]         | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [ItemDrop2][33]                 | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [ItemDropQuantity2][34]         | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [ItemDrop3][35]                 | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [ItemDropQuantity3][36]         | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [ItemDrop4][37]                 | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [ItemDropQuantity4][38]         | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemID1][39]       | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity1][40] | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemID2][41]       | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity2][42] | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemID3][43]       | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity3][44] | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemID4][45]       | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity4][46] | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemID5][47]       | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity5][48] | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemID6][49]       | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity6][50] | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [POIContinent][51]              | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [POIx][52]                      | float        |           |     | NO   | 0       |       |         |
| [POIy][53]                      | float        |           |     | NO   | 0       |       |         |
| [POIPriority][54]               | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardTitle][55]               | tinyint(3)   | unsigned  |     | NO   | 0       |       |         |
| [RewardTalents][56]             | tinyint(3)   | unsigned  |     | NO   | 0       |       |         |
| [RewardArenaPoints][57]         | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardFactionID1][58]          | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardFactionValue1][59]       | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardFactionOverride1][60]    | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardFactionID2][61]          | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardFactionValue2][62]       | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardFactionOverride2][63]    | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardFactionID3][64]          | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardFactionValue3][65]       | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardFactionOverride3][66]    | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardFactionID4][67]          | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardFactionValue4][68]       | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardFactionOverride4][69]    | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardFactionID5][70]          | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardFactionValue5][71]       | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardFactionOverride5][72]    | mediumint(9) |           |     | NO   | 0       |       |         |
| [TimeAllowed][73]               | int(10)      | unsigned  |     | NO   | 0       |       |         |
| [AllowableRaces][74]            | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [LogTitle][75]                  | text         |           |     | YES  |         |       |         |
| [LogDescription][76]            | text         |           |     | YES  |         |       |         |
| [QuestDescription][77]          | text         |           |     | YES  |         |       |         |
| [AreaDescription][78]           | text         |           |     | YES  |         |       |         |
| [QuestCompletionLog][79]        | text         |           |     | YES  |         |       |         |
| [RequiredNpcOrGo1][80]          | mediumint(9) |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGo2][81]          | mediumint(9) |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGo3][82]          | mediumint(9) |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGo4][83]          | mediumint(9) |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount1][84]     | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount2][85]     | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount3][86]     | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount4][87]     | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemId1][88]           | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemId2][89]           | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemId3][90]           | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemId4][91]           | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemId5][92]           | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemId6][93]           | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemCount1][94]        | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemCount2][95]        | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemCount3][96]        | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemCount4][97]        | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemCount5][98]        | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemCount6][99]        | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [Unknown0][100]                 | tinyint(3)   | unsigned  |     | NO   | 0       |       |         |
| [ObjectiveText1][101]           | text         |           |     | YES  |         |       |         |
| [ObjectiveText2][102]           | text         |           |     | YES  |         |       |         |
| [ObjectiveText3][103]           | text         |           |     | YES  |         |       |         |
| [ObjectiveText4][104]           | text         |           |     | YES  |         |       |         |
| [VerifiedBuild][105]            | smallint(6)  |           |     | YES  | 0       |       |         |

[1]: #ID
[2]: #QuestType
[3]: #QuestLevel
[4]: #MinLevel
[5]: #QuestSortID
[6]: #QuestInfoID
[7]: #SuggestedGroupNum
[8]: #RequiredFactionId1
[9]: #RequiredFactionId2
[10]: #RequiredFactionValue1
[11]: #RequiredFactionValue2
[12]: #RewardNextQuest
[13]: #RewardXPDifficulty
[14]: #RewardMoney
[15]: #RewardBonusMoney
[16]: #RewardDisplaySpell
[17]: #RewardSpell
[18]: #RewardHonor
[19]: #RewardKillHonor
[20]: #StartItem
[21]: #Flags
[22]: #RequiredPlayerKills
[23]: #RewardItem1
[24]: #RewardAmount1
[25]: #RewardItem2
[26]: #RewardAmount2
[27]: #RewardItem3
[28]: #RewardAmount3
[29]: #RewardItem4
[30]: #RewardAmount4
[31]: #ItemDrop1
[32]: #ItemDropQuantity1
[33]: #ItemDrop2
[34]: #ItemDropQuantity2
[35]: #ItemDrop3
[36]: #ItemDropQuantity3
[37]: #ItemDrop4
[38]: #ItemDropQuantity4
[39]: #RewardChoiceItemID1
[40]: #RewardChoiceItemQuantity1
[41]: #RewardChoiceItemID2
[42]: #RewardChoiceItemQuantity2
[43]: #RewardChoiceItemID3
[44]: #RewardChoiceItemQuantity3
[45]: #RewardChoiceItemID4
[46]: #RewardChoiceItemQuantity4
[47]: #RewardChoiceItemID5
[48]: #RewardChoiceItemQuantity5
[49]: #RewardChoiceItemID6
[50]: #RewardChoiceItemQuantity6
[51]: #POIContinent
[52]: #POIx
[53]: #POIy
[54]: #POIPriority
[55]: #RewardTitle
[56]: #RewardTalents
[57]: #RewardArenaPoints
[58]: #RewardFactionID1
[59]: #RewardFactionValue1
[60]: #RewardFactionOverride1
[61]: #RewardFactionID2
[62]: #RewardFactionValue2
[63]: #RewardFactionOverride2
[64]: #RewardFactionID3
[65]: #RewardFactionValue3
[66]: #RewardFactionOverride3
[67]: #RewardFactionID4
[68]: #RewardFactionValue4
[69]: #RewardFactionOverride4
[70]: #RewardFactionID5
[71]: #RewardFactionValue5
[72]: #RewardFactionOverride5
[73]: #TimeAllowed
[74]: #AllowableRaces
[75]: #LogTitle
[76]: #LogDescription
[77]: #QuestDescription
[78]: #AreaDescription
[79]: #QuestCompletionLog
[80]: #RequiredNpcOrGo1
[81]: #RequiredNpcOrGo2
[82]: #RequiredNpcOrGo3
[83]: #RequiredNpcOrGo4
[84]: #RequiredNpcOrGoCount1
[85]: #RequiredNpcOrGoCount2
[86]: #RequiredNpcOrGoCount3
[87]: #RequiredNpcOrGoCount4
[88]: #RequiredItemId1
[89]: #RequiredItemId2
[90]: #RequiredItemId3
[91]: #RequiredItemId4
[92]: #RequiredItemId5
[93]: #RequiredItemId6
[94]: #RequiredItemCount1
[95]: #RequiredItemCount2
[96]: #RequiredItemCount3
[97]: #RequiredItemCount4
[98]: #RequiredItemCount5
[99]: #RequiredItemCount6
[100]: #Unknown0
[101]: #ObjectiveText1
[102]: #ObjectiveText2
[103]: #ObjectiveText3
[104]: #ObjectiveText4
[105]: #VerifiedBuild

**Description of the fields**
