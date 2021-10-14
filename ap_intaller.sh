#!/bin/sh
sleep 1
echo "Old Version Deleting..."
sleep 1
# if [ -d /usr/lib/enigma2/python/Plugins/Extensions/AudioPlus ]; then
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/AudioPlus
# fi
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
echo "New Version Installed"
# sleep 2
# init 4
# echo "Restarting your enigma2 gui..."
# init 3
exit 0

