#!/bin/sh
# wget -q "--no-check-certificate" https://github.com/digiteng/plugins-test-/raw/master/ap_installer.sh -O - | /bin/sh
sleep 1
echo "Old Version Deleting..."
rm -rf /usr/lib/enigma2/python/Plugins/Extensions/AudioPlus
rm -rf /tmp/AudioPlus.tar.gz
sleep 1
wget github.com/digiteng/plugins-test-/releases/latest/download/AudioPlus.tar.gz -P /tmp
echo "New Version Downloaded"
sleep 1
if [ -f /tmp/AudioPlus.tar.gz ]; then
	tar -xzf /tmp/AudioPlus.tar.gz -C /usr/lib/enigma2/python/Plugins/Extensions
fi
sleep 2
if [ -d /usr/lib/enigma2/python/Plugins/Extensions/AudioPlus ]; then
	echo "New Version Installed"
	rm -rf /tmp/AudioPlus.tar.gz
	sleep 2
	init 4
	echo "Restarting Your Enigma2 Gui..."
	init 3
else
	echo "New Version Failed To Load"
fi
exit 0
