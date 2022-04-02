#coding:utf-8
import os
import time

os.system('masscan -iL ip.txt -p1-65535  -oL masscan.txt --rate=2000')
#判断当前目录是否有masscan.txt文件,如果没有则等待1秒，再次判断
while True:
    if os.path.exists("masscan.txt"):
        break
    else:
        print("Waiting for masscan.txt...")
        time.sleep(1)
#确认massscan.txt文件为否为空，如果为空则print("无开放端口")并退出程序，否则执行下面的代码
if os.path.getsize("masscan.txt") == 0:
    print("No open ports")
    exit()
else :
    print("MasscanConvert is running...")
    masscanfile = open("masscan.txt", "r")
    masscanfile.seek(0)
    for line in masscanfile:
        if line.startswith("#"):
            continue
        if line.startswith("open"):
            line = line.split(" ")
            print(line[3]+":"+line[2])
            with open("masscanconvert.txt", "a") as f:
                f.write(line[3]+":"+line[2]+"\n")
                f.close()
    masscanfile.close()
if os.path.exists("masscan.txt"):
    os.system('./httpx -l masscanconvert.txt -nc -o httpxresult.txt')
    os.remove("masscan.txt")
    print("httpx is done!")
else:
    print("未发现masscan.txt文件")
    exit()
