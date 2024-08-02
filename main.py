import os
import re

import requests


def get_uuid(user_name):
    global uuid
    resp = requests.get("https://api.mojang.com/users/profiles/minecraft/" + user_name)
    uuid = resp.json().get("id")
    if uuid:
        return f"{uuid[:8]}-{uuid[8:12]}-{uuid[12:16]}-{uuid[16:20]}-{uuid[20:]}"
    return None


def main():
    with open("server.properties", "r", encoding='utf-8') as f:
        config = f.read()
    level_name = re.search(r"level-name\s*=\s*(.+)", config).group(1).strip()

    input(
        f"使用之前请确保: \n  1. 良好的网络环境\n  2. 请备份以下文件或文件夹: \n    ops.json\n    usercache.json\n    whitelist.json\n    banned-players.json\n    {level_name}/advancements\n    {level_name}/playerdata\n    {level_name}/stats\n按 Enter 继续, 按 Ctrl+C 或者直接关闭窗口退出"
    )

    with open("usercache.json", "r", encoding='utf-8') as f:
        users = f.read()
    online_uuids = []
    names = re.findall(r'"name":\s*"([^"]+)"', users)
    offline_uuids = re.findall(r'"uuid":\s*"([0-9a-fA-F-]+)"', users)

    count = 0
    print("正在从 usercache.json 中查询玩家正版UUID...")
    for name in names:
        online_uuids.append(get_uuid(name))
        print(f"  {name}: {online_uuids[count]}")
        count += 1

    print("正在将 ops.json 中玩家 UUID 修改为正版...")
    with open("ops.json", "r+", encoding='utf-8') as f:
        ops = f.read()
        for i in range(count):
            if online_uuids[i]:
                ops = ops.replace(offline_uuids[i], online_uuids[i])
        f.seek(0)
        f.truncate(0)
        f.write(ops)

    print("正在将 banned-players.json 中玩家 UUID 修改为正版...")
    with open("banned-players.json", "r+", encoding='utf-8') as f:
        bans = f.read()
        for i in range(count):
            if online_uuids[i]:
                bans = bans.replace(offline_uuids[i], online_uuids[i])
        f.seek(0)
        f.truncate(0)
        f.write(bans)

    print("正在将 whitelist.json 中玩家 UUID 修改为正版...")
    with open("whitelist.json", "r+", encoding='utf-8') as f:
        wls = f.read()
        for i in range(count):
            if online_uuids[i]:
                wls = wls.replace(offline_uuids[i], online_uuids[i])
        f.seek(0)
        f.truncate(0)
        f.write(wls)

    print("正在将 usercache.json 中玩家 UUID 修改为正版...")
    with open("usercache.json", "r+", encoding='utf-8') as f:
        caches = f.read()
        for i in range(count):
            if online_uuids[i]:
                caches = caches.replace(offline_uuids[i], online_uuids[i])
        f.seek(0)
        f.truncate(0)
        f.write(caches)

    successd = []

    os.chdir(level_name + "/playerdata")
    print(f"正在将 {level_name}/playerdata 中玩家 UUID 修改为正版...")
    for i in range(count):
        try:
            os.remove(online_uuids[i] + ".dat")
            os.remove(online_uuids[i] + ".dat_old")
        except:
            pass
        try:
            if online_uuids[i]:
                os.rename(offline_uuids[i] + ".dat", online_uuids[i] + ".dat")
                successd.append(names[i])
                os.rename(offline_uuids[i] + ".dat_old", online_uuids[i] + ".dat_old")
        except:
            pass

    os.chdir("../advancements")
    print(f"正在将 {level_name}/advancements 中玩家 UUID 修改为正版...")
    for i in range(count):
        try:
            os.remove(online_uuids[i] + ".json")
        except:
            pass
        try:
            if online_uuids[i]:
                os.rename(offline_uuids[i] + ".json", online_uuids[i] + ".json")
        except:
            pass

    os.chdir("../stats")
    print(f"正在将 {level_name}/stats 中玩家 UUID 修改为正版...")
    for i in range(count):
        try:
            os.remove(online_uuids[i] + ".json")
        except:
            pass
        try:
            if online_uuids[i]:
                os.rename(offline_uuids[i] + ".json", online_uuids[i] + ".json")
        except:
            pass

    print("成功将以下玩家数据转为正版数据: \n\n", successd)
    input("\n按 Enter 退出或者直接关闭窗口")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\n\n程序出现异常, 请将以下信息发送给开发者\n")
        print(e)
        input()
