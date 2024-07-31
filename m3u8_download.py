import asyncio
import os
import re

import aiofiles
import aiohttp
import requests

head={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
# 得到第一层m3u8地址
def get_first_m3u8_url(url):
    resp=requests.get(url,headers=head)
    obj=re.compile(r'var vid="(?P<first_m3u8>.*?)";',re.S)
    result = obj.search(resp.text)
    resp.close()
    return result.group("first_m3u8").strip()
# 下载M3U8文件
def download_m3u8(m3u8_url,name):
    resp=requests.get(m3u8_url)
    resp.encoding="utf-8"
    with open(name,mode="w",encoding="utf=8") as f:
        f.write(resp.text)
    resp.close()

async def aio_download(up_url):
    tasks=[]
    async with aiofiles.open("m3u8/second_m3u8.txt",mode="r",encoding="utf-8") as f:
        async with aiohttp.ClientSession() as session:
            async for line in f:
                if line.startswith("#"):
                    continue
                else:
                    line=line.strip()
                    ts_url=up_url+"/"+line
                    name=line
                    tasks.append(download_ts(session,ts_url,name))
            await asyncio.wait(tasks)

async def download_ts(session,ts_url,name):
    async with session.get(ts_url) as resp:
        async with aiofiles.open(f"m3u8/{name}",mode="wb") as f:
            await f.write(await resp.content.read())
    print(name+" is success!")

def merge_ts():
    list=[]
    with open("m3u8/second_m3u8.txt",mode="r",encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            else:
                line=line.strip()
                list.append(f"m3u8/{line}")
    s="+".join(list)
    os.system(f"copy/b {s} m3u8/aa.mp4")




def main(url):
    first_m3u8_url=get_first_m3u8_url(url)
    # 下载第一层M3U8文件
    download_m3u8(first_m3u8_url,"m3u8/first_m3u8.txt")
    # first_m3u8_url=https://vip.lz-cdn9.com/20230823/18175_cd63de55/index.m3u8
    # second_m3u8_url=https://vip.lz-cdn9.com/20230823/18175_cd63de55/2000k/hls/mixed.m3u8
    # second_m3u8_ts=https://vip.lz-cdn9.com/20230823/18175_cd63de55/2000k/hls/706e76929e4000000.ts
    first_m3u8_url_up=first_m3u8_url.rsplit("/",1)[0]
    # 读取第一层m3u8文件得到第二层m3u8地址
    with open("m3u8/first_m3u8.txt",mode="r",encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            else:
                second_m3u8_url=first_m3u8_url_up+"/"+line.strip()
    download_m3u8(second_m3u8_url,"m3u8/second_m3u8.txt")
    # 读取第二层M3U8文件并下载ts内容
    second_m3u8_url_up=second_m3u8_url.rsplit("/",1)[0]
    asyncio.run(aio_download(second_m3u8_url_up))


if __name__ == '__main__':
    url="https://mjw21.com/dp/NTQyNS0xLTA=.html"
    main(url)