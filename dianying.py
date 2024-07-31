import json
import os
import pprint
import re
import subprocess

import requests

head={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

# 输入你想下载的视频地址URL
url="https://hey03.cjkypo.com/20220619/LblSI96x/hls/vN1rI5s0.ts"


response=requests.get(url,headers=head).content

with open("video\\1.mp4",mode='wb') as f:
    f.write(response)
    f.close()
