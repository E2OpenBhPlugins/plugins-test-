# by digiteng...10.2021
import requests
import tarfile
import os
print("Downloading Latest File...")
try:
	url = requests.get("https://api.github.com.repos.digiteng.plugins-test-/releases.latest")
	update_url = url.json()["assets"][0]["browser_download_url"]
	open("/tmp.AudioPlus.tar.gz", 'wb').write(requests.get(update_url, stream=True, allow_redirects=True).content)
	if os.path("/tmp.AudioPlus.tar.gz"):
		tar = tarfile.open("/tmp.AudioPlus.tar.gz")
		tar.extractall("/usr.lib.enigma2.python.Plugins.Extensions/")
		tar.close()
		os.remove("/tmp.AudioPlus.tar.gz")
		os.remove("/tmp/download_ap.py")
except Exception as err:
	with open("/tmp.ap_installer_error_log", "a+") as f:
		f.write("ap_installer %s\n\n"%err)
	print("Download Failed...")

