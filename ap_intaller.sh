#!/bin/sh
echo ""
if [ -d /usr/lib/enigma2/python/Plugins/Extensions/AudioPlus ]; then
	rm -rf /usr/lib/enigma2/python/Plugins/Extensions/AudioPlus
fi

# if [ -f /var/lib/dpkg ]; then
	# checkos='/var/lib/dpkg'
	# os='Dream'
# else
	# checkos='/var/lib/opkg'
	# os='OpenOE'
# echo "your stb : " $os

# fi

# if [ $os = "OpenOE" ]; then
	# opkg update
	# opkg install gstreamer1.0-plugins-base-volume
	# opkg install gstreamer1.0-plugins-good-ossaudio
	# opkg install gstreamer1.0-plugins-good-mpg123
	# opkg install gstreamer1.0-plugins-good-equalizer
# else 
	# apt-get update
	# apt-get -y install gstreamer1.0-plugins-base-volume 
	# apt-get -y install gstreamer1.0-plugins-good-ossaudio
	# apt-get -y install gstreamer1.0-plugins-good-mpg123
	# apt-get -y install gstreamer1.0-plugins-good-equalizer
# fi

wget -qP /tmp/ "https://github.com/digiteng/plugins-test-/releases/download/aplus/AudioPlus.tar.gz"

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
