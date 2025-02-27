# -*- coding: utf-8 -*-

from Components.config import config

skinColor = "#3478c1"
try:
	skinColor = config.plugins.xtraEvent.skinSelectColor.value
except:
	pass

xtra_720 = """
<screen name="xtra" position="0,0" size="1280,720" title="xtraEvent..." flags="wfNoBorder" backgroundColor="transparent">
	<widget source="Title" render="Label" position="30,30" size="770,40" font="Regular; 30" foregroundColor="#ffffff" backgroundColor="{0}" transparent="0" halign="center" valign="center" />
	<widget name="config" position="45,100" size="740,510" itemHeight="30" font="Regular;20" foregroundColor="#ffffff" scrollbarMode="showOnDemand" transparent="1" backgroundColor="#30000000" backgroundColorSelected="{0}" foregroundColorSelected="#ffffff" />
	<widget source="help" position="845,560" size="400,52" render="Label" font="Regular;20" foregroundColor="#f3fc92" backgroundColor="#30000000" halign="left" valign="center" transparent="1" />
	<widget name="status" position="845,100" size="400,30" transparent="1" font="Regular;20" foregroundColor="#92f1fc" backgroundColor="#30000000" />
	<widget name="info" position="845,145" size="400,390" transparent="1" font="Regular;20" foregroundColor="#ffffff" backgroundColor="#30000000" halign="left" valign="top" zPosition="5" />
	<widget name="int_statu" position="1230,40" size="30,22" text="" font="Regular; 22" foregroundColor="#1edb76" backgroundColor="#23262e" zPosition="2" transparent="1" />
	<eLabel name="int_statu_off" position="1230,40" size="30,22" text="" font="Regular; 22" foregroundColor="#555555" backgroundColor="#23262e" zPosition="1" transparent="1" />
	<eLabel name="red" position="45,680" size="185,10" backgroundColor="#ef2f2f" zPosition="2" />
	<eLabel name="green" position="230,680" size="185,10" backgroundColor="#2fef53" zPosition="2" />
	<eLabel name="yellow" position="415,680" size="185,10" backgroundColor="#edd02f" zPosition="2" />
	<eLabel name="blue" position="600,680" size="185,10" backgroundColor="#2fc7ed" zPosition="2" />
	<widget source="key_red" render="Label" font="Regular;20" foregroundColor="#ffffff" backgroundColor="#30000000" position="45,647" size="185,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_green" render="Label" font="Regular;20" foregroundColor="#ffffff" backgroundColor="#30000000" position="230,647" size="185,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_yellow" render="Label" font="Regular;20" foregroundColor="#ffffff" backgroundColor="#30000000" position="416,647" size="185,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_blue" render="Label" font="Regular; 20" foregroundColor="#ffffff" backgroundColor="#30000000" position="600,647" size="185,30" halign="center" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="825,30" size="440,40" font="Regular; 30" halign="center" valign="center" transparent="0" foregroundColor="#ffffff" backgroundColor="{0}" zPosition="0">
		<convert type="ClockToText">Default</convert>
	</widget>
	<ePixmap position="890,240" size="320,232" zPosition="0" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/film2.png" transparent="1" alphatest="blend" />
	<eLabel name="menu" text="" position="845,647" size="100,30" backgroundColor="#30000000" transparent="1" halign="left" font="Regular; 20" />
	<eLabel name="info" text="" position="1145,647" size="100,30" backgroundColor="#30000000" transparent="1" halign="right" font="Regular; 20" />
	<eLabel name="new eLabel" position="845,680" size="400,10" backgroundColor="#40484c" zPosition="2" />

	<eLabel name="" position="30,30" size="770,660" backgroundColor="#30000000" zPosition="-1" />
	<eLabel name="" position="825,30" size="440,660" backgroundColor="#30000000" zPosition="-1" />
	<!-- <eLabel name="" position="45,90" size="740,2" backgroundColor="#40484c" zPosition="1" /> -->
	<eLabel name="" position="45,620" size="740,2" backgroundColor="#40484c" zPosition="1" />
	<!-- <eLabel name="" position="845,90" size="400,2" backgroundColor="#40484c" zPosition="1" /> -->
	<eLabel name="" position="845,620" size="400,2" backgroundColor="#40484c" zPosition="1" />
	<eLabel name="" position="845,550" size="400,2" backgroundColor="#40484c" zPosition="1" />
</screen>""".format(skinColor)

