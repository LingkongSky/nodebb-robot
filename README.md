# English
## nodebb-robot
A topic robot use for nodebb，which can post data by string or url.Support the regular and multitasks.
Environment：Python3.11
## Build
````
pip install -r requirements.txt
pyinstaller ./main.py --onefile -p /usr/local/python/python3.11/lib/python3.11/site-packages
````
## Usage
````
vim config.yaml
chmod +x nodebb-robot
./nodebb-robot create <name>
./nodebb-robot start <name>
````
````
        create <name>           create a new task 
        start <name>            start the process by the task name
        stop <name>             stop the process by the task name
        list                    list the tasks
        log <name>              print the task log
        help                    print the usage
````

## Config
````
robots:
   -
      api_url : "https://www.example.com/api/v3/topics" #your website
      bearer_token : "f65632af-8115-4ab5-b63d-9fcae6198d15"#the admin page - API user uuid
      uid : 173 #user uuid
      cid : 2 #channel id
      title : "test" # topic title
      content_type: "url" #["url","string"]
      request_type: "get" # ['get','post'] if choose the url,the request method
      content : "http://118.31.18.68:8080/news/api/news-file/get" #string or url callback string
      time_type: "routine" #['routine','everyday',''everymonth'','once'] #execute rule
      time: "60" #[seconds,"h:m","day-h:m","month-day-h:m"] example: 86400  23:00 07-20:00  12-07-20:00
````

***
# 简体中文
## nodebb-robot
一个用于Nodebb的论坛机器人，可通过字符串或者链接来指定帖子内容。支持定时和多任务模式。
环境：Python3.11
## 构建
````
pip install -r requirements.txt
pyinstaller ./main.py --onefile -p /usr/local/python/python3.11/lib/python3.11/site-packages
````
## 使用方法
````
vim config.yaml
chmod +x nodebb-robot
./nodebb-robot create <name>
./nodebb-robot start <name>
````
````
        create <name>           创建一个新任务
        start <name>            根据任务名创建进程
        stop <name>             根据任务名关闭进程
        list                    列出所有任务
        log <name>              打印任务日志
        help                    打印使用方法
````
## 配置文件
````
robots:
   -
      api_url : "https://www.example.com/api/v3/topics" #你的论坛地址
      bearer_token : "f65632af-8115-4ab5-b63d-9fcae6198d15"#在管理页面-API访问中生成的用户id
      uid : 173 #机器人用户的uid
      cid : 2 #频道类别id
      title : "test" #帖子标题
      content_type: "url" #["url","string"] 正文类型
      request_type: "get" # ['get','post'] 如果选择了url，请求的发送方式
      content : "http://118.31.18.68:8080/news/api/news-file/get" #直接输入字符串或者选择url，生成url回调返回的字符串
      time_type: "routine" #['routine','everyday',''everymonth'','once'] #脚本的执行规则
      time: "60" #[seconds,"h:m","day-h:m","month-day-h:m"] example: 86400  23:00 07-20:00  12-07-20:00
````