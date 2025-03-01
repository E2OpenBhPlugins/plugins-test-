# by digiteng
# 11.2021
from __future__ import absolute_import
from Components.Renderer.Renderer import Renderer
from Components.VariableValue import VariableValue
from enigma import ePoint, eWidget, eSize, eSlider, loadPNG 
from Components.config import config
import re
import json
import os

try:
	pathLoc = config.plugins.xtraEvent.loc.value
except:
	pathLoc = ""

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

class xtraStar(VariableValue, Renderer):
	def __init__(self):
		Renderer.__init__(self)
		VariableValue.__init__(self)
		self.star = None

	def applySkin(self, desktop, screen):
		attribs = self.skinAttributes[:]
		for attrib, value in self.skinAttributes:
			if attrib == 'size':
				self.szX = int(value.split(',')[0])
				self.szY = int(value.split(',')[1])
			elif attrib == 'pixmap':
				self.pxmp = value
		self.star.setRange(0, 100)
		self.skinAttributes = attribs
		return Renderer.applySkin(self, desktop, screen)

	GUI_WIDGET = eWidget
	def changed(self, what):
		if not self.instance:
			return
		else:
			if what[0] != self.CHANGED_CLEAR:
				rating = None
				event = self.source.event
				if event:
					evnt = event.getEventName()
					try:
						evntNm = REGEX.sub('', evnt).strip()
						rating_json = pathLoc + "xtraEvent/infos/{}.json".format(evntNm)
						if os.path.exists(rating_json):
							with open(rating_json) as f:
								rating = json.load(f)['imdbRating']
							if rating:
								rtng = int(10*(float(rating)))
							else:
								rtng = 0
						else:
							rtng = 0
					except Exception as err:
						with open("/tmp/xtra_error.log", "a+") as f:
							f.write("xtraStar : %s\n"%err)
						rtng = 0
						return
				else:
					rtng = 0
				self.star.setValue(rtng)
				self.star.move(ePoint(0, 0))
				self.star.resize(eSize(self.szX, self.szY))
				self.star.setPixmap(loadPNG(self.pxmp))
				#self.star.setAlphatest(1)
				self.star.show()
			else:
				self.star.hide()

	def GUIcreate(self, parent):
		self.instance = eWidget(parent)
		self.star = eSlider(self.instance)