download_720 = """
<screen name="downloads" position="0,0" size="1280,720" title="downloads..." flags="wfNoBorder" backgroundColor="#ff000000">
	<widget source="Title" render="Label" position="30,30" size="770,40" font="Regular; 30" foregroundColor="#ffffff" backgroundColor="{0}" transparent="0" halign="center" valign="center" />
	<widget name="progress" position="45,100" size="740,20" foregroundColor="#ffffff" borderColor="#ffffff" borderWidth="1" backgroundColor="#30000000" />
	<widget name="status" position="45,130" size="740,30" transparent="1" font="Regular; 22" foregroundColor="#92f1fc" backgroundColor="#30000000" />
	<widget name="info" position="45,170" size="740,60" transparent="1" font="Regular; 22" foregroundColor="#ffffff" backgroundColor="#30000000" valign="top" />
	<widget name="info2" position="45,240" size="740,370" transparent="1" font="Regular; 24" foregroundColor="#ffffff" backgroundColor="#30000000" />
	<widget name="int_statu" position="1230,40" size="30,22" text="" font="Regular; 22" foregroundColor="#1edb76" backgroundColor="#23262e" zPosition="2" transparent="1" />
	<eLabel name="int_statu_off" position="1230,40" size="30,22" text="" font="Regular; 22" foregroundColor="#555555" backgroundColor="#23262e" zPosition="1" transparent="1" />
	<eLabel name="red" position="45,680" size="185,10" backgroundColor="#ef2f2f" zPosition="2" />
	<eLabel name="green" position="230,680" size="185,10" backgroundColor="#2fef53" zPosition="2" />
	<eLabel name="yellow" position="415,680" size="185,10" backgroundColor="#edd02f" zPosition="2" />
	<eLabel name="blue" position="600,680" size="185,10" backgroundColor="#2fc7ed" zPosition="2" />
	<widget source="key_red" render="Label" font="Regular;20" foregroundColor="#ffffff" backgroundColor="#30000000" position="45,647" size="185,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_green" render="Label" font="Regular;20" foregroundColor="#ffffff" backgroundColor="#30000000" position="230,647" size="185,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_yellow" render="Label" font="Regular;20" foregroundColor="#ffffff" backgroundColor="#30000000" position="416,647" size="185,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_blue" render="Label" font="Regular; 20" foregroundColor="#ffffff" backgroundColor="#30000000" position="600,647" size="185,30" halign="center" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="825,30" size="440,40" font="Regular; 30" halign="center" valign="center" transparent="0" foregroundColor="#ffffff" backgroundColor="{0}" zPosition="0">
		<convert type="ClockToText">Default</convert>
	</widget>
	<eLabel name="" position="45,620" size="740,2" backgroundColor="#666666" zPosition="1" />
	<!-- <ePixmap position="890,100" size="320,232" zPosition="0" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/film2.png" transparent="1" alphatest="blend" /> -->
	<widget name="Picture" position="890,240" size="400,278" zPosition="9" transparent="1" />
	<widget name="Picture2" position="890,240" size="320,232" zPosition="1" transparent="1" alphatest="blend" />
	<eLabel name="" position="30,30" size="770,660" backgroundColor="#30000000" zPosition="-1" />
	<eLabel name="" position="825,30" size="440,660" backgroundColor="#30000000" zPosition="-1" />

</screen>""".format(skinColor)

manuel_720 = """
<screen name="manuelSearch" position="center,center" size="1280,720" title="Manuel Search..." backgroundColor="transparent" flags="wfNoBorder">
	<widget source="Title" render="Label" position="30,30" size="770,40" font="Regular; 30" foregroundColor="#ffffff" backgroundColor="{0}" transparent="0" halign="center" valign="center" />
	<widget source="session.CurrentService" render="Label" position="45,100" size="740,40" zPosition="1" font="Console; 30" transparent="1" backgroundColor="30000000" valign="center">
		<convert type="ServiceName">Name</convert>
	</widget>
	<widget name="config" position="45,145" size="740,391" itemHeight="30" font="Regular;22" foregroundColor="#ffffff" scrollbarMode="showOnDemand" transparent="1" backgroundColor="30000000" backgroundColorSelected="{0}" foregroundColorSelected="#ffffff" />
	<widget name="status" position="45,585" size="740,30" transparent="1" font="Regular;22" foregroundColor="#92f1fc" backgroundColor="30000000" />
	<widget name="info" position="840,640" size="400,30" transparent="1" font="Regular;22" halign="center" foregroundColor="#ffffff" backgroundColor="30000000" />
	<widget name="int_statu" position="1230,40" size="30,22" text="" font="Regular; 22" foregroundColor="#1edb76" backgroundColor="#23262e" zPosition="2" transparent="1" />
	<eLabel name="int_statu_off" position="1230,40" size="30,22" text="" font="Regular; 22" foregroundColor="#555555" backgroundColor="#23262e" zPosition="1" transparent="1" />
	<widget name="progress" position="45,555" size="740,20" foregroundColor="#ffffff" borderColor="#ffffff" borderWidth="1"  backgroundColor="#30000000" />

	<eLabel name="red" position="45,680" size="185,10" backgroundColor="#ef2f2f" zPosition="2" />
	<eLabel name="green" position="230,680" size="185,10" backgroundColor="#2fef53" zPosition="2" />
	<eLabel name="yellow" position="415,680" size="185,10" backgroundColor="#edd02f" zPosition="2" />
	<eLabel name="blue" position="600,680" size="185,10" backgroundColor="#2fc7ed" zPosition="2" />
	<widget source="key_red" render="Label" font="Regular;20" foregroundColor="#ffffff" backgroundColor="#30000000" position="45,647" size="185,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_green" render="Label" font="Regular;20" foregroundColor="#ffffff" backgroundColor="#30000000" position="230,647" size="185,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_yellow" render="Label" font="Regular;20" foregroundColor="#ffffff" backgroundColor="#30000000" position="416,647" size="185,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_blue" render="Label" font="Regular; 20" foregroundColor="#ffffff" backgroundColor="#30000000" position="600,647" size="185,30" halign="center" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="825,30" size="440,40" font="Regular; 30" halign="center" valign="center" transparent="0" foregroundColor="#ffffff" backgroundColor="{0}" zPosition="0">
		<convert type="ClockToText">Default</convert>
	</widget>
	<!-- <eLabel name="" position="45,620" size="740,2" backgroundColor="#666666" zPosition="1" /> -->
	<!-- <ePixmap position="890,100" size="320,232" zPosition="0" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/film2.png" transparent="1" alphatest="blend" /> -->
	<widget name="Picture" position="890,240" size="400,278" zPosition="2" transparent="1" />
	<widget name="Picture2" position="890,240" size="320,232" zPosition="1" transparent="1" alphatest="blend" />
	<eLabel name="" position="30,30" size="770,660" backgroundColor="#30000000" zPosition="-1" />
	<eLabel name="" position="825,30" size="440,660" backgroundColor="#30000000" zPosition="-1" />
	<!-- <eLabel name="" position="45,90" size="740,2" backgroundColor="#666666" zPosition="1" /> -->
	<eLabel name="" position="45,620" size="740,2" backgroundColor="#666666" zPosition="1" />
	<!-- <eLabel name="" position="845,90" size="400,2" backgroundColor="#666666" zPosition="1" /> -->
	<eLabel name="" position="845,620" size="400,2" backgroundColor="#666666" zPosition="1" />
</screen>""".format(skinColor)

