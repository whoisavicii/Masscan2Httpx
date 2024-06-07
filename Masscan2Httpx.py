#coding:utf-8
import os
import time

# Run masscan with specified options
os.system('masscan -iL ip.txt -p1-65535 -oL masscan.txt --rate=2000')

# Wait for the masscan.txt file to be created
while not os.path.exists("masscan.txt"):
    print("Waiting for masscan.txt...")
    time.sleep(1)

# Check if the masscan.txt file is empty
if os.path.getsize("masscan.txt") == 0:
    print("No open ports")
    exit()

print("MasscanConvert is running...")

# Process the masscan.txt file
with open("masscan.txt", "r") as masscanfile:
    with open("masscanconvert.txt", "a") as convertfile:
        for line in masscanfile:
            if line.startswith("open"):
                parts = line.split(" ")
                ip = parts[3]
                port = parts[2]
                convertfile.write(f"{ip}:{port}\n")
                print(f"{ip}:{port}")

# Run httpx with the generated masscanconvert.txt
if os.path.exists("masscan.txt"):
    os.system('./httpx -l masscanconvert.txt -nc -o httpxresult.txt')
    os.remove("masscan.txt")
    print("httpx is done!")
else:
    print("masscan.txt file not found")
    exit()
