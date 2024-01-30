import asyncio
import requests


async def tasks():
    # 这里是你要执行的任务代码
    print("Running tasks...")
    await asyncio.sleep(1)  # 模拟任务执行时间


# create(api_url, bearer_token, uid, cid, title, content)


def create(url, token, uid, cid, title, content):
    headers = {"Authorization": "Bearer " + token}
    topic = {'uid': uid, 'cid': cid, 'title': title, 'content': content}
    response = requests.post(url, headers=headers, data=topic)
    print(response.text)
    return response
