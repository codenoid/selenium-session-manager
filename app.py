#!/usr/bin/python3

import os, time, atexit, subprocess
from selenium import webdriver

print("selenium session manager")

time.sleep(1.5)

session_id = input("Your session ID : ")

if session_id == "":
	exit(1)

driverPath = '/usr/bin/chromedriver'

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=" + session_id)
options.add_argument('no-sandbox')
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36')
driver = webdriver.Chrome(chrome_options=options, executable_path=driverPath)

def doexit():
	driver.quit()

atexit.register(doexit)

while True:
	cmd = input("cmd~$ ")

	cmd = cmd.split(" ")

	if len(cmd) == 2:
		if "open" in cmd[0]:
			if "http" in cmd[1]:
				driver.get(cmd[1])
			else:
				print("[ERROR], need url scheme")

		if "save" in cmd[0]:
			filename = cmd[1]
			subprocess.run(["zip", "-r", filename, session_id])

	if len(cmd) == 1:
		if "exit" in cmd[0]:
			exit(0)

		if "help" in cmd[0]:
			print("cmd~$ open https://facebook.com (open web page)")
			print("cmd~$ save filename.zip (save current session as .zip file)")
			print("cmd~$ exit")

	time.sleep(0.5)