selbuq_720 = """
<screen name="selBouquets" position="0,0" size="1280,720" title="bouquets..." backgroundColor="transparent">
	<widget source="Title" render="Label" position="45,40" size="745,40" font="Console; 30" foregroundColor="#ffffff" backgroundColor="30000000" transparent="1" />
	<widget name="list" position="45,100" size="740,510" itemHeight="30" font="Regular;22" foregroundColor="#ffffff" scrollbarMode="showOnDemand" transparent="1" backgroundColor="30000000" backgroundColorSelected="{0}" foregroundColorSelected="#ffffff" />
	<widget name="status" position="845,100" size="400,30" transparent="1" font="Regular;22" foregroundColor="#92f1fc" backgroundColor="30000000" />
	<widget name="info" position="845,145" size="400,390" transparent="1" font="Regular;22" foregroundColor="#ffffff" backgroundColor="30000000" halign="left" valign="top" />
	<eLabel name="new eLabel" position="45,640" size="10,30" backgroundColor="#d90000" zPosition="2" />
	<eLabel name="new eLabel" position="225,640" size="10,30" backgroundColor="#2db300" zPosition="2" />
	<eLabel name="new eLabel" position="410,640" size="10,30" backgroundColor="#ffd24c" zPosition="2" />
	<eLabel name="new eLabel" position="600,640" size="10,30" backgroundColor="#00a3d9" zPosition="2" />
	<widget source="key_red" render="Label" font="Regular;20" foregroundColor="#ffffff" backgroundColor="30000000" position="65,645" size="150,30" halign="left" transparent="1" zPosition="1" />
	<widget source="key_green" render="Label" font="Regular;20" foregroundColor="#ffffff" backgroundColor="30000000" position="245,645" size="150,30" halign="left" transparent="1" zPosition="1" />
	<widget source="key_yellow" render="Label" font="Regular;20" foregroundColor="#ffffff" backgroundColor="30000000" position="430,645" size="150,30" halign="left" transparent="1" zPosition="1" />
	<widget source="key_blue" render="Label" font="Regular; 20" foregroundColor="#ffffff" backgroundColor="30000000" position="620,645" size="150,30" halign="left" transparent="1" zPosition="1" />
	<eLabel name="" position="30,30" size="771,660" backgroundColor="#30000000" zPosition="-1" />
	<eLabel name="" position="45,90" size="740,2" backgroundColor="#666666" zPosition="1" />
	<eLabel name="" position="45,620" size="740,2" backgroundColor="#666666" zPosition="1" />
</screen>""".format(skinColor)


