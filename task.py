import requests


async def tasks(array):
    # 这里是你要执行的任务代码
    api_url = array['api_url']
    bearer_token = array['bearer_token']
    uid = array['uid']
    cid = array['cid']
    title = array['title']
    content_type = array['content_type']
    request_type = array['request_type']
    content = array['content']

    # await asyncio.sleep(1)  # 模拟任务执行时间

    if content_type == "string":
        print("Running tasks...")
        create(api_url, bearer_token, uid, cid, title, content)
    elif content_type == "url":
        if request_type == 'get':
            result = requests.get(content)
        else:
            result = requests.post(content)
        content = result.text
        create(api_url, bearer_token, uid, cid, title, content)


def create(url, token, uid, cid, title, content):
    headers = {"Authorization": "Bearer " + token}
    topic = {'uid': uid, 'cid': cid, 'title': title, 'content': content}
    response = requests.post(url, headers=headers, data=topic)
    print(response.text)
    return response
