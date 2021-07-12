# -*- coding: utf-8 -*-
# by digiteng...06-07.2021
# file for skin FullHDLine by sunriser...
# for infobar,
# <widget source="session.Event_Now" render="Poster" position="0,125" size="185,278" nexts="2" language="en" zPosition="4" />
# for ch,
# <widget source="ServiceEvent" render="Poster" position="820,100" size="100,150" zPosition="4" />
# for secondInfobar,
# <widget source="session.Event_Now" render="Poster" position="20,155" size="100,150" zPosition="4" />
# <widget source="session.Event_Next" render="Poster" position="1080,155" size="100,150" zPosition="4" />

from Renderer import Renderer
from enigma import ePixmap, eTimer, loadJPG, eEPGCache, getBestPlayableServiceReference
# from Components.Pixmap import Pixmap
import json, re, os, socket, sys

tmdb_api = "3c3efcf47c3577558812bb9d64019d65"
epgcache = eEPGCache.getInstance()

PY3 = (sys.version_info[0] == 3)
if PY3:
	from urllib.parse import quote, urlencode
	from urllib.request import urlopen, Request
	from _thread import start_new_thread
else:
	from urllib2 import urlopen, quote
	from thread import start_new_thread

if os.path.isdir("/media/sda3"):
	path_folder = "/media/sda3/poster/"
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
		self.lngg = None
		self.sz = "185,278"
		self.src = None
		self.nxts = None
		self.intCheck()
		self.timer = eTimer()
		self.timer.callback.append(self.curPoster)
		
	def applySkin(self, desktop, parent):
		attribs = []
		for (attrib, value,) in self.skinAttributes:
			if attrib == "language":
				self.lngg = value
			if attrib == "nexts":
				self.nxts = int(value)
			if attrib == "size":
				self.sz = value.split(",")[0]
			if attrib.find("source"):
				self.src = value.split(".")[0]
			attribs.append((attrib, value))

		self.skinAttributes = attribs
		return Renderer.applySkin(self, desktop, parent)
		
	def intCheck(self):
		try:
			socket.setdefaulttimeout(1)
			socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
			return True
		except:
			# from Screens.MessageBox import MessageBox
			# from Tools import Notifications
			# Notifications.AddPopup("NO INTERNET CONNECTION !!!", MessageBox.TYPE_INFO, timeout=5)
			return

	GUI_WIDGET = ePixmap
	def changed(self, what):
		if not self.instance:
			return
		if what[0] == self.CHANGED_CLEAR:
			self.instance.hide()
		if what[0] != self.CHANGED_CLEAR:
			self.timer.start(100, True)
			
	def curPoster(self):
		self.instance.hide()
		self.event = self.source.event
		if self.event is None:
			self.instance.hide()
			return
		if self.event:
			evntNm = REGEX.sub('', self.event.getEventName()).strip()
			# evntNm = evntNm.replace("Die ", "The ").replace("Das ", "The ").replace("und ", "and ").replace("LOS ", "The ").rstrip()
			evntNm = evntNm.replace('\xc2\x86', '').replace('\xc2\x87', '')
			pstrNm = path_folder + evntNm + ".jpg"
			if os.path.exists(pstrNm):
				self.instance.setPixmap(loadJPG(pstrNm))
				self.instance.setScale(2)
				self.instance.show()
			else:
				if self.src == "100":
					self.instance.hide()
					return
				else:
					try:
						# self.instance.hide()
						self.year = self.filterSearch()
						url_tmdb = "https://api.themoviedb.org/3/search/{}?api_key={}&query={}".format(self.srch, tmdb_api, quote(evntNm))
						if self.year:
							url_tmdb += "&year={}".format(self.year)
						if self.lngg != "":
							url_tmdb += "&language={}".format(self.lngg)
							
						# open("/tmp/urls","a+").write("%s\n"%url_tmdb)
						poster = json.load(urlopen(url_tmdb))['results'][0]['poster_path']
						if poster:
							url_poster = "https://image.tmdb.org/t/p/w{}{}".format(self.sz, poster)
							dwn_poster = path_folder + "{}.jpg".format(evntNm)
							with open(dwn_poster,'wb') as f:
								f.write(urlopen(url_poster).read())
							# self.instance.show()
							self.delay2()
					except:
						return
		else:
			self.instance.hide()
			return



	def filterSearch(self):
		try:
			fd = "%s\n%s\n%s" % (self.event.getEventName(), self.event.getShortDescription(), self.event.getExtendedDescription())
			checkTV = [
				"serial", 
				"series", 
				"serie", 
				"serien", 
				"série", 
				"séries", 
				"serious", 
				"folge", 
				"episodio", 
				"episode", 
				"épisode", 
				"l'épisode", 
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

			checkMovie = ["film", "movie", "фильм", "кино", "ταινία", "película", "cinéma", "cine", "cinema", "filma"]
			for i in checkMovie:
				if i in fd.lower():
					self.srch = "movie"
					break
			for i in checkTV:
				if i in fd.lower():
					self.srch = "tv"
					break
				else:
					self.srch = "multi"

			if self.srch == "movie":
				pattern = re.findall('\d{4}', fd)
				return pattern[0]
			
		except:
			pass

	def epgs(self):
		if self.nxts != None or self.nxts != "0":
			events = None
			evntNm = ""
			import NavigationInstance
			ref = NavigationInstance.instance.getCurrentlyPlayingServiceReference().toString()
			events = epgcache.lookupEvent(['IBDCT', (ref, 0, -1, -1)])

			for i in range(self.nxts):
				title = events[i+1][4]
				evntNm = REGEX.sub('', title).rstrip()
				# evntNm = evntNm.replace("Die ", "The ").replace("Das ", "The ").replace("und ", "and ").replace("LOS ", "The ").rstrip()
				evntNm = evntNm.replace('\xc2\x86', '').replace('\xc2\x87', '')
				pstrNm = path_folder + evntNm + ".jpg"
				if not os.path.exists(pstrNm):
					try:
						url_tmdb = "https://api.themoviedb.org/3/search/multi?api_key={}&query={}".format(tmdb_api, quote(evntNm))
						if self.lngg != "":
							url_tmdb += "&language={}".format(self.lngg)
						poster = json.load(urlopen(url_tmdb))['results'][0]['poster_path']
						url_poster = "https://image.tmdb.org/t/p/w{}{}".format(self.sz, poster)
						dwn_poster = path_folder + "{}.jpg".format(evntNm)
						with open(dwn_poster,'wb') as f:
							f.write(urlopen(url_poster).read())
					except:
						pass
			return
			return
		else:
			return

	def delay2(self):
		self.timer2 = eTimer()
		self.timer2.callback.append(self.dwn)
		self.timer2.start(1000, True)
	
	def dwn(self):
		start_new_thread(self.epgs, ())
	