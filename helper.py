from selenium import webdriver

def open_session(session_path, session_id):
	driverPath = '/usr/bin/chromedriver'

	options = webdriver.ChromeOptions()
	options.add_argument("--user-data-dir=" + session_path + session_id)
	options.add_argument('no-sandbox')
	options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36')
	return webdriver.Chrome(chrome_options=options, executable_path=driverPath)