xtra_720_2 = """
<screen name="xtra" position="0,0" size="1280,720" title="xtraEvent..." flags="wfNoBorder">
	<ePixmap position="0,0" size="1280,720" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/xtra_hd3.png" transparent="1" />
	<widget source="Title" render="Label" position="40,35" size="745,40" font="Regular; 30" foregroundColor="#c5c5c5" backgroundColor="#23262e" transparent="1" />
	<widget name="config" position="40,95" size="745,510" itemHeight="30" font="Regular;24" foregroundColor="#c5c5c5" scrollbarMode="showOnDemand" transparent="1" backgroundColor="#23262e" backgroundColorSelected="#565d6d" foregroundColorSelected="#ffffff" />
	<widget source="help" position="840,600" size="400,26" render="Label" font="Regular;22" foregroundColor="#f3fc92" backgroundColor="#23262e" halign="left" valign="center" transparent="1" />
	<widget name="status" position="840,300" size="400,30" transparent="1" font="Regular;22" foregroundColor="#92f1fc" backgroundColor="#23262e" />
	<widget name="info" position="840,330" size="400,260" transparent="1" font="Regular;22" foregroundColor="#c5c5c5" backgroundColor="#23262e" halign="left" valign="top" />
	<widget name="int_statu" position="1210,40" size="30,22" transparent="1" text="" font="Regular; 22" foregroundColor="#1edb76" backgroundColor="#23262e" zPosition="2" halign="center" />
	<eLabel name="int_statu_off" position="1210,40" size="30,22" text="" font="Regular; 22" foregroundColor="#555555" backgroundColor="#23262e" zPosition="1" transparent="1" /> 
	<widget source="key_red" render="Label" font="Regular;22" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="45,640" size="170,30" halign="left" transparent="1" zPosition="1" />
	<widget source="key_green" render="Label" font="Regular;22" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="235,640" size="170,30" halign="left" transparent="1" zPosition="1" />
	<widget source="key_yellow" render="Label" font="Regular;22" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="425,640" size="170,30" halign="left" transparent="1" zPosition="1" />
	<widget source="key_blue" render="Label" font="Regular; 20" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="615,640" size="170,30" halign="left" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="839,40" size="400,30" font="Regular; 25" valign="center" halign="center" transparent="1" foregroundColor="#c5c5c5" backgroundColor="#23262e" zPosition="2">
		<convert type="ClockToText">Default</convert>
	</widget>
	<eLabel name="menu" text="" position="785,640" size="150,30" transparent="1" halign="center" font="Regular; 20" />
	<eLabel name="info" text="" position="1175,640" size="100,30" transparent="1" halign="center" font="Regular; 20" />
</screen>"""
download_720_2 = """
<screen name="downloads" position="0,0" size="1280,720" title="downloads..." flags="wfNoBorder" backgroundColor="transparent">
	<ePixmap position="0,0" size="1280,720" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/xtra_hd3.png" zPosition="-1" transparent="1" />
	<widget source="Title" render="Label" position="40,35" size="745,40" font="Regular; 30" foregroundColor="#ffffff" backgroundColor="#23262e" transparent="1" />
	<widget name="progress" position="40,100" size="740,20" foregroundColor="#ffffff" borderColor="#ffffff" borderWidth="1" backgroundColor="#23262e" />
	<widget name="status" position="40,130" size="740,30" transparent="1" font="Regular; 24" foregroundColor="#92f1fc" backgroundColor="#23262e" />
	<widget name="info" position="40,175" size="740,40" transparent="1" font="Regular; 24" foregroundColor="#ffffff" backgroundColor="#23262e" valign="top" />
	<widget name="info2" position="40,220" size="740,400" transparent="1" font="Regular; 24" foregroundColor="#ffffff" backgroundColor="#23262e" />
	<widget source="key_red" render="Label" font="Regular;22" foregroundColor="#ffffff" backgroundColor="#23262e" position="45,640" size="170,30" halign="left" transparent="1" zPosition="1" />
	<widget source="key_green" render="Label" font="Regular;22" foregroundColor="#ffffff" backgroundColor="#23262e" position="235,640" size="170,30" halign="left" transparent="1" zPosition="1" />
	<widget source="key_yellow" render="Label" font="Regular;22" foregroundColor="#ffffff" backgroundColor="#23262e" position="425,640" size="170,30" halign="left" transparent="1" zPosition="1" />
	<widget source="key_blue" render="Label" font="Regular; 20" foregroundColor="#ffffff" backgroundColor="#23262e" position="615,640" size="170,30" halign="left" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="839,40" size="400,30" font="Regular; 25" valign="center" halign="center" transparent="1" foregroundColor="#ffffff" backgroundColor="#23262e" zPosition="2">
		<convert type="ClockToText">Default</convert>
	</widget>
	<widget name="int_statu" position="1210,40" size="30,22" transparent="1" text="" font="Regular; 22" foregroundColor="#1edb76" backgroundColor="#23262e" zPosition="2" halign="center" />
	<eLabel name="int_statu_off" position="1210,40" size="30,22" text="" font="Regular; 22" foregroundColor="#555555" backgroundColor="#23262e" zPosition="1" transparent="1" />
	<widget name="Picture" position="840,324" size="400,278" zPosition="9" transparent="1" />
	<!-- <widget name="Picture2" position="892,343" size="320,232" zPosition="1" transparent="1" alphatest="blend" /> -->
</screen>"""
manuel_720_2 = """
<screen name="manuelSearch" position="center,center" size="1280,720" title="Manuel Search..." backgroundColor="transparent" flags="wfNoBorder">
	<ePixmap position="0,0" size="1280,720" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/xtra_hd3.png" transparent="1" />
	<widget source="Title" render="Label" position="40,40" size="745,40" font="Regular; 30" foregroundColor="#c5c5c5" backgroundColor="#23262e" transparent="1" />
	<widget source="session.CurrentService" render="Label" position="40,80" size="745,40" zPosition="1" font="Regular; 30" transparent="1" backgroundColor="#23262e" valign="center">
		<convert type="ServiceName">Name</convert>
	</widget>
	<widget name="config" position="40,145" size="745,391" itemHeight="30" font="Regular;24" foregroundColor="#c5c5c5" scrollbarMode="showOnDemand" transparent="1" backgroundColor="#23262e" backgroundColorSelected="#0d71aa" foregroundColorSelected="#ffffff" />
	<widget name="status" position="40,590" size="745,30" transparent="1" font="Regular;24" foregroundColor="#92f1fc" backgroundColor="#23262e" />
	<widget name="info" position="840,640" size="400,30" transparent="1" font="Regular;22" halign="center" foregroundColor="#c5c5c5" backgroundColor="#23262e" />
	<widget name="Picture" position="840,320" size="185,278" zPosition="5" transparent="1" />
	<widget name="progress" position="40,560" size="745,20" foregroundColor="prgrsbs" borderColor="prgrsbs" borderWidth="1"  backgroundColor="#23262e" />
	<widget source="key_red" render="Label" font="Regular;22" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="40,640" size="170,30" halign="left" transparent="1" zPosition="1" />
	<widget source="key_green" render="Label" font="Regular;22" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="230,640" size="170,30" halign="left" transparent="1" zPosition="1" />
	<widget source="key_yellow" render="Label" font="Regular;22" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="420,640" size="170,30" halign="left" transparent="1" zPosition="1" />
	<widget source="key_blue" render="Label" font="Regular;22" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="610,640" size="170,30" halign="left" transparent="1" zPosition="1" />
	<eLabel name="" position="40,120" size="745, 1" backgroundColor="#898989" />
	<widget name="int_statu" position="1210,40" size="30,22" transparent="1" text="" font="Regular; 22" foregroundColor="#1edb76" backgroundColor="#23262e" zPosition="2" halign="center" />
	<eLabel name="int_statu_off" position="1210,40" size="30,22" text="" font="Regular; 22" foregroundColor="#555555" backgroundColor="#23262e" zPosition="1" transparent="1" />
</screen>"""		
selbuq_720_2 = """
<screen name="selBouquets" position="center,center" size="1280,720" title="xtraEvent v1" backgroundColor="#ffffff">
<ePixmap position="0,0" size="1280,720" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/xtra_hd3.png" transparent="1" />
<widget source="Title" render="Label" position="40,35" size="745,40" font="Regular; 30" foregroundColor="#c5c5c5" backgroundColor="#23262e" transparent="1" />
<widget name="list" position="40,95" size="745,510" itemHeight="30" font="Regular;24" foregroundColor="#c5c5c5" scrollbarMode="showOnDemand" transparent="1" backgroundColor="#23262e" backgroundColorSelected="#0d71aa" foregroundColorSelected="#ffffff" />

<widget name="status" position="840,300" size="400,30" transparent="1" font="Regular;22" foregroundColor="#92f1fc" backgroundColor="#23262e" />
<widget name="info" position="840,330" size="400,270" transparent="1" font="Regular;10" foregroundColor="#c5c5c5" backgroundColor="#23262e" halign="left" valign="top" />
<widget source="key_red" render="Label" font="Regular;22" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="40,640" size="170,30" halign="left" transparent="1" zPosition="1" />
<widget source="key_green" render="Label" font="Regular;22" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="230,640" size="170,30" halign="left" transparent="1" zPosition="1" />
<widget source="key_yellow" render="Label" font="Regular;22" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="420,640" size="170,30" halign="left" transparent="1" zPosition="1" />
<widget source="key_blue" render="Label" font="Regular;22" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="610,640" size="170,30" halign="left" transparent="1" zPosition="1" />

</screen>"""


