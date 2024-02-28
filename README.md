# English
## nodebb-robot
A topic robot use for nodebb,which can post data by string or url.Support the regular and multitasks.

Environment: Python3.11

## Planning
Add the function of image post.

## Build
````
pip install -r requirements.txt
pyinstaller ./main.py --onefile
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
        logs <name>              print the task log
````

## Config
````
robots:
   -
      api_url : "https://www.example.com/api/v3/topics" #your website
      bearer_token : "f65632af-8115-4ab5-b63d-9fcae6198d15" # the admin page - API user uuid
      uid : 173 # user id
      cid : 2 # channel id
      title_content_type: "string" # ["url","string"]
      title_request_type: "get" # ['get','post'] if choose the url,the request method
      title : "test" # topic title,string or request callback string
      text_content_type: "url" # ["url","string"]
      text_crequest_type: "get" # ['get','post'] if choose the url,the request method
      text : "http://www.example.com/get" # topic content,string or request callback string
      time_type: "routine" # ['routine','everyday',''everymonth'','once'] # execute rule
      time: "60" # [seconds,"h:m","day-h:m","month-day-h:m"] example: 86400  23:00 07-20:00  12-07-20:00
````

***
# 简体中文
## nodebb-robot
一个用于Nodebb的论坛机器人，可通过字符串或者链接来指定帖子内容。支持定时和多任务模式。

环境：Python3.11

## 计划
新增对图片的发送支持

## 构建
````
pip install -r requirements.txt
pyinstaller ./main.py --onefile
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
        logs <name>              打印任务日志
````
## 配置文件
````
robots:
   -
      api_url : "https://www.example.com/api/v3/topics" # 你的论坛地址
      bearer_token : "f65632af-8115-4ab5-b63d-9fcae6198d15"# 在管理页面-API访问中生成的用户id
      uid : 173 # 机器人用户的id
      cid : 2 # 频道类别id
      title_content_type: "url" # ["url","string"] 标题类型
      title_request_type: "get" # ['get','post'] 如果选择了url，请求的发送方式
      title : "test"  # 标题内容，直接输入字符串或者选择url，生成url回调返回的字符串
      text_content_type: "url" # ["url","string"] 正文类型
      text_request_type: "get" # ['get','post'] 如果选择了url，请求的发送方式
      text : "http://www.example.com/ge" # 正文内容，直接输入字符串或者选择url，生成url回调返回的字符串
      time_type: "routine" # ['routine','everyday',''everymonth'','once'] # 脚本的执行规则
      time: "60" # [seconds,"h:m","day-h:m","month-day-h:m"] example: 86400  23:00 07-20:00  12-07-20:00
````