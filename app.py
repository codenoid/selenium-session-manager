#!/usr/bin/python3

import os, time, subprocess, atexit
from helper import open_session

print("selenium session manager")

time.sleep(1.5)

# define a session path to use
# session_path/chrome_profile1
# session_path/chrome_profile2
# session_path/myprofile
session_path = input("Session path : ")

# put slash character in the end of path name
if not session_path:
	session_path = "./"
else:
	if session_path[-1] != "/":
		session_path += "/"

# quit() all driver when app receive exit signal
def doexit(driver):
	driver.quit()

# store all session inside dictionary
sessions = {}

# active session
use_session = ""

# is enable to use open and save
enable_command = False

while True:
	# primary stdin to receive command
	cmd = input("cmd~$ ")

	cmd = cmd.split(" ")

	if len(cmd) == 2:
		if "create" in cmd[0]:
			session_id = cmd[1]

			if session_id not in sessions:

				if not session_id:
					print("failed, empty session name")
					continue

				sessions[session_id] = open_session(session_path, session_id)
				atexit.register(doexit, sessions[session_id])

		if "use" in cmd[0]:
			if cmd[1] in sessions:
				use_session = cmd[1]
				enable_command = True
			else:
				session_id = cmd[1]
				if os.path.isdir(session_path + session_id):
					sessions[session_id] = open_session(session_path, session_id)
					atexit.register(doexit, sessions[session_id])
					use_session = session_id
					enable_command = True
				else:
					enable_command = False

		if "stop" in cmd[0] or "close" in cmd[0]:
			if cmd[1] in sessions:
				sessions[cmd[1]].quit()
				sessions.pop(cmd[1], None)

		if "remove" in cmd[0]:
			if cmd[1] in sessions:
				sessions[cmd[1]].quit()
				sessions.pop(cmd[1], None)
			target_path = session_path + cmd[1]
			subprocess.run(["rm", "-rf", target_path])

		if "open" in cmd[0]:
			if enable_command == True:
				if "http" in cmd[1]:
					sessions[use_session].get(cmd[1])
				else:
					print("[ERROR], need url scheme")
			else:
				print("[INFO] Please select a session")

		if "save" in cmd[0]:
			if enable_command == True:
				filename = cmd[1]
				subprocess.run(["zip", "-r", filename, use_session])
			else:
				print("[INFO] Please select a session")

		if "list" in cmd[0]:
			if "session" in cmd[1]:
				for key in sessions:
					print(key)

	if len(cmd) == 1:
		if "exit" in cmd[0]:
			exit(0)

		if "help" in cmd[0]:
			print("SELENIUM SESSION MANAGER - HELP")
			print("---------------------------------")
			print("cmd~$ create newsessionname (create new session)")
			print("cmd~$ use newsessionname (select session id to use)")
			print("cmd~$ stop|close newsessionname (select session to be stop)")
			print("cmd~$ remove newsessionname (remove session profile and it's folder)")
			print("cmd~$ open https://facebook.com (open web page)")
			print("cmd~$ save filename.zip (save current session as compressed zip file)")
			print("cmd~$ exit")

	time.sleep(0.5)