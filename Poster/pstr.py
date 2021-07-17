# -*- coding: utf-8 -*-
# by digiteng...
from Renderer import Renderer
from enigma import ePixmap, eTimer, loadJPG
from Components.Pixmap import Pixmap
import json, os, re
from urllib2 import urlopen, quote

tmdb_api = "3c3efcf47c3577558812bb9d64019d65"
path_folder = "/tmp/"

class pstr(Renderer):

	def __init__(self):
		Renderer.__init__(self)

	GUI_WIDGET = ePixmap
	def changed(self, what):
		self.event = ""
		if not self.instance:
			return
		if what[0] == self.CHANGED_CLEAR:
			self.instance.hide()
		if what[0] != self.CHANGED_CLEAR:
			self.event = self.source.event
			if self.event:
				evntNm = self.event.getEventName()
				dwn_poster = path_folder + "{}.jpg".format(evntNm)
				pstrNm = path_folder + evntNm + ".jpg"
				if os.path.exists(pstrNm):
					self.instance.setPixmap(loadJPG(pstrNm))
					self.instance.setScale(2)
					self.instance.show()
				else:
					try:
						url_tmdb = "https://api.themoviedb.org/3/search/multi?api_key={}&query={}".format(tmdb_api, quote(evntNm))
						poster = json.load(urlopen(url_tmdb))['results'][0]['poster_path']
						if poster:
							url_poster = "https://image.tmdb.org/t/p/w185{}".format(poster)
							with open(dwn_poster,'wb') as f:
								f.write(urlopen(url_poster).read())
					except:
						return
			else:
				self.instance.hide()
				return

	