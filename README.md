# English
## nodebb-robot
A topic robot use for nodebb，which can post data by string or url.Support the regular and multitasks.
## Build
````
pip install requirements.txt
pyinstaller ./main.py --onefile
````
## Usage
````
vim config.yaml
chmod +x nodebb-robot
./nodebb-robot [options]
````
````
        start                   start the process by default
        stop                    stop the process by default
        start -n, --name        start the process by the input name
        stop -n, --name         stop the process by the input name
        -l, --list              list the process
        -h, --help              print the usage
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
## 构建
````
pip install requirements.txt
pyinstaller ./main.py --onefile
````
## 使用方法
````
pip install requirements.txt
vim config.yaml
python main.py &
````
````
        start                   以默认名称运行程序
        stop                    终止默认名称的程序
        start -n, --name        以自定义名称运行程序
        stop -n, --name         终止自定义名称的程序
        -l, --list              列出所有在运行的程序
        -h, --help              打印使用方法
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