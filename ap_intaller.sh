#!/bin/sh
# wget -q "--no-check-certificate" https://github.com/digiteng/plugins-test-/raw/master/ap_intaller.sh -O - | /bin/sh
sleep 1
echo "Old Version Deleting..."
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/AudioPlus
rm -rf /tmp/AudioPlus.tar.gz
rm -rf /tmp/download_ap.py
wget "https://github.com/digiteng/plugins-test-/raw/master/download_ap.py" -P /tmp/
sleep 2
if [ -f /tmp/download_ap.py ]; then
	python /tmp/download_ap.py
fi
sleep 1
if [ -f /tmp/AudioPlus.tar.gz ]; then
	tar -xzf /tmp/AudioPlus.tar.gz -C /usr/lib/enigma2/python/Plugins/Extensions
fi
if [ -d /usr/lib/enigma2/python/Plugins/Extensions/AudioPlus ]; then
	echo "New Version Installed"
	sleep 2
	init 4
	echo "Restarting Your Enigma2 Gui..."
	init 3
else
	echo "Installed Failed..."
fi
rm -rf /tmp/AudioPlus.tar.gz
rm -rf /tmp/download_ap.py

exit 0
