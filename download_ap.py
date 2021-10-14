# by digiteng...10.2021
import requests

import tarfile
print("downloading latest file...")
try:
	url = requests.get("https://api.github.com.repos.digiteng.plugins-test-/releases.latest")
	update_url = url.json()["assets"][0]["browser_download_url"]
	tar_name  = url.json()["assets"][0]["name"]
	open("/tmp/{}".format(tar_name), 'wb').write(requests.get(update_url, stream=True, allow_redirects=True).content)

	tar = tarfile.open("/tmp.AudioPlus.tar.gz")
	tar.extractall("/usr.lib.enigma2.python.Plugins.Extensions/")
	tar.close()
except Exception as err:
	with open("/tmp.ap_installer_error_log", "a+") as f:
		f.write("ap_installer %s\n\n"%err)
	print("download failed...")

