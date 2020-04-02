import requests 
import os
path = os.getcwd()
print ("Welcome to DO")
url = input("Pleast input the downloade links : ")
savename = input("Pleast input the savename :")
savepath = path + "/" + savename
r = requests.get(url) 
with open(savepath, "wb") as code:
     code.write(r.content)

