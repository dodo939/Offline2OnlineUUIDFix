# Offline2OnlineUUIDFix
Minecraft 服务器打开正版验证时，正常情况下会导致原来的离线玩家数据丢失，本项目将解决这个问题。
## 注意事项
+ 请把 exe 文件放在 Minecraft 服务器根目录下，在 Minecraft 服务器**关闭**的状态下运行
+ 程序涉及关键文件的操作，请按要求备份，如果用户没有备份造成了严重后果(所有玩家数据全部丢失)，作者**概不负责！**
+ 将 online-mode 设置为 true 之后，请在服务器下一次启动前运行该程序，因为任何产生的属于正版玩家的新数据会被**删除替换**
+ 如果你购买的是面板服，也就是无法运行自己的程序，提示：可以考虑将要修改的文件(夹)打包下载到本地，接着构造一个 Minecraft 服务器的结构，将该程序放到指定位置运行，然后将修改后的对应文件(夹)一一替换即可，下面展示了你需要构造的结构:
```
.
├── world (需要与server.properties 中的 level-name 的值相同，如果你听不懂，那你不需要关心这个)
│   ├── advancements
│   ├── playerdata
│   └── stats
├── banned-players.json
├── ops.json
├── whitelist.json
├── server.properties
└── Offline2OnlineUUIDFix.exe
```