xtra_1080 = """
<screen name="xtra" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder" backgroundColor="transparent">
	<widget source="Title" render="Label" position="30,30" size="1165,60" font="Regular; 34" halign="center" valign="center" foregroundColor="#ffffff" backgroundColor="{0}" transparent="0" />
	<!-- <ePixmap position="620,30" size="330,70" zPosition="3" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/xtra_title.png" transparent="1" alphatest="blend" /> -->
	<widget name="config" position="60,140" size="1100,800" itemHeight="45" font="Regular;34" foregroundColor="#ffffff" scrollbarMode="showOnDemand" transparent="1" backgroundColor="#30000000" backgroundColorSelected="{0}" foregroundColorSelected="#ffffff" />
	<widget source="help" position="1255,860" size="600,100" render="Label" font="Regular;28" foregroundColor="#f3fc92" backgroundColor="#30000000" halign="left" valign="center" transparent="1" />
	<widget name="status" position="1255,140" size="600,45" transparent="1" font="Regular;32" foregroundColor="#92f1fc" backgroundColor="#30000000" />
	<widget name="info" position="1255,220" size="600,600" transparent="1" font="Regular;32" foregroundColor="#ffffff" backgroundColor="#30000000" halign="left" valign="top" zPosition="1" />
	<widget name="int_statu" text="" font="Regular; 30" position="1835,40" size="40,40" foregroundColor="#1edb76" backgroundColor="{0}" zPosition="2" transparent="1" />
	<eLabel name="int_statu_off" text="" font="Regular; 30" position="1840,35" size="40,40" foregroundColor="#555555" backgroundColor="{0}" zPosition="1" transparent="1" />	
	<eLabel name="red" position="60,1040" size="275,10" backgroundColor="#ef2f2f" zPosition="2" />
	<eLabel name="green" position="335,1040" size="275,10" backgroundColor="#2fef53" zPosition="2" />
	<eLabel name="yellow" position="610,1040" size="275,10" backgroundColor="#edd02f" zPosition="2" />
	<eLabel name="blue" position="885,1040" size="275,10" backgroundColor="#2fc7ed" zPosition="2" />
	<widget source="key_red" render="Label" font="Regular;26" foregroundColor="#ffffff" backgroundColor="#30000000" position="60,1010" size="275,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_green" render="Label" font="Regular;26" foregroundColor="#ffffff" backgroundColor="#30000000" position="335,1010" size="275,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_yellow" render="Label" font="Regular;26" foregroundColor="#ffffff" backgroundColor="#30000000" position="611,1010" size="275,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_blue" render="Label" font="Regular; 26" foregroundColor="#ffffff" backgroundColor="#30000000" position="885,1010" size="275,30" halign="center" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="1220,30" size="670,60" font="Regular; 34" valign="center" halign="center" transparent="0" foregroundColor="#ffffff" backgroundColor="{0}" zPosition="2">
		<convert type="ClockToText">Default</convert>
	</widget>
	<eLabel name="menu" text="" position="1255,1000" size="40,40" backgroundColor="#30000000" transparent="1" halign="left" font="Regular; 40" />
	<eLabel name="info" text="" position="1815,1000" size="40,40" backgroundColor="#30000000" transparent="1" halign="right" font="Regular; 40" />
	<eLabel name="new eLabel" position="1255,1040" size="600,10" backgroundColor="#40484c" zPosition="2" />

	<eLabel name="" position="30,30" size="1165,1020" backgroundColor="#30000000" zPosition="-1" />
	<eLabel name="" position="1220,30" size="670,1020" backgroundColor="#30000000" zPosition="-1" />
	<!-- <eLabel name="" position="30,30" size="1165,60" backgroundColor="{0}" zPosition="1" /> -->
	<eLabel name="" position="60,970" size="1100,2" backgroundColor="#666666" zPosition="1" />
	<!-- <eLabel name="" position="1260,130" size="600,2" backgroundColor="#666666" zPosition="1" /> -->
	<eLabel name="" position="1255,845" size="600,2" backgroundColor="#666666" zPosition="1" />
	<eLabel name="" position="1255,970" size="600,2" backgroundColor="#666666" zPosition="1" />
	<ePixmap position="1410,413" size="320,232" zPosition="0" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/film2.png" transparent="1" alphatest="blend" />
</screen>""".format(skinColor)

