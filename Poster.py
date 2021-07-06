# -*- coding: utf-8 -*-
# by digiteng...06.2021
# <widget source="session.Event_Now" render="Poster" position="0,0" size="300,500" language="en" zPosition="1" />
from Renderer import Renderer
from enigma import ePixmap, eTimer, loadJPG, eEPGCache, getBestPlayableServiceReference
from Components.Pixmap import Pixmap
import json, re, os, socket, sys
from thread import start_new_thread

tmdb_api = "3c3efcf47c3577558812bb9d64019d65"
epgcache = eEPGCache.getInstance()

PY3 = (sys.version_info[0] == 3)

if PY3:
	from urllib.parse import quote, urlencode
	from urllib.request import urlopen, Request
else:
	from urllib2 import urlopen, quote

if os.path.isdir("/media/e4"):
	path_folder = "/media/e4/poster/"
else:
	path_folder = "/media/usb/poster/"

REGEX = re.compile(
		r'([\(\[]).*?([\)\]])|'
		r'(: odc.\d+)|'
		r'(\d+: odc.\d+)|'
		r'(\d+ odc.\d+)|(:)|'
		r'( -(.*?).*)|(,)|'
		r'!|'
		r'/.*|'
		r'\|\s[0-9]+\+|'
		r'[0-9]+\+|'
		r'\s\d{4}\Z|'
		r'([\(\[\|].*?[\)\]\|])|'
		r'(\"|\"\.|\"\,|\.)\s.+|'
		r'\"|:|'
		r'Премьера\.\s|'
		r'(х|Х|м|М|т|Т|д|Д)/ф\s|'
		r'(х|Х|м|М|т|Т|д|Д)/с\s|'
		r'\s(с|С)(езон|ерия|-н|-я)\s.+|'
		r'\s\d{1,3}\s(ч|ч\.|с\.|с)\s.+|'
		r'\.\s\d{1,3}\s(ч|ч\.|с\.|с)\s.+|'
		r'\s(ч|ч\.|с\.|с)\s\d{1,3}.+|'
		r'\d{1,3}(-я|-й|\sс-н).+|', re.DOTALL)

class Poster(Renderer):

	def __init__(self):
		Renderer.__init__(self)
		self.language="en"
		self.sz="185,278"
		self.intCheck()

	def applySkin(self, desktop, parent):
		attribs = self.skinAttributes[:]
		for attrib, value in self.skinAttributes:
			if attrib == "language":
				self.language = value
			elif attrib == "size":
				self.sz = value.split(",")[0]
			
		self.skinAttributes = attribs
		return Renderer.applySkin(self, desktop, parent)
		
	def intCheck(self):
		try:
			socket.setdefaulttimeout(1)
			socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
			return True
		except:
			return False

	GUI_WIDGET = ePixmap
	def changed(self, what):
		try:
			if not self.instance:
				return
			if what[0] == self.CHANGED_CLEAR:
				self.instance.hide()
			if what[0] != self.CHANGED_CLEAR:
				self.event = self.source.event
				if self.event:
					self.delay2()
					evntNm = REGEX.sub('', self.event.getEventName()).strip()
					evntNm = evntNm.replace("Die ", "The ").replace("Das ", "The ").replace("und ", "and ").replace("LOS ", "The ").rstrip()
					dwn_poster = path_folder + "{}.jpg".format(evntNm)
					pstrNm = path_folder + evntNm + ".jpg"
					if os.path.exists(pstrNm):
						self.instance.setPixmap(loadJPG(pstrNm))
						self.instance.show()
					else:
						try:
							if self.intCheck():
								
								self.year = self.filterSearch()
								url_tmdb = "https://api.themoviedb.org/3/search/{}?api_key={}&query={}&language={}".format(self.srch, tmdb_api, quote(evntNm), self.language)
								if self.year:
									url_tmdb += "&year={}".format(self.year)
								poster = json.load(urlopen(url_tmdb))['results'][0]['poster_path']
								if poster:
									url_poster = "https://image.tmdb.org/t/p/w{}{}".format(self.sz, poster)
									with open(dwn_poster,'wb') as f:
										f.write(urlopen(url_poster).read())
								else:
									return
							else:
								return
						except:
							pass
		except:
			pass

	def filterSearch(self):
		try:
			# sd = self.event.getShortDescription() + "\n" + self.event.getExtendedDescription()
			sd = "%s\n%s\n%s" % (self.event.getEventName(), self.event.getShortDescription(), self.event.getExtendedDescription())
			w = [
				"serial", 
				"series", 
				"serie", 
				"serien", 
				"séries", 
				"serious", 
				"folge", 
				"episodio", 
				"episode", 
				"ep.", 
				"staffel", 
				"soap", 
				"doku", 
				"tv", 
				"talk", 
				"show", 
				"news", 
				"factual", 
				"entertainment", 
				"telenovela", 
				"dokumentation", 
				"dokutainment", 
				"documentary", 
				"informercial", 
				"information", 
				"sitcom", 
				"reality", 
				"program", 
				"magazine", 
				"mittagsmagazin", 
				"т/с", 
				"м/с", 
				"сезон", 
				"с-н", 
				"эпизод", 
				"сериал", 
				"серия"
				]

			for i in w:
				if i in sd.lower():
					self.srch = "tv"
					break
				else:
					self.srch = "multi"
			
			pattern = ["(19[0-9][0-9])", "(20[0-9][0-9])"]
			for i in pattern:
				yr = re.search(i, sd)
				if yr:
					jr = yr.group(1)
					return "{}".format(jr)
			return ""
		except:
			pass

	def epgs(self):
		events = None
		import NavigationInstance
		ref = NavigationInstance.instance.getCurrentlyPlayingServiceReference().toString()
		events = epgcache.lookupEvent(['IBDCT', (ref, 0, -1, -1)])
		for i in range(9):
			title = events[i][4]
			evntNm = REGEX.sub('', title).rstrip()
			evntNm = evntNm.replace("Die ", "The ").replace("Das ", "The ").replace("und ", "and ").replace("LOS ", "The ").rstrip()
			evntNm = evntNm.replace('\xc2\x86', '').replace('\xc2\x87', '')
			pstrNm = path_folder + evntNm + ".jpg"
			if not os.path.exists(pstrNm):
				try:
					url_tmdb = "https://api.themoviedb.org/3/search/multi?api_key={}&query={}&language={}".format(tmdb_api, quote(evntNm), self.language)
					poster = json.load(urlopen(url_tmdb))['results'][0]['poster_path']
					url_poster = "https://image.tmdb.org/t/p/w{}{}".format(self.sz, poster)
					dwn_poster = path_folder + "{}.jpg".format(evntNm)
					with open(dwn_poster,'wb') as f:
						f.write(urlopen(url_poster).read())
				except:
					pass
		return

	def delay2(self):
		self.timer = eTimer()
		self.timer.callback.append(self.dwn)
		self.timer.start(2000, True)
	
	def dwn(self):
		start_new_thread(self.epgs, ())
	