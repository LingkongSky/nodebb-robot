import asyncio
import os
import shutil
import signal
import subprocess

import psutil
import yaml
import sys
import utils
from decode import inputs


async def main():
    utils.file_scanner()
    utils.status_update()
    if len(sys.argv) < 2:
        print("Use --help to print the usage")
        sys.exit()

    command = sys.argv[1]
    match command:
        case "start":
            await start()
        case "stop":
            stop()
        case "create":
            create()
        case "list":
            lists()
        case "-h":
            helps()
        case "--help":
            helps()
        case _:
            print("Use --help to print the usage")


async def start():
    arrays = ["", "", ""]
    i = 0
    for arg in sys.argv:
        arrays[i] = arg
        i = i + 1

    if arrays[2] != "":
        name = arrays[2]
    else:
        name = "default"

    # check the status
    status = ''
    try:
        with open("tasks.list") as f:
            lines = f.readlines()
        for line in lines:
            parts = line.strip().split(" ")
            if len(parts) == 2:
                if parts[0] == name:
                    status = parts[1]
                    break

    except FileNotFoundError:
        print(f"Task was not found")

    if status == "Enable":
        print(f"Task is running...")
        return

    try:
        with open('tasks/' + name + '/config.yaml', 'r', encoding='utf-8') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
            for i in result['robots']:
                await inputs(i, name)
    except IOError:
        print(IOError)


def stop():
    arrays = ["", "", ""]
    i = 0
    for arg in sys.argv:
        arrays[i] = arg
        i = i + 1

    if arrays[2] != "":
        name = arrays[2]
    else:
        name = "default"

    # check the status
    status = ''
    try:
        with open("tasks.list") as f:
            lines = f.readlines()
        for line in lines:
            parts = line.strip().split(" ")
            if len(parts) == 2:
                if parts[0] == name:
                    status = parts[1]
                    break

    except FileNotFoundError:
        print(f"Task was not found")

    if status == "Disable":
        print(f"Task is already stopped...")
        return

    process_file_path = "tasks/" + name + "/process.pid"

    if os.path.exists(process_file_path):
        with open(process_file_path, "r") as process_file:
            pid = process_file.read().strip()
            if pid:
                try:
                    os.kill(int(pid), signal.SIGTERM)
                except (psutil.NoSuchProcess, ValueError):
                    print("Not found such process")


def create():
    arrays = ["", "", ""]
    i = 0
    for arg in sys.argv:
        arrays[i] = arg
        i = i + 1

    if arrays[2] != "":
        name = arrays[2]
    else:
        name = "default"

    if not os.path.exists("tasks"):
        os.makedirs("tasks")

    if not os.path.exists("tasks/" + name):
        os.makedirs("tasks/" + name)

    current_dir = os.getcwd()
    config_file_path = os.path.join(current_dir, "config.yaml")
    if os.path.exists(config_file_path):
        shutil.copy(config_file_path, "tasks/" + name)
    else:
        print("config.yaml isn't exist")


def lists():
    with open("tasks.list", "r") as f:
        lines = f.readlines()

        # 遍历每一行并处理
    for line in lines:
        parts = line.strip().split(" ")
        if len(parts) == 2:
            folder_name, status = parts
            if status == "Enable":
                # Use the ANSI encode
                print(f"{folder_name} \033[92m{status}\033[0m")
            elif status == "Disable":
                print(f"{folder_name} \033[91m{status}\033[0m")
            else:
                print(line.strip())
        else:
            print(line.strip())


def helps():
    print('''
    Welcome to use this tool to create a robot for nodebb.
    It produce by LingkongSky@gmail.com.
    Usage:
        create <name>           create a new task 
        start <name>            start the process by the task name
        stop <name>             stop the process by the task name
        list                    list the tasks
        -h, --help              print the usage
    ''')



loop = asyncio.get_event_loop()
task = loop.create_task(main())
loop.run_until_complete(task)