download_1080 = """	
<screen name="downloads" position="0,0" size="1920,1080" title="downloads..." flags="wfNoBorder" backgroundColor="transparent">
	<widget source="Title" render="Label" position="30,30" size="1165,60" font="Regular; 45" halign="center" foregroundColor="#ffffff" backgroundColor="{0}" transparent="0" />
	<widget name="progress" position="60,148" size="1100,20" foregroundColor="#ffffff" borderColor="#ffffff" borderWidth="1" backgroundColor="#30000000" />
	<widget name="status" position="60,190" size="1100,44" transparent="1" font="Regular;33" foregroundColor="#92f1fc" backgroundColor="#30000000" />
	<widget name="info" position="60,270" size="1100,44" transparent="1" font="Regular;33" foregroundColor="#ffffff" backgroundColor="#30000000" valign="top" />
	<widget name="info2" position="60,335" size="1100,600" transparent="1" font="Regular; 33" foregroundColor="#ffffff" backgroundColor="#30000000" />
	<widget name="int_statu" text="" font="Regular; 30" position="1835,40" size="40,40" foregroundColor="#1edb76" backgroundColor="{0}" zPosition="2" transparent="1" />
	<eLabel name="int_statu_off" text="" font="Regular; 30" position="1840,35" size="40,40" foregroundColor="#555555" backgroundColor="{0}" zPosition="1" transparent="1" />
	<eLabel name="red" position="60,1040" size="275,10" backgroundColor="#ef2f2f" zPosition="2" />
	<eLabel name="green" position="335,1040" size="275,10" backgroundColor="#2fef53" zPosition="2" />
	<eLabel name="yellow" position="610,1040" size="275,10" backgroundColor="#edd02f" zPosition="2" />
	<eLabel name="blue" position="885,1040" size="275,10" backgroundColor="#2fc7ed" zPosition="2" />
	<widget source="key_red" render="Label" font="Regular;26" foregroundColor="#ffffff" backgroundColor="#30000000" position="60,1010" size="275,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_green" render="Label" font="Regular;26" foregroundColor="#ffffff" backgroundColor="#30000000" position="335,1010" size="275,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_yellow" render="Label" font="Regular;26" foregroundColor="#ffffff" backgroundColor="#30000000" position="611,1010" size="275,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_blue" render="Label" font="Regular; 26" foregroundColor="#ffffff" backgroundColor="#30000000" position="885,1010" size="275,30" halign="center" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="1220,30" size="670,60" font="Regular; 34" valign="center" halign="center" transparent="0" foregroundColor="#ffffff" backgroundColor="{0}" zPosition="2">
		<convert type="ClockToText">Default</convert>
	</widget>
	<widget name="Picture" position="1258,400" size="596,278" zPosition="2" transparent="1" />
	<widget name="Picture2" position="1410,400" size="320,232" zPosition="1" transparent="1" alphatest="blend" />
	<eLabel name="" position="30,30" size="1165,1020" backgroundColor="#30000000" zPosition="-1" />
	<eLabel name="" position="1220,30" size="670,1020" backgroundColor="#30000000" zPosition="-1" />
	<!-- <eLabel name="" position="60,130" size="1100,2" backgroundColor="#666666" zPosition="1" /> -->
	<eLabel name="" position="60,950" size="1100,2" backgroundColor="#666666" zPosition="1" />
	<!-- <eLabel name="" position="1260,130" size="600,2" backgroundColor="#666666" zPosition="1" /> -->
	<eLabel name="" position="1260,950" size="600,2" backgroundColor="#666666" zPosition="1" />
	<!-- <ePixmap position="1410,120" size="320,232" zPosition="0" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/film2.png" transparent="1" alphatest="blend" /> -->
</screen>""".format(skinColor)

manuel_1080 = """
<screen name="manuelSearch" position="center,center" size="1920,1080" title="Manuel Search..." backgroundColor="transparent" flags="wfNoBorder">
	<widget source="Title" render="Label" position="30,30" size="1165,60" font="Console; 45" halign="center"  foregroundColor="#ffffff" backgroundColor="{0}" transparent="0" />
	<widget source="session.CurrentService" render="Label" position="60,145" size="1100,60" zPosition="2" font="Console; 45" transparent="1" backgroundColor="#30000000" valign="center">
		<convert type="ServiceName">Name</convert>
	</widget>
	<widget name="config" position="60,225" size="1100,588" itemHeight="45" font="Regular;36" foregroundColor="#ffffff" scrollbarMode="showOnDemand" transparent="1" backgroundColor="#30000000" backgroundColorSelected="{0}" foregroundColorSelected="#ffffff" />
	<widget name="status" position="60,885" size="1100,40" transparent="1" font="Regular;36" foregroundColor="#92f1fc" backgroundColor="#30000000" />
	<widget name="info" position="1260,980" size="600,45" transparent="1" font="Regular;33" halign="center" foregroundColor="#ffffff" backgroundColor="#30000000" />
	<widget name="Picture" position="1260,480" size="278,417" zPosition="5" transparent="1" />
	<widget name="Picture2" position="1410,400" size="320,232" zPosition="1" transparent="1" alphatest="blend" />
	<widget name="progress" position="60,840" size="1100,20" foregroundColor="#ffffff" borderColor="#ffffff" borderWidth="1"  backgroundColor="#30000000" />
	<widget name="int_statu" text="" font="Regular; 30" position="1835,40" size="40,40" foregroundColor="#1edb76" backgroundColor="{0}" zPosition="2" transparent="1" />
	<eLabel name="int_statu_off" text="" font="Regular; 30" position="1840,35" size="40,40" foregroundColor="#555555" backgroundColor="{0}" zPosition="1" transparent="1" />
	<eLabel name="red" position="60,1040" size="275,10" backgroundColor="#ef2f2f" zPosition="2" />
	<eLabel name="green" position="336,1040" size="275,10" backgroundColor="#2fef53" zPosition="2" />
	<eLabel name="yellow" position="610,1040" size="275,10" backgroundColor="#edd02f" zPosition="2" />
	<eLabel name="blue" position="885,1040" size="275,10" backgroundColor="#2fc7ed" zPosition="2" />
	<widget source="key_red" render="Label" font="Regular;26" foregroundColor="#ffffff" backgroundColor="#30000000" position="60,1010" size="275,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_green" render="Label" font="Regular;26" foregroundColor="#ffffff" backgroundColor="#30000000" position="335,1010" size="275,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_yellow" render="Label" font="Regular;26" foregroundColor="#ffffff" backgroundColor="#30000000" position="611,1010" size="275,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_blue" render="Label" font="Regular; 26" foregroundColor="#ffffff" backgroundColor="#30000000" position="885,1010" size="275,30" halign="center" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="1220,30" size="670,60" font="Regular; 34" valign="center" halign="center" transparent="0" foregroundColor="#ffffff" backgroundColor="{0}" zPosition="2">
		<convert type="ClockToText">Default</convert>
	</widget>
	<eLabel name="" position="30,30" size="1165,1020" backgroundColor="#30000000" zPosition="-1" />
	<eLabel name="" position="1220,30" size="670,1020" backgroundColor="#30000000" zPosition="-1" />
	<!-- <eLabel name="" position="60,130" size="1100,2" backgroundColor="#666666" zPosition="1" /> -->
	<eLabel name="" position="60,950" size="1100,2" backgroundColor="#666666" zPosition="1" />
	<!-- <eLabel name="" position="1260,130" size="600,2" backgroundColor="#666666" zPosition="1" /> -->
	<eLabel name="" position="1260,950" size="600,2" backgroundColor="#666666" zPosition="1" />
</screen>""".format(skinColor)

