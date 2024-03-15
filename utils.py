import os
import sys
import psutil
from loguru import logger


def file_scanner():
    if not os.path.exists('./config.yaml'):
        with open('./config.yaml', 'w') as file:
            file.write('''robots:
   -
      api_url : "https://www.example.com/api/v3/topics"
      bearer_token : "f35452af-8225-4ab5-b63d-9fcae6266d15"
      cid : 2
      title_content_type: "string" # ["url","string"]
      title_request_type: "get" # ['get','post']
      title : "test"
      text_content_type: "string" #["url","string"]
      text_request_type: "get" # ['get','post']
      text : "http://118.31.18.68:8080/news/api/news-file/get"
      time_type: "routine" #['routine','everyday',''everymonth'','once']
      time: "60" #[seconds,"h:m","day-h:m","month-day-h:m"] example: 86400  23:00 07-20:00  12-07-20:00
            ''')
    if not os.path.exists('./tasks.list'):
        open('./tasks.list', 'w')


def status_update():
    if not os.path.exists("tasks"):
        os.makedirs("tasks")
        return

    tasks_list_file = "tasks.list"

    with open(tasks_list_file, "w") as f:
        for root, dirs, files in os.walk("tasks"):
            if "config.yaml" in files:
                folder_name = os.path.basename(root)
                process_file_path = os.path.join(root, "process.pid")
                result = 0
                if os.path.exists(process_file_path):
                    with open(process_file_path, "r") as process_file:
                        pid = process_file.read().strip()
                        if pid:
                            try:
                                process = psutil.Process(int(pid))
                                if process.is_running():
                                    result = 1
                            except (psutil.NoSuchProcess, ValueError):
                                pass

                else:
                    open(process_file_path, "w").close()
                if result == 1:
                    f.write(f"{folder_name} Enable\n")
                else:
                    f.write(f"{folder_name} Disable\n")


def write_process(name):
    pid = os.getpid()
    with open('tasks/' + name + '/process.pid', 'w', encoding='utf-8') as f:
        f.write(str(pid))


def write_log(name, content):
    with open('tasks/' + name + '/logs.txt', 'a', encoding='utf-8') as f:
        f.write(content + "\n")


def over():
    logger.error("Uncaught error occurred.")
    sys.exit()
