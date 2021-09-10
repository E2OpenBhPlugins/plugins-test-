#!/bin/sh
echo ""
if [ -d /usr/lib/enigma2/python/Plugins/Extensions/AudioPlus ]; then
	rm -rf /usr/lib/enigma2/python/Plugins/Extensions/AudioPlus
fi

wget -qP /tmp/ "https://github.com/digiteng/plugins-test-/raw/master/AudioPlus.tar.gz"

echo "New Version Installing...wait..."
sleep 1
tar -xzf /tmp/AudioPlus.tar.gz -C /usr/lib/enigma2/python/Plugins/Extensions
sleep 1
rm -rf /tmp/AudioPlus.tar.gz
echo "New Version Installed"
sleep 2
init 4
echo "Restarting your enigma2 gui..."
init 3
exit 0