selbuq_1080 = """
<screen name="selBouquets" position="center,center" size="1920,1080" title="xtraEvent" backgroundColor="transparent">
	<widget source="Title" render="Label" position="30,30" size="1165,60" font="Console; 45" foregroundColor="#ffffff" backgroundColor="{0}" transparent="0" halign="center" valign="center" />
	<widget name="list" position="60,143" size="1118,765" itemHeight="45" font="Regular;36" foregroundColor="#ffffff" scrollbarMode="showOnDemand" transparent="1" backgroundColor="#30000000" backgroundColorSelected="{0}" foregroundColorSelected="#ffffff" />
	<widget name="status" position="1260,450" size="600,45" transparent="1" font="Regular;33" foregroundColor="#92f1fc" backgroundColor="#30000000" />
	<widget name="info" position="1260,495" size="600,405" transparent="1" font="Regular;33" foregroundColor="#ffffff" backgroundColor="#30000000" halign="left" valign="top" />
	<eLabel name="red" position="60,1040" size="275,10" backgroundColor="#ef2f2f" zPosition="2" />
	<eLabel name="green" position="335,1040" size="275,10" backgroundColor="#2fef53" zPosition="2" />
	<eLabel name="yellow" position="610,1040" size="275,10" backgroundColor="#edd02f" zPosition="2" />
	<eLabel name="blue" position="885,1040" size="275,10" backgroundColor="#2fc7ed" zPosition="2" />
	<widget source="key_red" render="Label" font="Regular;26" foregroundColor="#ffffff" backgroundColor="#30000000" position="60,1010" size="275,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_green" render="Label" font="Regular;26" foregroundColor="#ffffff" backgroundColor="#30000000" position="335,1010" size="275,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_yellow" render="Label" font="Regular;26" foregroundColor="#ffffff" backgroundColor="#30000000" position="611,1010" size="275,30" halign="center" transparent="1" zPosition="1" />
	<widget source="key_blue" render="Label" font="Regular; 26" foregroundColor="#ffffff" backgroundColor="#30000000" position="885,1010" size="275,30" halign="center" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="1220,30" size="670,60" font="Regular; 34" valign="center" halign="center" transparent="0" foregroundColor="#ffffff" backgroundColor="{0}" zPosition="2">
		<convert type="ClockToText">Default</convert>
	</widget>
	<eLabel name="" position="30,30" size="1165,1020" backgroundColor="#30000000" zPosition="-1" />
	<eLabel name="" position="1220,30" size="670,1020" backgroundColor="#30000000" zPosition="-1" />
	<!-- <eLabel name="" position="60,130" size="1100,2" backgroundColor="#666666" zPosition="1" /> -->
	<eLabel name="" position="60,950" size="1100,2" backgroundColor="#666666" zPosition="1" />
	<!-- <eLabel name="" position="1260,130" size="600,2" backgroundColor="#666666" zPosition="1" /> -->
	<!-- <eLabel name="" position="1260,840" size="600,2" backgroundColor="#666666" zPosition="1" /> -->
	<eLabel name="" position="1260,950" size="600,2" backgroundColor="#666666" zPosition="1" />
</screen>""".format(skinColor)


xtra_1080_2 = """
<screen name="xtra" position="0,0" size="1920,1080" title="xtraEvent..." flags="wfNoBorder">
	<ePixmap position="0,0" size="1920,1080" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/xtra_fhd3.png" transparent="1" />
	<widget source="Title" render="Label" position="60,53" size="1118,60" font="Console; 45" foregroundColor="#c5c5c5" backgroundColor="#23262e" transparent="1" />
	<widget name="config" position="60,143" size="1118,765" itemHeight="45" font="Regular;36" foregroundColor="#c5c5c5" scrollbarMode="showOnDemand" transparent="1" backgroundColor="#23262e" backgroundColorSelected="#0d71aa" foregroundColorSelected="#ffffff" />
	<widget source="help" position="1260,850" size="600,60" render="Label" font="Regular;28" foregroundColor="#f3fc92" backgroundColor="#23262e" halign="left" valign="center" transparent="1" />
	<widget name="status" position="1260,450" size="600,45" transparent="1" font="Regular;33" foregroundColor="#92f1fc" backgroundColor="#23262e" />
	<widget name="info" position="1260,495" size="600,390" transparent="1" font="Regular;33" foregroundColor="#c5c5c5" backgroundColor="#23262e" halign="left" valign="top" />
	<widget name="int_statu" position="1819,55" size="40,40" transparent="1" text="●" font="Regular; 36" foregroundColor="#1edb76" backgroundColor="#23262e" zPosition="2" halign="center" />
	<widget source="key_red" render="Label" font="Regular;33" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="68,960" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget source="key_green" render="Label" font="Regular;33" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="353,960" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget source="key_yellow" render="Label" font="Regular;33" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="638,960" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget source="key_blue" render="Label" font="Regular; 30" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="923,960" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="1259,60" size="600,45" font="Console; 38" valign="center" halign="center" transparent="1" foregroundColor="#c5c5c5" backgroundColor="#23262e" zPosition="1">
		<convert type="ClockToText">Default</convert>
	</widget>
	<eLabel name="" text=" MENU" position="1235,960" size="150,45" transparent="1" halign="center" font="Console; 30" />
	<eLabel name="" text=" INFO" position="1735,960" size="150,45" transparent="1" halign="center" font="Console; 30" />
</screen>"""

