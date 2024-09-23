# Ubuntu 安装cloudflare
# !wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
# !sudo dpkg -i cloudflared-linux-amd64.deb

# Windows11 手动下载安装 cloudflare
# 浏览器打开 https://github.com/cloudflare/cloudflared/releases/download/2024.9.1/cloudflared-windows-amd64.msi

# 默认启动方式
# python use_cloudflare_tunnel.py --port 8080 --branch 1

import subprocess
import threading
import time
import socket
import urllib.request
import os
import argparse


def iframe_thread(port):
    while True:
        time.sleep(0.5)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(("127.0.0.1", port))
        if result == 0:
            break
        sock.close()
    print(
        "\nxxxxxx finished loading, trying to launch cloudflared (if it gets stuck here cloudflared is having issues)\n"
    )

    p = subprocess.Popen(
        ["cloudflared", "tunnel", "--url", "http://127.0.0.1:{}".format(port)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    for line in p.stderr:
        l = line.decode()
        if "trycloudflare.com " in l:
            print("This is the URL to access xxxxxx:", l[l.find("http") :], end="")
        # print(l, end='')


# 创建ArgumentParser对象
parser = argparse.ArgumentParser(description="控制运行分支的Python脚本")

# 添加命令行参数，确保参数是整数类型
parser.add_argument("--port", type=int, required=True, help="指定端口号")
parser.add_argument("--branch", type=int, required=True, help="指定分支值")

# 解析命令行参数
OutArgs = parser.parse_args()

threading.Thread(target=iframe_thread, daemon=True, args=(OutArgs.port,)).start()

if OutArgs.branch == 1:  # Ubuntu
    # # 显式加载环境变量
    # os.system("source /etc/profile")
    # # 我这里的jdk没有使用apt安装，所以需要手动添加环境变量，确定能通过os.system启动可以删掉这几个
    # os.environ["PATH"] = "/home/ubuntu/jdk1.8.0_192/bin:" + os.environ["PATH"]

    # 检查Java版本
    os.system("java -version")

# 启动kiftd
os.system("java -jar kiftd-*-RELEASE.jar -start")
