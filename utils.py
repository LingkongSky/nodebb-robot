import os
import psutil


def file_scanner():
    if not os.path.exists('./config.yaml'):
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

                if os.path.exists(process_file_path):
                    with open(process_file_path, "r") as process_file:
                        pid = process_file.read().strip()
                        if pid:
                            try:
                                process = psutil.Process(int(pid))
                                if process.is_running():
                                    f.write(f"{folder_name} Enable\n")
                                else:
                                    f.write(f"{folder_name} Disable\n")
                            except (psutil.NoSuchProcess, ValueError):
                                f.write(f"{folder_name} Disable\n")
                        else:
                            f.write(f"{folder_name} Disable\n")
                else:
                    # 创建空的process文件
                    open(process_file_path, "w").close()
                    f.write(f"{folder_name} Disable\n")