download_1080_2 = """
<screen name="downloads" position="0,0" size="1920,1080" title="downloads..." flags="wfNoBorder" backgroundColor="transparent">
	<ePixmap position="0,0" size="1920,1080" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/xtra_fhd3.png" zPosition="-1" transparent="1" />
	<widget source="Title" render="Label" position="60,53" size="1118,60" font="Console; 45" foregroundColor="#c5c5c5" backgroundColor="#23262e" transparent="1" />
	<widget name="progress" position="60,148" size="1100,20" foregroundColor="#ffffff" borderColor="#ffffff" borderWidth="1" backgroundColor="#23262e" />
	<widget name="status" position="60,190" size="1100,44" transparent="1" font="Regular;33" foregroundColor="#92f1fc" backgroundColor="#23262e" />
	<widget name="info" position="60,270" size="1100,44" transparent="1" font="Regular;33" foregroundColor="#c5c5c5" backgroundColor="#23262e" valign="top" />
	<widget name="info2" position="60,350" size="1100,600" transparent="1" font="Regular; 33" foregroundColor="#ffffff" backgroundColor="#23262e" />
	<widget source="key_red" render="Label" font="Regular;33" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="68,960" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget source="key_green" render="Label" font="Regular;33" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="353,960" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget source="key_yellow" render="Label" font="Regular;33" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="638,960" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget source="key_blue" render="Label" font="Regular; 30" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="923,960" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget source="global.CurrentTime" render="Label" position="1259,60" size="600,45" font="Console; 38" transparent="1" foregroundColor="#c5c5c5" backgroundColor="#23262e" zPosition="2">
		<convert type="ClockToText">Default</convert>
	</widget>

</screen>"""

manuel_1080_2 = """
<screen name="manuelSearch" position="center,center" size="1920,1080" title="Manuel Search..." backgroundColor="#000000" flags="wfNoBorder">
	<ePixmap position="0,0" size="1920,1080" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/xtra_fhd3.png" transparent="1" />
	<widget source="Title" render="Label" position="60,60" size="1118,60" font="Regular; 45" foregroundColor="#ffffff" backgroundColor="#23262e" transparent="1" />
	<widget source="session.CurrentService" render="Label" position="60,120" size="957,60" zPosition="2" font="Regular; 45" transparent="1" backgroundColor="#23262e" valign="center">
		<convert type="ServiceName">Name</convert>
	</widget>
	<widget name="config" position="60,225" size="1118,588" itemHeight="45" font="Regular;36" foregroundColor="#ffffff" scrollbarMode="showOnDemand" transparent="1" backgroundColor="#23262e" backgroundColorSelected="#0d71aa" foregroundColorSelected="#ffffff" />
	<widget name="status" position="60,885" size="1118,40" transparent="1" font="Regular;36" foregroundColor="#92f1fc" backgroundColor="#23262e" />
	<widget name="info" position="1260,960" size="600,45" transparent="1" font="Regular;33" halign="center" foregroundColor="#ffffff" backgroundColor="#23262e" />
	<widget name="Picture" position="1260,480" size="278,417" zPosition="5" transparent="1" />
	<widget name="progress" position="60,840" size="1118,20" foregroundColor="#ffffff" borderColor="#ffffff" borderWidth="1"  backgroundColor="#23262e" />
	<widget source="key_red" render="Label" font="Regular;33" foregroundColor="#ffffff" backgroundColor="#23262e" position="60,960" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget source="key_green" render="Label" font="Regular;33" foregroundColor="#ffffff" backgroundColor="#23262e" position="345,960" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget source="key_yellow" render="Label" font="Regular;33" foregroundColor="#ffffff" backgroundColor="#23262e" position="630,960" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget source="key_blue" render="Label" font="Regular;33" foregroundColor="#ffffff" backgroundColor="#23262e" position="915,960" size="255,45" halign="left" transparent="1" zPosition="1" />
	<eLabel name="" position="60,180" size="1118, 2" backgroundColor="#898989" />
</screen>"""

selbuq_1080_2 = """
<screen name="selBouquets" position="center,center" size="1920,1080" title="xtraEvent v1" backgroundColor="#ffffff">
	<ePixmap position="0,0" size="1920,1080" zPosition="-1" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/xtraEvent/pic/xtra_fhd3.png" transparent="1" />
	<widget source="Title" render="Label" position="60,53" size="1118,60" font="Regular; 45" foregroundColor="#c5c5c5" backgroundColor="#23262e" transparent="1" />
	<widget name="list" position="60,143" size="1118,765" itemHeight="45" font="Regular;36" foregroundColor="#c5c5c5" scrollbarMode="showOnDemand" transparent="1" backgroundColor="#23262e" backgroundColorSelected="#0d71aa" foregroundColorSelected="#ffffff" />
	<widget name="status" position="1260,450" size="600,45" transparent="1" font="Regular;33" foregroundColor="#92f1fc" backgroundColor="#23262e" />
	<widget name="info" position="1260,495" size="600,405" transparent="1" font="Regular;33" foregroundColor="#c5c5c5" backgroundColor="#23262e" halign="left" valign="top" />
	<widget source="key_red" render="Label" font="Regular;33" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="60,960" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget source="key_green" render="Label" font="Regular;33" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="345,960" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget source="key_yellow" render="Label" font="Regular;33" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="630,960" size="255,45" halign="left" transparent="1" zPosition="1" />
	<widget source="key_blue" render="Label" font="Regular;33" foregroundColor="#c5c5c5" backgroundColor="#23262e" position="915,960" size="255,45" halign="left" transparent="1" zPosition="1" />
	<eLabel name="" text="v1" position="1260, 53" size="600, 60" transparent="1" halign="center" font="Regular; 45" backgroundColor="#0023262e" />
</screen>"""



