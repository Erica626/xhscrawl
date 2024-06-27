import json
import os
import re
import execjs
import requests

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh-TW;q=0.9,zh;q=0.8,ms-MY;q=0.7,ms;q=0.6,en-MY;q=0.5,en;q=0.4,en-US;q=0.3",
    "cache-control": "no-cache",
    "content-type": "application/json;charset=UTF-8",
    "origin": "https://www.xiaohongshu.com",
    "pragma": "no-cache",
    "referer": "https://www.xiaohongshu.com/",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "x-b3-traceid": "8a03835d29e6f918",
}


def getXs(cookie, api, data):
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, "xhs.js")
    with open(file_path, 'r', encoding='utf-8') as f:
        jstext = f.read()

    ctx = execjs.compile(jstext)

    match = re.search(r'a1=([^;]+)', cookie)
    a1 = ""
    if match:
        a1 = match.group(1)
    else:
        print("关键参数a1获取失败，请检查你的cookie")
        return ""

    result = ctx.call("get_xs", api, data, a1)
    return result


def sentRequest(host, api, data, cookie):
    xs_xt = getXs(cookie, api, data)

    headers['cookie'] = cookie
    headers['x-s'] = xs_xt['X-s']
    headers['x-t'] = str(xs_xt['X-t'])

    url = host + api

    return requests.post(url=url, data=json.dumps(data, separators=(",", ":")), headers=headers)


def DoApi(param, cookie):
    api = '/api/sns/web/v1/homefeed'
    host = 'https://edith.xiaohongshu.com'
    return sentRequest(host, api, param, cookie)




if __name__ == '__main__':
    # 获取homefeed列表demo
    # warning 该js逆向只能用于改接口，如需其他接口请联系作者

    cookie = ""  #添加已登陆的cookie

    param = {
        "cursor_score":"",
        "num":31,
        "refresh_type":1,
        "note_index":31,
        "unread_begin_note_id":"",
        "unread_end_note_id":"",
        "unread_note_count":0,
        "category":"homefeed.fashion_v3",
        "search_key":"",
        "need_num":6,
        "image_formats":["jpg","webp","avif"],
        "need_filter_image":False
        }

    response = DoApi(param,cookie)
    if response.status_code == 200:
        print("Request successful:")
        print(response.json())
    else:
        print("POST request failed. Status code:", response.status_code)
        print(response.text)