# Selenium Session Manager

![usage](https://raw.githubusercontent.com/codenoid/selenium-session-manager/master/ssm.png)

## Installation

1. Tested on Ubuntu
2. Python3 & pip3
3. google-chrome browser and chromedriver at `/usr/bin`
4. cd working folder and run `pip3 install -r requirements.txt`

## Example Usage

```
$ python3 app.py
Session path : ./
cmd~$ create myprofile
cmd~$ use myprofile
cmd~$ open https://web.whatsapp.com (scan the qr-code and get the logged session)
cmd~$ list session
myprofile
cmd~$ close myprofile (required!!, if you wanna save myprofile as zip)
cmd~$ save myprofile.zip (save myprofile session folder as .zip)
cmd~$ upload myprofile
{"success":true,"key":"UxiaHl","link":"https://file.io/UxiaHl","expiry":"14 days"} (download with "wget --content-disposition https://file.io/UxiaHl")
cmd~$ remove myprofile
cmd~$ list session
cmd~$ exit
```
## User Notes

1. file.io download link will expire after single GET connection to it
2. there is issue menu to report error or some other needed improvement