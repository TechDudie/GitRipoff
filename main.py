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
files = [f for f in os.listdir('.') if os.path.isfile(f)]
os.system("wget " + url)
downloaded = [f for f in os.listdir('.') if os.path.isfile(f)]
file = str(list(set(files) - set(downloaded))[0])
os.system("unzip " + file)
os.system("rm " + file)
print("Done.")
