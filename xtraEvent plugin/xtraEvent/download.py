# -*- coding: utf-8 -*-
# by digiteng...06.2020, 11.2020, 11.2021
from __future__ import absolute_import
from Components.AVSwitch import AVSwitch
from Screens.Screen import Screen
from Components.Pixmap import Pixmap
from Components.Label import Label
from Components.ActionMap import ActionMap
from enigma import eEPGCache, eTimer, getDesktop, ePixmap, ePoint, eSize, loadJPG
from Components.config import config
from ServiceReference import ServiceReference
from Screens.MessageBox import MessageBox
import Tools.Notifications
import requests
from requests.utils import quote
import os
import re
import json

from PIL import Image
import socket
from . import xtra
from datetime import datetime
import time
import threading
from Components.ProgressBar import ProgressBar
import io
from enigma import addFont
from Plugins.Extensions.xtraEvent.skins.xtraSkins import *

addFont("/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/fonts/arial.ttf", "Regular", 100, 1)
addFont("/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/fonts/xtra.ttf", "di", 100, 1)

if config.plugins.xtraEvent.tmdbAPI.value != "":
	tmdb_api = config.plugins.xtraEvent.tmdbAPI.value
else:
	tmdb_api = "3c3efcf47c3577558812bb9d64019d65"
if config.plugins.xtraEvent.tvdbAPI.value != "":
	tvdb_api = config.plugins.xtraEvent.tvdbAPI.value
else:
	tvdb_api = "a99d487bb3426e5f3a60dea6d3d3c7ef"
if config.plugins.xtraEvent.fanartAPI.value != "":
	fanart_api = config.plugins.xtraEvent.fanartAPI.value
else:
	fanart_api = "6d231536dea4318a88cb2520ce89473b"


try:
	import sys
	if sys.version_info[0] == 3:
		from builtins import str
		from builtins import range
		from configparser import ConfigParser
		from _thread import start_new_thread
	else:
		from ConfigParser import ConfigParser
		from thread import start_new_thread
except:
	pass
try:
	lang = config.osd.language.value[:-3]
except:
	pass
lng = ConfigParser()
lng.read('/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/languages')
# lng = lng.get(lang, '5')	
epgcache = eEPGCache.getInstance()
pathLoc = config.plugins.xtraEvent.loc.value + "xtraEvent/"
desktop_size = getDesktop(0).size().width()
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
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

class downloads(Screen):
	def __init__(self, session):
		Screen.__init__(self, session)
		self.session = session
		if desktop_size <= 1280:
			if config.plugins.xtraEvent.skinSelect.value == 'skin_1':
				self.skin = download_720
			if config.plugins.xtraEvent.skinSelect.value == 'skin_2':
				self.skin = download_720_2
		else:
			if config.plugins.xtraEvent.skinSelect.value == 'skin_1':
				self.skin = download_1080
			if config.plugins.xtraEvent.skinSelect.value == 'skin_2':
				self.skin = download_1080_2
		self.titles = ""
		self['status'] = Label()
		self['info'] = Label()
		self['info2'] = Label()
		self['Picture'] = Pixmap()
		self['Picture2'] = Pixmap()
		self['int_statu'] = Label()
		self['key_red'] = Label(_('Back'))
		self['key_green'] = Label(_('Download'))
		# self['key_yellow'] = Label(_('Show'))
		self['key_blue'] = Label(_(lng.get(lang, '66')))
		self['actions'] = ActionMap(['xtraEventAction'], 
		{
		'cancel': self.close, 
		'red': self.close, 
		'ok':self.save,
		'green':self.save,
		# 'yellow':self.ir,
		'blue':self.showhide
		}, -2)
		self['progress'] = ProgressBar()
		self['progress'].setRange((0, 100))
		self['progress'].setValue(0)
		self.setTitle(_(" Downloads"))
		self.screen_hide = False
		self.onLayoutFinish.append(self.showFilm)

	def showhide(self):
		if self.screen_hide:
			Screen.show(self)
		else:
			Screen.hide(self)
		self.screen_hide = not (self.screen_hide)

	def save(self):
		if config.plugins.xtraEvent.searchMOD.value == lng.get(lang, '14'):
			self.currentChEpgs()
		if config.plugins.xtraEvent.searchMOD.value == lng.get(lang, '13'):
			self.selBouquets()

	def currentChEpgs(self):
		events = None
		import NavigationInstance
		ref = NavigationInstance.instance.getCurrentlyPlayingServiceReference().toString()
		events = epgcache.lookupEvent(['IBDCTSERNX', (ref, 1, -1, -1)])
		if events:
			try:
				n = config.plugins.xtraEvent.searchNUMBER.value
				titles = []
				for i in range(int(n)):
					try:
						title = events[i][4]
						title = REGEX.sub('', title).strip()
						titles.append(title)
					except:
						continue
					if i == n:
						break
				self.titles = list(dict.fromkeys(titles))
				start_new_thread(self.downloadEvents, ())
			except Exception as err:
				with open("/tmp/xtra_error.log", "a+") as f:
					f.write("currentChEpgs, %s\n"%(err))

	def selBouquets(self):
		if os.path.exists(pathLoc + "bqts"):
			with open(pathLoc + "bqts", "r") as f:
				refs = f.readlines()
			nl = len(refs)
			eventlist=[]
			for i in range(nl):
				ref = refs[i]
				try:
					events = epgcache.lookupEvent(['IBDCTSERNX', (ref, 1, -1, -1)])
					n = config.plugins.xtraEvent.searchNUMBER.value
					for i in range(int(n)):
						title = events[i][4]
						title = REGEX.sub('', title).strip()
						eventlist.append(title)
				except:
					pass
			self.titles = list(dict.fromkeys(eventlist))
			start_new_thread(self.downloadEvents, ())

	def intCheck(self):
		try:
			socket.setdefaulttimeout(2)
			socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
			self['int_statu'].setText("")
			return True
		except:
			return False
