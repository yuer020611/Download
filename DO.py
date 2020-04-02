import requests 
print ("Welcome to do")
print ("D url=xxxxx path=xxxx")
url = 'http://www.anyuer.club/zb_system/login.php' 
r = requests.get(url) 
with open("D://001.php", "wb") as code:
     code.write(r.content)
