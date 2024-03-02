import asyncio
import os
import shutil
import signal
import psutil
import yaml
import sys
import utils
import traceback
from decode import inputs


version = "1.3.1"
arrays = ["", "", ""]
d = 0
for arg in sys.argv:
    arrays[d] = arg
    d = d + 1

if arrays[2] != "":
    name = arrays[2]
else:
    name = "default"


async def main():
    utils.file_scanner()  # create the necessary files
    utils.status_update()  # update the tasks.list
    if len(sys.argv) < 2:
        helps()
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
        case "help":
            helps()
        case "logs":
            logs()
        case _:
            helps()


async def start():
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
        traceback.print_exc()

    if status == "Enable":
        print(f"Task is running...")
        return

    try:
        with open('tasks/' + name + '/config.yaml', 'r', encoding='utf-8') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
            for i in result['robots']:
                await inputs(i, name)
    except IOError as e:
        print(e)
        traceback.print_exc()


def stop():
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
        print(f"Task was not found:")
        traceback.print_exc()

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
                    traceback.print_exc()


def create():
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


def logs():
    try:
        with open('tasks/' + name + '/logs.txt', 'r', encoding='utf-8') as f:
            print(str(f.read()))
    except OSError as e:
        print(e)
        traceback.print_exc()
    # print the log and add log output


def helps():
    print('''    Nodebb-robot Running Version: ''' + version + '''
    Welcome to use this tool to create a robot for nodebb.
    It produce by LingkongSky@gmail.com.
    Project Site: https://github.com/LingkongSky/nodebb-robot.git
    Usage:
        create <name>           create a new task(default) 
        start <name>            start the process by the task name(default)
        stop <name>             stop the process by the task name(default)
        list                    list the tasks
        logs <name>             print the task log(default)''')


if sys.version_info < (3, 10):
    loop = asyncio.get_event_loop()
else:
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()

asyncio.set_event_loop(loop)
task = loop.create_task(main())
loop.run_until_complete(task)