####################################################
	def downloadEvents(self):
		dwnldFile=""
		self.title = ""
		self['progress'].setValue(0)
		lang = None
		now = datetime.now()
		st = now.strftime("%d/%m/%Y %H:%M:%S ")
		tmdb_poster_downloaded = 0
		tvdb_poster_downloaded = 0
		maze_poster_downloaded = 0
		fanart_poster_downloaded = 0
		tmdb_backdrop_downloaded = 0
		tvdb_backdrop_downloaded = 0
		fanart_backdrop_downloaded = 0
		banner_downloaded = 0
		extra_downloaded = 0
		extra2_downloaded = 0
		extra3_poster_downloaded = 0
		extra3_info_downloaded = 0
		info_downloaded = 0
		title_search = 0
		title = ""
		if config.plugins.xtraEvent.onoff.value:
# elcinema(en) #################################################################
			if config.plugins.xtraEvent.extra3.value == True:
				Type = ""
				Genre = ""
				Language = ""
				Country = ""
				imdbRating = ""
				Rated = ""
				Duration = ""
				Year = ""
				Director = ""
				Writer = ""
				Actors = ""
				Plot = ""
				setime = ""
				try:
					if not os.path.exists("/tmp/urlo.html"):
						url = "https://elcinema.com/en/tvguide/"
						urlo = requests.get(url)
						urlo = urlo.text.replace('&#39;', "'").replace('&quot;', '"').replace('&amp;', 'and').replace('(', '').replace(')', '')
						with io.open("/tmp/urlo.html", "w", encoding="utf-8") as f:
							f.write(urlo)
					if os.path.exists("/tmp/urlo.html"):
						with io.open("/tmp/urlo.html", "r", encoding="utf-8") as f:
							urlor = f.read()
						titles = re.findall('<li><a title="(.*?)" href="/en/work', urlor)
					n = len(titles)
				except Exception as err:
					with open("/tmp/xtra_error.log", "a+") as f:
						f.write("elcinema urlo, %s, %s\n"%(title, err))
				for title in titles:
					try:
						title = REGEX.sub('', title).strip()
						dwnldFile = pathLoc + "poster/{}.jpg".format(title)
						info_files = pathLoc + "infos/{}.json".format(title)
						tid = re.findall('title="%s" href="/en/work/(.*?)/"'%title, urlor)[0]
						self.setTitle(_("{}".format(title)))
						if not os.path.exists(dwnldFile):
							turl =	"https://elcinema.com/en/work/{}/".format(tid)
							jurlo = requests.get(turl.strip(), stream=True, allow_redirects=True, headers=headers)
							jurlo = jurlo.text.replace('&#39;', "'").replace('&quot;', '"').replace('&amp;', 'and').replace('(', '').replace(')', '')
							# poster elcinema
							img = re.findall('<img src="(.*?).jpg" alt=""', jurlo)[0]
							open(dwnldFile, "wb").write(requests.get(img + ".jpg", stream=True, allow_redirects=True).content)
							self['info'].setText(" {}, EXTRA3, POSTER".format("  " + title.upper()))
							extra3_poster_downloaded += 1
							downloaded = extra3_poster_downloaded
							self.prgrs(downloaded, n)
							self.showPoster(dwnldFile)
					except Exception as err:
						with open("/tmp/xtra_error.log", "a+") as f:
							f.write("elcinema poster, %s, %s\n"%(title, err))
					#info elcinema,
					if not os.path.exists(info_files):
						turl =	"https://elcinema.com/en/work/{}/".format(tid)
						jurlo = requests.get(turl.strip(), stream=True, allow_redirects=True, headers=headers)
						jurlo = jurlo.text.replace('&#39;', "'").replace('&quot;', '"').replace('&amp;', 'and').replace('(', '').replace(')', '')
						try:
							setime = urlor.partition('title="%s"'%title)[2].partition('</ul>')[0].strip()
							setime = re.findall("(\d\d\:\d\d) (.*?) - (\d\d\:\d\d) (.*?)</li>", setime)
							setime = setime[0][0]+setime[0][1]+" - "+setime[0][2]+setime[0][3]
						except:
							pass
						try:
							Category = jurlo.partition('<li>Category:</li>')[2].partition('</ul>')[0].strip()
							Category = Category.partition('<li>')[2].partition('</li>')[0].strip()
						except:
							pass
						try:
							glist=[]
							Genre = (jurlo.partition('<li>Genre:</li>')[2].partition('</ul>')[0]).strip().split("</a> </li>")
							for i in range(len(Genre)-1):
								Genre = (jurlo.partition('<li>Genre:</li>')[2].partition('</ul>')[0]).strip().split("</a> </li>")[i]
								Genre = Genre.partition('">')[2].strip()
								glist.append(Genre)
						except:
							pass
						try:
							llist=[]
							Language = (jurlo.partition('<li>Language:</li>')[2].partition('</ul>')[0]).strip().split("</a> </li>")
							for i in range(len(Language)-1):
								Language = (jurlo.partition('<li>Language:</li>')[2].partition('</ul>')[0]).strip().split("</a> </li>")[i]
								Language = Language.partition('">')[2].strip()
								llist.append(Language)
						except:
							pass
						try:
							clist=[]
							Country = (jurlo.partition('<li>Country:</li>')[2].partition('</ul>')[0]).strip().split("</a> </li>")
							for i in range(len(Country)-1):
								Country = (jurlo.partition('<li>Country:</li>')[2].partition('</ul>')[0]).strip().split("</a> </li>")[i]
								Country = Country.partition('">')[2].strip()
								clist.append(Country)
						except:
							pass
						try:
							Rating = re.findall("class='fa fa-star'></i> (.*?) </span><div", jurlo)[0]
							Rated = jurlo.partition('<li>MPAA</li><li>')[2].partition('</li></ul></li>')[0].strip()
							if Rated =="":
								Rated = jurlo.partition('class="censorship purple" title="Censorship:')[2].partition('"><li>')[0].strip()
						except:
							pass					
						try:	
							Year = jurlo.partition('href="/en/index/work/release_year/')[2].partition('/"')[0].strip()
						except:
							pass
						try:
							Duration = re.findall("<li>(.*?) minutes</li>", jurlo)[0]
						except:
							pass
						try:
							dlist=[]
							Director = (jurlo.partition('<li>Director:</li>')[2].partition('</ul>')[0]).strip().split('</a>')
							for i in range(len(Director)-1):
								Director = (jurlo.partition('<li>Director:</li>')[2].partition('</ul>')[0]).strip().split('</a>')[i]
								Director = Director.partition('/">')[2].strip()
								dlist.append(Director)
						except:
							pass
						try:
							wlist=[]
							Writer = (jurlo.partition('<li>Writer:</li>')[2].partition('</ul>')[0]).strip().split('</a>')
							for i in range(len(Writer)-1):
								Writer = (jurlo.partition('<li>Writer:</li>')[2].partition('</ul>')[0]).strip().split('</a>')[i]
								Writer = Writer.partition('/">')[2].strip()
								wlist.append(Writer)
						except:
							pass
						try:
							calist=[]
							Cast = (jurlo.partition('<li>Cast:</li>')[2].partition('</ul>')[0]).strip().split("</a> </li>")
							for i in range(len(Cast)-1):
								Cast = (jurlo.partition('<li>Cast:</li>')[2].partition('</ul>')[0]).strip().split("</a> </li>")[i]
								Cast = Cast.partition('">')[2].strip()
								calist.append(Cast)
						except:
							pass
						try:
							Description1 = re.findall("<p>(.*?)<a href='#' id='read-more'>...Read more</a><span class='hide'>", jurlo)[0]
							Description2 = re.findall("<a href='#' id='read-more'>...Read more</a><span class='hide'>(.*?)\.", jurlo)[0]
							Description = Description1+Description2
						except:
							try:
								Description = re.findall("<p>(.*?)</p>", jurlo)[0]
							except:
								pass
						try:
							ej = {
							"Title": "%s"%title, 
							"Start-End Time": "%s"%setime,
							"Type": "%s"%Category,
							"Year": "%s"%Year,
							"imdbRating": "%s"%Rating, 
							"Rated": "%s"%Rated,
							"Genre": "%s"%(', '.join(glist)), 
							"Duration": "%s min."%Duration,
							"Language": "%s"%(', '.join(llist)),
							"Country": "%s"%(', '.join(clist)),
							"Director": "%s"%(', '.join(dlist)),
							"Writer": "%s"%(', '.join(wlist)),
							"Actors": "%s"%(', '.join(calist)),
							"Plot": "%s"%Description,
							}
							open(info_files, "w").write(json.dumps(ej))
							if os.path.exists(info_files):
								extra3_info_downloaded += 1
								downloaded = extra3_info_downloaded
								self.prgrs(downloaded, n)
								self['info'].setText(" {}, EXTRA3, INFO".format("  " + title.upper()))
						except Exception as err:
							with open("/tmp/xtra_error.log", "a+") as f:
								f.write("elcinema ej, %s, %s\n"%(title, err))
			n = len(self.titles)
			for i in range(n):
				title = self.titles[i]
				title = title.strip()
				self.setTitle(_("{}".format(title)))
	# tmdb_Poster() #################################################################
				if config.plugins.xtraEvent.poster.value == True:
					dwnldFile = pathLoc + "poster/{}.jpg".format(title)
					if config.plugins.xtraEvent.tmdb.value == True:
						if not os.path.exists(dwnldFile):
							try:
								srch = "multi"
								lang = config.plugins.xtraEvent.searchLang.value
								url_tmdb = "https://api.themoviedb.org/3/search/{}?api_key={}&query={}".format(srch, tmdb_api, quote(title))
								if lang != None:
									url_tmdb += "&language={}".format(lang)
								poster = ""
								poster = requests.get(url_tmdb).json()['results'][0]['poster_path']
								p_size = config.plugins.xtraEvent.TMDBpostersize.value
								url = "https://image.tmdb.org/t/p/{}{}".format(p_size, poster)
								if poster != "":
									open(dwnldFile, 'wb').write(requests.get(url, stream=True, allow_redirects=True).content)
								if os.path.exists(dwnldFile):
									self['info'].setText("  " + title.upper() + ", TMDB, POSTER")
									tmdb_poster_downloaded += 1
									downloaded = tmdb_poster_downloaded
									self.prgrs(downloaded, n)
									self.showPoster(dwnldFile)
									#continue
									try:
										img = Image.open(dwnldFile)
										img.verify()
									except Exception as err:
										with open("/tmp/xtra_error.log", "a+") as f:
											f.write("deleted tmdb poster: %s.jpg\n"%title)
										try:
											os.remove(dwnldFile)
										except:
											pass
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("tmdb poster, %s, %s\n"%(title, err))
		# tvdb_Poster() #################################################################
					if config.plugins.xtraEvent.tvdb.value == True:
						try:
							img = Image.open(dwnldFile)
							img.verify()
						except Exception as err:
							with open("/tmp/xtra_error.log", "a+") as f:
								f.write("deleted : %s.jpg\n"%title)
							try:
								os.remove(dwnldFile)
							except:
								pass
						if not os.path.exists(dwnldFile):
							try:
								url_tvdb = "https://thetvdb.com/api/GetSeries.php?seriesname={}".format(quote(title))
								url_read = requests.get(url_tvdb).text
								series_id = re.findall('<seriesid>(.*?)</seriesid>', url_read)[0]
								if series_id:
									url_tvdb = "https://thetvdb.com/api/{}/series/{}/en".format(tvdb_api, series_id)
									url_read = requests.get(url_tvdb).text
									poster = ""
									poster = re.findall('<poster>(.*?)</poster>', url_read)[0]
									if poster != '':
										url = "https://artworks.thetvdb.com/banners/{}".format(poster)
										if config.plugins.xtraEvent.TVDBpostersize.value == "thumbnail":
											url = url.replace(".jpg", "_t.jpg")
										open(dwnldFile, 'wb').write(requests.get(url, stream=True, allow_redirects=True).content)
										if os.path.exists(dwnldFile):
											self['info'].setText("  " + title.upper()+", TVDB, POSTER")
											tvdb_poster_downloaded += 1
											downloaded = tvdb_poster_downloaded
											self.prgrs(downloaded, n)
											self.showPoster(dwnldFile)
											#continue
											try:
												img = Image.open(dwnldFile)
												img.verify()
											except Exception as err:
												with open("/tmp/xtra_error.log", "a+") as f:
													f.write("deleted tvdb poster: %s.jpg\n"%title)
												try:
													os.remove(dwnldFile)
												except:
													pass
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("tvdb poster, %s, %s\n"%(title, err))
		# maze_Poster() #################################################################								
					if config.plugins.xtraEvent.maze.value == True:
						try:
							img = Image.open(dwnldFile)
							img.verify()
						except Exception as err:
							with open("/tmp/xtra_error.log", "a+") as f:
								f.write("deleted : %s.jpg\n"%title)
							try:
								os.remove(dwnldFile)
							except:
								pass
						if not os.path.exists(dwnldFile):
							url_maze = "http://api.tvmaze.com/search/shows?q={}".format(quote(title))
							try:
								url = requests.get(url_maze).json()[0]['show']['image']['medium']
								open(dwnldFile, 'wb').write(requests.get(url, stream=True, allow_redirects=True).content)
								if os.path.exists(dwnldFile):
									self['info'].setText("  " + title.upper()+", MAZE, POSTER")
									maze_poster_downloaded += 1
									downloaded = maze_poster_downloaded
									self.prgrs(downloaded, n)
									self.showPoster(dwnldFile)
									try:
										img = Image.open(dwnldFile)
										img.verify()
									except Exception as err:
										with open("/tmp/xtra_error.log", "a+") as f:
											f.write("deleted maze poster: %s.jpg\n"%title)
										try:
											os.remove(dwnldFile)
										except:
											pass	
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("maze poster, %s, %s\n"%(title, err))
		# fanart_Poster() #################################################################								
					if config.plugins.xtraEvent.fanart.value == True:
						try:
							img = Image.open(dwnldFile)
							img.verify()
						except Exception as err:
							with open("/tmp/xtra_error.log", "a+") as f:
								f.write("deleted : %s.jpg\n"%title)
							try:
								os.remove(dwnldFile)
							except:
								pass
						if not os.path.exists(dwnldFile):
							try:
								url = None
								srch = "multi"
								url_tmdb = "https://api.themoviedb.org/3/search/{}?api_key={}&query={}".format(srch, tmdb_api, quote(title))
								bnnr = requests.get(url_tmdb, verify=False).json()
								tmdb_id = (bnnr['results'][0]['id'])
								if tmdb_id:
									m_type = (bnnr['results'][0]['media_type'])
									if m_type == "movie":
										m_type = (bnnr['results'][0]['media_type']) + "s"
									else:
										mm_type = m_type
									url_maze = "http://api.tvmaze.com/singlesearch/shows?q={}".format(quote(title))
									mj = requests.get(url_maze, verify=False).json()
									tvdb_id = (mj['externals']['thetvdb'])
									if tvdb_id:
										url_fanart = "https://webservice.fanart.tv/v3/{}/{}?api_key={}".format(m_type, tvdb_id, fanart_api)
										fjs = requests.get(url_fanart, verify=False).json()
										if fjs:
											if m_type == "movies":
												mm_type = (bnnr['results'][0]['media_type'])
											else:
												mm_type = m_type
											if mm_type == "tv":
												url = fjs['tvposter'][0]['url']
											elif mm_type == "movies":
												url = fjs['movieposter'][0]['url']
											if url:
												open(dwnldFile, 'wb').write(requests.get(url, stream=True, allow_redirects=True, verify=False).content)
											if os.path.exists(dwnldFile):
												self['info'].setText("  " + title.upper()+", FANART, POSTER")
												fanart_poster_downloaded += 1
												downloaded = fanart_poster_downloaded
												self.prgrs(downloaded, n)
												self.showPoster(dwnldFile)
												try:
													img = Image.open(dwnldFile)
													img.verify()
												except Exception as err:
													with open("/tmp/xtra_error.log", "a+") as f:
														f.write("deleted fanart poster: %s.jpg\n"%title)
													try:
														os.remove(dwnldFile)
													except:
														pass
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("fanart poster, %s, %s\n"%(title, err))
	# backdrop() #################################################################
				if config.plugins.xtraEvent.backdrop.value == True:
					dwnldFile = "{}backdrop/{}.jpg".format(pathLoc, title)
					if config.plugins.xtraEvent.extra.value == True:
						if not os.path.exists(dwnldFile):
							try:
								url = "http://capi.tvmovie.de/v1/broadcasts/search?q={}&page=1&rows=1".format(title.replace(" ", "+"))
								try:
									url = requests.get(url).json()['results'][0]['images'][0]['filepath']['android-image-320-180']
								except:
									pass
								open(dwnldFile, 'wb').write(requests.get(url, stream=True, allow_redirects=True).content)
								if os.path.exists(dwnldFile):
									self['info'].setText("  " + title.upper()+", EXTRA, BACKDROP")
									extra_downloaded += 1
									downloaded = extra_downloaded
									self.prgrs(downloaded, n)
									self.showBackdrop(dwnldFile)
									try:
										img = Image.open(dwnldFile)
										img.verify()
									except Exception as err:
										with open("/tmp/xtra_error.log", "a+") as f:
											f.write("deleted extra poster: %s.jpg\n"%title)
										try:
											os.remove(dwnldFile)
										except:
											pass
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("extra, %s, %s\n"%(title, err))
					if config.plugins.xtraEvent.tmdb.value == True:
						try:
							img = Image.open(dwnldFile)
							img.verify()
						except Exception as err:
							with open("/tmp/xtra_error.log", "a+") as f:
								f.write("deleted : %s.jpg\n"%title)
							try:
								os.remove(dwnldFile)
							except:
								pass
						if not os.path.exists(dwnldFile):	
							srch = "multi"
							lang = config.plugins.xtraEvent.searchLang.value
							url_tmdb = "https://api.themoviedb.org/3/search/{}?api_key={}&query={}".format(srch, tmdb_api, quote(title))
							if lang != None:
								url_tmdb += "&language={}".format(lang)
							try:
								backdrop = requests.get(url_tmdb).json()['results'][0]['backdrop_path']
								if backdrop:
									backdrop_size = config.plugins.xtraEvent.TMDBbackdropsize.value
									# backdrop_size = "w300"
									url = "https://image.tmdb.org/t/p/{}{}".format(backdrop_size, backdrop)
									open(dwnldFile, 'wb').write(requests.get(url, stream=True, allow_redirects=True).content)
									if os.path.exists(dwnldFile):
										self['info'].setText("  " + title.upper()+", TMDB, BACKDROP")
										tmdb_backdrop_downloaded += 1
										downloaded = tmdb_backdrop_downloaded
										self.prgrs(downloaded, n)
										self.showBackdrop(dwnldFile)
										try:
											img = Image.open(dwnldFile)
											img.verify()
										except Exception as err:
											with open("/tmp/xtra_error.log", "a+") as f:
												f.write("deleted tmdb backdrop: %s.jpg\n"%title)
											try:
												os.remove(dwnldFile)
											except:
												pass
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("tmdb-backdrop, %s, %s\n"%(title, err))
					if config.plugins.xtraEvent.tvdb.value == True:
						try:
							img = Image.open(dwnldFile)
							img.verify()
						except Exception as err:
							with open("/tmp/xtra_error.log", "a+") as f:
								f.write("deleted : %s.jpg\n"%title)
							try:
								os.remove(dwnldFile)
							except:
								pass
						if not os.path.exists(dwnldFile):
							try:
								url_tvdb = "https://thetvdb.com/api/GetSeries.php?seriesname={}".format(quote(title))
								url_read = requests.get(url_tvdb).text
								series_id = re.findall('<seriesid>(.*?)</seriesid>', url_read)[0]
								if series_id:
									lang = config.plugins.xtraEvent.searchLang.value
									# lang ="en"
									url_tvdb = "https://thetvdb.com/api/{}/series/{}/{}.xml".format(tvdb_api, series_id, lang)
									url_read = requests.get(url_tvdb).text
									backdrop = re.findall('<fanart>(.*?)</fanart>', url_read)[0]
									if backdrop:
										url = "https://artworks.thetvdb.com/banners/{}".format(backdrop)
										if config.plugins.xtraEvent.TVDBbackdropsize.value == "thumbnail":
											url = url.replace(".jpg", "_t.jpg")
										open(dwnldFile, 'wb').write(requests.get(url, stream=True, allow_redirects=True).content)
										if os.path.exists(dwnldFile):
											self['info'].setText("  " + title.upper()+", TVDB, BACKDROP")
											tvdb_backdrop_downloaded += 1
											downloaded = tvdb_backdrop_downloaded
											self.prgrs(downloaded, n)
											self.showBackdrop(dwnldFile)
											try:
												img = Image.open(dwnldFile)
												img.verify()
											except Exception as err:
												with open("/tmp/xtra_error.log", "a+") as f:
													f.write("deleted tvdb backdrop: %s.jpg\n"%title)
												try:
													os.remove(dwnldFile)
												except:
													pass
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("tvdb-backdrop, %s, %s\n"%(title, err))
					if config.plugins.xtraEvent.extra2.value == True:
						try:
							img = Image.open(dwnldFile)
							img.verify()
						except Exception as err:
							with open("/tmp/xtra_error.log", "a+") as f:
								f.write("deleted : %s.jpg\n"%title)
							try:
								os.remove(dwnldFile)
							except:
								pass
						if not os.path.exists(dwnldFile):
							try:
								url = "https://www.bing.com/images/search?q={}".format(title.replace(" ", "+"))
								if config.plugins.xtraEvent.PB.value == "posters":
									url += "+poster"
								else:
									url += "+backdrop"
								ff = requests.get(url, stream=True, headers=headers).text
								p = ',&quot;murl&quot;:&quot;(.*?)&'
								url = re.findall(p, ff)[0]
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("bing-backdrop, %s, %s\n"%(title, err))
								try:
									url = "https://www.google.com/search?q={}&tbm=isch&tbs=sbd:0".format(title.replace(" ", "+"))
									if config.plugins.xtraEvent.PB.value == "posters":
										url += "+poster"
									else:
										url += "+backdrop"
									ff = requests.get(url, stream=True, headers=headers).text
									p = re.findall('\],\["https://(.*?)",\d+,\d+]', ff)[0]
									url = "https://" + p
								except Exception as err:
									with open("/tmp/xtra_error.log", "a+") as f:
										f.write("google-backdrop, %s, %s\n"%(title, err))
							try:
								open(dwnldFile, 'wb').write(requests.get(url, stream=True, allow_redirects=True).content)
								if os.path.exists(dwnldFile):
									self['info'].setText("  " + title.upper()+", EXTRA2, BACKDROP")
									extra2_downloaded += 1
									downloaded = extra2_downloaded
									self.prgrs(downloaded, n)
									self.showBackdrop(dwnldFile)
									try:
										img = Image.open(dwnldFile)
										img.verify()
									except Exception as err:
										with open("/tmp/xtra_error.log", "a+") as f:
											f.write("deleted extra2 backdrop: %s.jpg\n"%title)
										try:
											os.remove(dwnldFile)
										except:
											pass
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("extra2 backdrop, %s, %s\n"%(title, err))							
	# banner() #################################################################	
				if config.plugins.xtraEvent.banner.value == True:
					dwnldFile = pathLoc + "banner/{}.jpg".format(title)				
					try:
						img = Image.open(dwnldFile)
						img.verify()
					except Exception as err:
						with open("/tmp/xtra_error.log", "a+") as f:
							f.write("deleted : %s.jpg\n"%title)
						try:
							os.remove(dwnldFile)
						except:
							pass
					if config.plugins.xtraEvent.tvdb.value == True:
						if not os.path.exists(dwnldFile):
							try:
								banner_img = ""
								url = "https://thetvdb.com/api/GetSeries.php?seriesname={}".format(quote(title))
								url = requests.get(url).text
								banner_img = re.findall('<banner>(.*?)</banner>', url, re.I)[0]
								if banner_img:
									url = "https://artworks.thetvdb.com{}".format(banner_img)
									if url:
										open(dwnldFile, 'wb').write(requests.get(url, stream=True, allow_redirects=True).content)
										if os.path.exists(dwnldFile):
											self['info'].setText("  " + title.upper()+", TVDB, BANNER")
											banner_downloaded += 1
											downloaded = banner_downloaded
											self.prgrs(downloaded, n)
											self.showBanner(dwnldFile)
											try:
												img = Image.open(dwnldFile)
												img.verify()
											except Exception as err:
												with open("/tmp/xtra_error.log", "a+") as f:
													f.write("deleted extra2 backdrop: %s.jpg\n"%title)
												try:
													os.remove(dwnldFile)
												except:
													pass
											scl = 1
											im = Image.open(dwnldFile)
											scl = config.plugins.xtraEvent.TVDB_Banner_Size.value
											im1 = im.resize((im.size[0] // int(scl), im.size[1] // int(scl)), Image.ANTIALIAS)
											im1.save(dwnldFile)
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("tvdb banner, %s, %s\n"%(title, err))			
					if config.plugins.xtraEvent.fanart.value == True:
						try:
							img = Image.open(dwnldFile)
							img.verify()
						except Exception as err:
							with open("/tmp/xtra_error.log", "a+") as f:
								f.write("deleted : %s.jpg\n"%title)
							try:
								os.remove(dwnldFile)
							except:
								pass
						if not os.path.exists(dwnldFile):
							try:
								url = "https://api.themoviedb.org/3/search/multi?api_key={}&query={}".format(tmdb_api, quote(title))
								jp = requests.get(url, verify=False).json()
								tmdb_id = (jp['results'][0]['id'])
								print(tmdb_id)
								if tmdb_id:
									m_type = (jp['results'][0]['media_type'])
									if m_type == "movie":
										m_type = (jp['results'][0]['media_type']) + "s"
									else:
										mm_type = m_type
								if m_type == "movies":
									url = "https://webservice.fanart.tv/v3/{}/{}?api_key={}".format(m_type, tmdb_id, fanart_api)
									fjs = requests.get(url, verify=False, timeout=5).json()
									url = fjs["moviebanner"][0]["url"]
									if url:
										open(dwnldFile, 'wb').write(requests.get(url, stream=True, allow_redirects=True, verify=False, timeout=5).content)
										if os.path.exists(dwnldFile):
											self['info'].setText("  " + title.upper()+", FANART, BANNER")
											banner_downloaded += 1
											downloaded = banner_downloaded
											self.prgrs(downloaded, n)
											self.showBanner(dwnldFile)
											try:
												img = Image.open(dwnldFile)
												img.verify()
											except Exception as err:
												with open("/tmp/xtra_error.log", "a+") as f:
													f.write("deleted fanart banner: %s.jpg\n"%title)
												try:
													os.remove(dwnldFile)
												except:
													pass
											scl = 1
											im = Image.open(dwnldFile)
											scl = config.plugins.xtraEvent.FANART_Banner_Size.value
											im1 = im.resize((im.size[0] // int(scl), im.size[1] // int(scl)), Image.ANTIALIAS)
											im1.save(dwnldFile)
								else:
									try:
										url_maze = "http://api.tvmaze.com/singlesearch/shows?q={}".format(quote(title))
										mj = requests.get(url_maze, verify=False).json()
										tvdb_id = mj['externals']['thetvdb']
									except Exception as err:
										with open("/tmp/xtra_error.log", "a+") as f:
											f.write("fanart maze banner2, %s, %s\n"%(title, err))
									try:
										if tvdb_id:
											url = "https://webservice.fanart.tv/v3/tv/{}?api_key={}".format(tvdb_id, fanart_api)
											fjs = requests.get(url, verify=False, timeout=5).json()
											url = fjs["tvbanner"][0]["url"]
									except Exception as err:
										with open("/tmp/xtra_error.log", "a+") as f:
											f.write("fanart banner3, %s, %s\n"%(title, err))
									try:
										if url:
											open(dwnldFile, 'wb').write(requests.get(url, stream=True, allow_redirects=True, verify=False).content)
											if os.path.exists(dwnldFile):
												self['info'].setText("  " + title.upper()+", FANART, BANNER")
												banner_downloaded += 1
												downloaded = banner_downloaded
												self.prgrs(downloaded, n)
												self.showBanner(dwnldFile)
												try:
													img = Image.open(dwnldFile)
													img.verify()
												except Exception as err:
													with open("/tmp/xtra_error.log", "a+") as f:
														f.write("deleted fanart banner: %s.jpg\n"%title)
													try:
														os.remove(dwnldFile)
													except:
														pass
												scl = 1
												im = Image.open(dwnldFile)
												scl = config.plugins.xtraEvent.FANART_Banner_Size.value
												im1 = im.resize((im.size[0] // int(scl), im.size[1] // int(scl)), Image.ANTIALIAS)
												im1.save(dwnldFile)
									except Exception as err:
										with open("/tmp/xtra_error.log", "a+") as f:
											f.write("fanart banner4 end, %s, %s\n"%(title, err))
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("fanart maze banner1, %s, %s\n"%(title, err))
	# infos #################################################################
				if config.plugins.xtraEvent.info.value == True:
					dwnldFile = pathLoc + "infos/{}.json".format(title)
					if config.plugins.xtraEvent.infoOmdb.value:
						if not os.path.exists(dwnldFile):
							imdb_id = None
							try:
								url = 'https://m.imdb.com/find?q={}'.format(title)
								ff = requests.get(url).text
								try:
									rc = re.compile('<a href="/title/(.*?)/"', re.DOTALL)
									imdb_id = rc.search(ff).group(1)
								except:
									pass
								try:
									if not os.path.exists("/tmp/imdb.html"):
										url= "https://m.imdb.com/title/{}/?ref_=fn_al_tt_0".format(imdb_id)
										ff = requests.get(url).text
										with io.open("/tmp/imdb.html", "w", encoding="utf-8") as f:
											f.write(ff)
									if os.path.exists("/tmp/imdb.html"):
										with io.open("/tmp/imdb.html", "r", encoding="utf-8") as f:
											ff = f.read()
								except Exception as err:
									with open("/tmp/xtra_error.log", "a+") as f:
										f.write("info Omdb imdb-html, %s, %s\n"%(title, err))
								if config.plugins.xtraEvent.omdbAPI.value:
									omdb_api = config.plugins.xtraEvent.omdbAPI.value
								else:
									omdb_apis = ["6a4c9432", "a8834925", "550a7c40", "8ec53e6b"]
									try:
										for omdb_api in omdb_apis:
											if not os.path.exists(dwnldFile):
												if imdb_id != None:
													url = "http://www.omdbapi.com/?apikey={}&i={}".format(omdb_api, imdb_id)
												else:
													url = "http://www.omdbapi.com/?apikey={}&t={}".format(omdb_api, title)
												with open("/tmp/info1", "a+") as f:
													f.write("info, %s, %s\n"%(title, url))
												if not os.path.exists(dwnldFile):
													info_omdb = requests.get(url)
													if info_omdb.status_code == 200:
														open(dwnldFile, "w").write(json.dumps(info_omdb.json()))
														try:
															with open(dwnldFile) as f:
																rj = json.load(f)
															if rj["Response"] == "False" or rj["Genre"] == "":
																os.remove(dwnldFile)
														except:
															pass
													else:
														continue
													break
									except Exception as err:
										with open("/tmp/xtra_error.log", "a+") as f:
											f.write("info-apis, %s, %s\n"%(title, err))
										continue	
								if not os.path.exists(dwnldFile):
									if imdb_id != None:
										url = "http://www.omdbapi.com/?apikey={}&i={}".format(omdb_api, imdb_id)
									else:
										url = "http://www.omdbapi.com/?apikey={}&t={}".format(omdb_api, title)
									info_omdb = requests.get(url)
									if info_omdb.status_code == 200:
										open(dwnldFile, "w").write(json.dumps(info_omdb.json()))
										if os.path.exists("/tmp/imdb.html"):
											os.remove("/tmp/imdb.html")
										try:
											with open(dwnldFile) as f:
												rj = json.load(f)
											if rj["Response"] == "False":
												os.remove(dwnldFile)
										except:
											pass
								if os.path.exists(dwnldFile):
									info_downloaded += 1
									downloaded = info_downloaded
									self.prgrs(downloaded, n)
									self['info'].setText("  " + title.upper() + ", OMDB, INFO")
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("info Omdb, %s, %s\n"%(title, err))
								continue
					if config.plugins.xtraEvent.infoImdb.value:
						if not os.path.exists(dwnldFile):
							imdb_id = None
							Year = ""
							Rating=""
							Rated=""
							glist=""
							Duration=""
							description=""
							Type=""
							try:
								url_find = 'https://m.imdb.com/find?q={}'.format(title)
								ff = requests.get(url_find).text
								rc = re.compile('<a href="/title/(.*?)/"', re.DOTALL)
								imdb_id = rc.search(ff).group(1)
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("info Imdb id, %s, %s\n"%(title, err))
							try:
								if not os.path.exists("/tmp/imdb.html"):
									url= "https://m.imdb.com/title/{}/?ref_=fn_al_tt_0".format(imdb_id)
									ff = requests.get(url).text
									with io.open("/tmp/imdb.html", "w", encoding="utf-8") as f:
										f.write(ff)
								if os.path.exists("/tmp/imdb.html"):
									with io.open("/tmp/imdb.html", "r", encoding="utf-8") as f:
										ff = f.read()
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("info Imdb html, %s, %s\n"%(title, err))
							# imdb poster
							try:
								p = 'src=\"https://(.*?)._V1_UX75_CR0,0,75,109_AL_.jpg'
								pstr = re.findall(p, ff)[0]
								pstr = "https://"+pstr+"._V1_UX185_AL_.jpg"
								if not os.path.exists(pathLoc + "poster/{}.jpg".format(title)):
									open(dwnldFile, 'wb').write(requests.get(url, stream=True, allow_redirects=True).content)
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("info Imdb, %s, %s\n"%(title, err))
							# imdb Rating
							try:
								rtng = re.findall('"aggregateRating":{(.*?)}',ff)[0] #ratingValue":8.4
								Rating = rtng.partition('ratingValue":')[2].partition('}')[0].strip()
								ratingCount = rtng.partition('ratingCount":')[2].partition(',"')[0].strip()# "ratingCount":1070843
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("info Imdb Rating, %s, %s\n"%(title, err))
							# imdb Rated
							try:
								Rated = ff.partition('contentRating":"')[2].partition('","')[0].replace("+", "").strip() # "contentRating":"18+","genre":["Crime","Drama","Thriller"],"datePublished":"2019-10-04"
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("info Imdb Rated, %s, %s\n"%(title, err))
							# imdb Genre
							try:
								glist=[]
								genre = ff.partition('genre":[')[2].partition('],')[0].strip().split(",")
								for i in genre:
									genre=(i.replace('"',''))
									glist.append(genre)
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("info Imdb Genre, %s, %s\n"%(title, err))
							# imdb Year
							try:
								Year = ff.partition('datePublished":"')[2].partition('"')[0].strip()
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("info Imdb Year, %s, %s\n"%(title, err))
							# imdb	Duration
							try:
								try:
									Duration = re.findall('\d+h \d+min', ff)[0]
								except:
									Duration = re.findall('\d+min', ff)[0]
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("info Imdb Duration, %s, %s\n"%(title, err))
							# imdb Description
							try:
								description = ff.partition('name="description" content="')[2].partition('" data-id="main"/>')[0].strip()
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("info Imdb Description, %s, %s\n"%(title, err))
							try:
								types = ff.partition('class="ipc-inline-list__item">')[2].partition('</li>')[0].strip().split(" ")
								if types[0].lower() == "tv":
									types = "Tv Series"
								else:
									types = "Movie"
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("info Imdb Type, %s, %s\n"%(title, err))
							try:
								infs = {
								"Title": "%s"%title, 
								# "Start-End Time": "%s"%setime,
								# "Category": "%s"%Category,
								"Year": "%s"%Year,
								"imdbRating": "%s"%Rating.replace("N/A", ""), 
								"Rated": "%s"%Rated,
								"Genre": "%s"%(', '.join(glist)), 
								"Duration": "%s"%Duration,
								# # "Language": "%s"%(', '.join(llist)),
								# # "Country": "%s"%(', '.join(clist)),
								# "Director": "%s"%(', '.join(dlist)),
								# "Writer": "%s"%(', '.join(wlist)),
								# "Cast": "%s"%(', '.join(calist)),
								"Type": "%s"%types,
								"Plot": "%s"%description,
								}
								info_files = pathLoc + "infos/{}.json".format(title)
								open(info_files, "w").write(json.dumps(infs))
								if os.path.exists("/tmp/imdb.html"):
									os.remove("/tmp/imdb.html")
								try:
									with open(dwnldFile) as f:
										rj = json.load(f)
									if rj["Response"] == "False" or rj["Title"] == "":
										os.remove(dwnldFile)
								except:
									pass
								if os.path.exists(dwnldFile):
									info_downloaded += 1
									downloaded = info_downloaded
									self.prgrs(downloaded, n)
									self['info'].setText("  " + title.upper() + ", IMDB, INFO")
							except Exception as err:
								with open("/tmp/xtra_error.log", "a+") as f:
									f.write("info Imdb json Create, %s, %s\n"%(title, err))
								continue
			now = datetime.now()
			dt = now.strftime("%d/%m/%Y %H:%M:%S")
			report = "\n\nSTART : {}\nEND : {}\
				\nPOSTER; Tmdb :{}, Tvdb :{}, Maze :{}, Fanart :{}\
				\nBACKDROP; Tmdb :{}, Tvdb :{}, Fanart :{}, Extra :{}, Extra2 :{}\
				\nBANNER :{}\
				\nINFOS :{}\
				\nEXTRA3 ; Poster :{}, Info :{}".format(st, dt, 
				str(tmdb_poster_downloaded), str(tvdb_poster_downloaded), str(maze_poster_downloaded), str(fanart_poster_downloaded), 
				str(tmdb_backdrop_downloaded), str(tvdb_backdrop_downloaded), str(fanart_backdrop_downloaded), 
				str(extra_downloaded), str(extra2_downloaded),
				str(banner_downloaded), 
				str(info_downloaded), 
				str(extra3_poster_downloaded), str(extra3_info_downloaded))
			self['info2'].setText(report)
			self.report = report
			try:
				if os.path.exists("/tmp/urlo.html"):
					os.remove("/tmp/urlo.html")
			except:
				pass			
			with open("/tmp/xtra_report", "a+") as f:
				f.write("%s"%report)
			Screen.show(self)
			self.brokenImageRemove()
			self.brokenInfoRemove()
			self.cleanRam()
			return
####################################################################################################################################
	def prgrs(self, downloaded, n):
		self['status'].setText("Download : {} / {}".format(downloaded, n))
		self['progress'].setValue(int(100*downloaded//n))

	def showPoster(self, dwnldFile):
		if config.plugins.xtraEvent.onoff.value:
			if not config.plugins.xtraEvent.timerMod.value:
				self["Picture2"].hide()
				self["Picture"].instance.setPixmap(loadJPG(dwnldFile))
				self["Picture"].instance.setScale(1)
				self["Picture"].show()
				if desktop_size <= 1280:
					self["Picture"].instance.resize(eSize(185,278))
					self["Picture"].instance.move(ePoint(955,235))
					self["Picture"].instance.setScale(1)
				else:
					self["Picture"].instance.setScale(1)
					self["Picture"].instance.resize(eSize(185,278))
					self["Picture"].instance.move(ePoint(1450,400))

	def showBackdrop(self, dwnldFile):
		if config.plugins.xtraEvent.onoff.value:
			if not config.plugins.xtraEvent.timerMod.value:
				self["Picture2"].hide()
				self["Picture"].instance.setPixmap(loadJPG(dwnldFile))
				if desktop_size <= 1280:
					self["Picture"].instance.resize(eSize(300,170))
					self["Picture"].instance.move(ePoint(895,280))
					self["Picture"].instance.setScale(1)
				else:
					self["Picture"].instance.setScale(1)
					self["Picture"].instance.resize(eSize(300,170))
					self["Picture"].instance.move(ePoint(1400,400))

	def showBanner(self, dwnldFile):
		if config.plugins.xtraEvent.onoff.value:
			if not config.plugins.xtraEvent.timerMod.value:
				self["Picture2"].hide()
				self["Picture"].instance.setPixmap(loadJPG(dwnldFile))
				if desktop_size <= 1280:
					self["Picture"].instance.resize(eSize(400,80))
					self["Picture"].instance.move(ePoint(845,320))
					self["Picture"].instance.setScale(1)
				else:
					self["Picture"].instance.setScale(1)
					self["Picture"].instance.resize(eSize(400,90))
					self["Picture"].instance.move(ePoint(1400,400))

	def showFilm(self):
		self["Picture2"].instance.setPixmapFromFile("/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/film2.png")
		self["Picture2"].instance.setScale(1)
		self["Picture2"].show()

	def brokenImageRemove(self):
		b = os.listdir(pathLoc)
		rmvd = 0
		try:
			for i in b:
				bb = pathLoc + "{}/".format(i)
				fc = os.path.isdir(bb)
				if fc != False:	
					for f in os.listdir(bb):
						if f.endswith('.jpg'):
							try:
								img = Image.open(bb+f)
								img.verify()
							except:
								try:
									os.remove(bb+f)
									rmvd += 1
								except:
									pass
		except:
			pass

	def brokenInfoRemove(self):
		try:
			infs = os.listdir(pathLoc + "infos")
			for i in infs:
				with open(pathLoc + "infos/{}".format(i)) as f:
					rj = json.load(f)
				if rj["Response"] == "False":
					os.remove(pathLoc + "infos/{}".format(i))
		except:
			pass
			
	def cleanRam(self):
		os.system("echo 1 > /proc/sys/vm/drop_caches")
		os.system("echo 2 > /proc/sys/vm/drop_caches")
		os.system("echo 3 > /proc/sys/vm/drop_caches")
