#!/usr/bin/python
# -*- coding: utf-8 -*-

# by digiteng...(digiteng@gmail.com)
# https://github.com/digiteng/
# 06.2020 - 11.2020(v2.0) - 11.2021

from Plugins.Plugin import PluginDescriptor
from Components.config import config
import threading
from six.moves import reload_module
from . import xtra
from . import download

def ddwn():
	try:
		
		if config.plugins.xtraEvent.timerMod.value == True:
			download.downloads("").save()
		if config.plugins.xtraEvent.timerMod.value == True:
			tmr = config.plugins.xtraEvent.timer.value
			t = threading.Timer(3600*int(tmr), ddwn) # 1h=3600
			t.start()
	except Exception as err:
		with open("/tmp/xtra_error.log", "a+") as f:
			f.write("xtra plugin ddwn, %s\n\n"%err)
		
try:
	if config.plugins.xtraEvent.timerMod.value == True:
		threading.Timer(30, ddwn).start()
except Exception as err:
	with open("/tmp/xtra_error.log", "a+") as f:
		f.write("xtra plugin timer start, %s\n\n"%err)	

def main(session, **kwargs):
	try:
		reload_module(xtra)
		reload_module(download)
		session.open(xtra.xtra)
	except:
		import traceback
		traceback.print_exc()

def Plugins(**kwargs):
	return [PluginDescriptor(name="xtraEvent", description="Poster, Baskdrop, Banner, Info...Etc...Support...", where = PluginDescriptor.WHERE_PLUGINMENU, icon="plugin.png", fnc=main)]
