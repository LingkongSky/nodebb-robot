import requests
from decode import write_log


async def tasks(array, name):
    api_url = array['api_url']
    bearer_token = array['bearer_token']
    uid = array['uid']
    cid = array['cid']
    title_content_type = array['title_content_type']
    title_request_type = array['title_request_type']
    title = array['title']
    text_content_type = array['text_content_type']
    text_request_type = array['text_request_type']
    text = array['text']

    if title_content_type == "url":
        if title_request_type == 'get':
            result = requests.get(title)
        else:
            result = requests.post(title)
        title = result.text

    if text_content_type == "url":
        if text_request_type == 'get':
            result = requests.get(text)
        else:
            result = requests.post(text)
        text = result.text

    response = create(api_url, bearer_token, uid, cid, title, text)
    if response.status_code != 200:
        print(response.text)
        write_log(name, response.text)
    else:
        print("200 OK")
        write_log(name, "200 OK")

def create(url, token, uid, cid, title, content):
    print("Running tasks...")
    headers = {"Authorization": "Bearer " + token}
    topic = {'uid': uid, 'cid': cid, 'title': title, 'content': content}
    response = requests.post(url, headers=headers, data=topic)
    return response
