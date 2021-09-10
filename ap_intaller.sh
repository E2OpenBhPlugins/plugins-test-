#!/bin/sh

if [ -d /usr/lib/enigma2/python/Plugins/Extensions/AudioPlus ]; then
	rm -rf /usr/lib/enigma2/python/Plugins/Extensions/AudioPlus
fi

if [ -d "/var/lib/dpkg" ]; then 
	os='Dream' 
elif [ -d "/var/lib/opkg" ]; then 
	os='OpenOE' 
else 
	os='Unknown' 
fi 
echo "Your Stb : " $os

if [ ! -f "/usr/bin/gst-launch-1.0" ]; then 
	if [ $os = 'OpenOE' ]; then
		opkg update
		opkg install gstreamer1.0-plugins-base-volume
		opkg install gstreamer1.0-plugins-good-ossaudio
		opkg install gstreamer1.0-plugins-good-mpg123
		opkg install gstreamer1.0-plugins-good-equalizer
	else 
		apt-get update
		apt-get -y install gstreamer1.0-plugins-base-volume 
		apt-get -y install gstreamer1.0-plugins-good-ossaudio
		apt-get -y install gstreamer1.0-plugins-good-mpg123
		apt-get -y install gstreamer1.0-plugins-good-equalizer
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
exit


