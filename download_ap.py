# by digiteng...10.2021

try:
	import requests
	print("Downloading Latest File...")
	url = requests.get("https://api.github.com/repos/digiteng/plugins-test-/releases/latest")
	update_url = url.json()["assets"][0]["browser_download_url"]
	open("/tmp/AudioPlus.tar.gz", 'wb').write(requests.get(update_url, stream=True, allow_redirects=True).content)
except Exception as err:
	with open("/tmp/ap_installer_error_log", "a+") as f:
		f.write("ap_installer %s\n\n"%err)
	print(err)
	print("Download Failed...")
