import json
import os
import pprint
import re
import subprocess

import requests

head={
    "Referer":"https://www.bilibili.com/",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
url="https://www.bilibili.com/video/BV1aN411e7BC"


response=requests.get(url,headers=head)
content = response.text
# print(content)
title=re.findall("<title data-vue-meta=\"true\">(.*?)</title>",response.text)[0]
play_info=re.findall("<script>window.__playinfo__=(.*?)</script>",response.text)[0]
print(title)
# print(play_info)
json_data=json.loads(play_info)
# print(json_data)
# pprint.pprint(json_data)
audio_url=json_data['data']['dash']['audio'][0]['baseUrl']
video_url=json_data['data']['dash']['video'][0]['baseUrl']
audio_content=requests.get(url=audio_url,headers=head).content
video_content=requests.get(url=video_url,headers=head).content
with open('video\\'+title+".mp3",mode='wb') as f:
    f.write(audio_content)
    f.close()
with open('video\\'+title+".mp4",mode='wb') as f:
    f.write(video_content)
    f.close()
COMMAND = f"ffmpeg -i video\\{title}.mp4 -i video\\{title}.mp3 -c:v copy -c:a aac -strict experimental video\\{title}output.mp4"
subprocess.run(COMMAND,shell=True)
os.remove(f'video\\{title}.mp3')
os.remove(f'video\\{title}.mp4')