import subprocess
import urllib.request

# retrieve zip file and place in dir
urllib.request.urlretrieve("https://download.geonames.org/export/zip/US.zip", "./US.zip")

# unzip file
subprocess.run(["unzip", "-o", "./zip_code_files/US.zip", "-d", "."])
