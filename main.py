import asyncio
import os
import signal
import yaml
from decode import inputs
import sys


async def main():
    file_scanner()

    if len(sys.argv) < 2:
        print("Use --help to print the usage")
        sys.exit()

    command = sys.argv[1]
    match command:
        case "start":
            await start()
        case "stop":
            stop()
        case "-l":
            lists()
        case "--list":
            lists()
        case "-h":
            helps()
        case "--help":
            helps()
        case _:
            print("Use --help to print the usage")


async def start():
    arrays = ["", "", "", ""]
    i = 0
    for arg in sys.argv:
        arrays[i] = arg
        i = i + 1

    if (arrays[2] == "-n" or arrays[2] == '--name') and arrays[3] != "":
        name = arrays[3]
    else:
        name = "default"

    try:
        with open('./config.yaml', 'r', encoding='utf-8') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
            for i in result['robots']:
                await inputs(i, name)
    except IOError:
        print(IOError)


def stop():
    arrays = ["", "", "", ""]
    i = 0
    for arg in sys.argv:
        arrays[i] = arg
        i = i + 1

    if (arrays[2] == "-n" or arrays[2] == '--name') and arrays[3] != "":
        name = arrays[3]
    else:
        name = "default"

    file_path = 'process.list'
    target_pid = None

    try:
        # 找到匹配的行并保存第二部分
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.split()
                if len(parts) > 0 and parts[0] == name:
                    target_pid = parts[1]
                    break

        # 从文件中删除匹配的行
        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(file_path, 'w') as file:
            for line in lines:
                parts = line.split()
                if len(parts) > 0 and parts[0] != name:
                    file.write(line)

        # 打印匹配行的第二部分
        if target_pid:
            print("close the " + str(target_pid))
            os.kill(int(target_pid), signal.SIGTERM)
        else:
            print("cannot found the process by the name")
    except OSError:
        print(OSError)


def lists():
    with open('process.list', 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) > 0:
                first_part = parts[0]
                print(first_part)


def helps():
    print('''
    Welcome to use this tool to create a robot for nodebb.
    It produce by LingkongSky@gmail.com.
    Usage:
        start                   start the process by default
        stop                    stop the process by default
        start -n, --name        start the process by the input name
        stop -n, --name         stop the process by the input name
        -l, --list              list the process
        -h, --help              print the usage
    ''')


def file_scanner():
    if not os.path.exists('./config.yaml'):
        # 创建并写入文件
        with open('./config.yaml', 'w') as file:
            file.write('''robots:
              -
                api_url: "https://www.example.com/api/v3/topics"
                bearer_token: "26370927-9d0f-44ae-b343-dd365464575d"
                uid: 173
                cid: 2
                title: "test"
                content_type: "url" #["url","string"]
                request_type: "get" # ['get','post']
                content: "http://118.31.18.68:8080/news/api/news-file/get"
                time_type: "routine" #['routine','everyday',''everymonth'','once']
                time: "60" #[seconds,"h:m","day-h:m","month-day-h:m"] example: 86400 23:00 07-20:00 12-07-20:00
            # -
            #   api_url: "https://www.example.com/api/v3/topics"
            #   bearer_token: "26370927-9d0f-44ae-b343-dd365464575d"
            #   uid: 173
            #   cid: 2
            #   title: "test"
            #   content_type: "url" #["url","string"]
            #   request_type: "get" # ['get','post']
            #   content: "http://118.31.18.68:8080/news/api/news-file/get"
            #   time_type: "routine" #['routine','everyday',''everymonth'','once']
            #   time: "60" #[seconds,"h:m","day-h:m","month-day-h:m"] example: 86400 23:00 07-20:00 12-07-20:00
            ''')
    if not os.path.exists('./process.list'):
        # 创建并写入文件
        open('./process.list', 'w')


loop = asyncio.get_event_loop()
task = loop.create_task(main())
loop.run_until_complete(task)
