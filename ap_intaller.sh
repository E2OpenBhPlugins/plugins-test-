#!/bin/sh
sleep 1
echo "Old Version Deleting..."
sleep 1
if [ -d /usr/lib/enigma2/python/Plugins/Extensions/AudioPlus ]; then
	rm -rf /usr/lib/enigma2/python/Plugins/Extensions/AudioPlus
fi

wget "https://github.com/digiteng/plugins-test-/raw/master/download_ap.py" -P /tmp/
sleep 2
if [ -f /tmp/download_ap.py ]; then
	python /tmp/download_ap.py
fi

sleep 1
exit 0
