import sys
import os
try:
  username = sys.argv[1]
  repo = sys.argv[2]
except:
  print("What do I download?")
  exit()
try: branch = sys.argv[3]
except: branch = "main" 
url = "https://github.com/{}/{}/archive/{}.zip".format(username, repo, branch) 
print("Downloading " + url + "...")
os.system("wget " + url)
os.system("unzip " + branch + ".zip")
os.system("rm " + branch + ".zip")
os.rename(repo + "-" + branch + ".zip", repo + ".zip")
print("Done.")
