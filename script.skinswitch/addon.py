################################################################################
#      Copyright (C) 2017 FTG                                                  #
#                                                                              #
#  This Program is free software; you can redistribute it and/or modify        #
#  it under the terms of the GNU General Public License as published by        #
#  the Free Software Foundation; either version 2, or (at your option)         #
#  any later version.                                                          #
#                                                                              #
#  This Program is distributed in the hope that it will be useful,             #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of              #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the                #
#  GNU General Public License for more details.                                #
#                                                                              #
#  You should have received a copy of the GNU General Public License           #
#  along with XBMC; see the file COPYING.  If not, write to                    #
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.       #
#  http://www.gnu.org/copyleft/gpl.html                                        #
################################################################################



import xbmc, xbmcaddon, xbmcgui, xbmcplugin,os,sys,random,urllib2,urllib
from resources.libs import skinSwitch

ADDON_ID = 'script.skinswitch'
ADDON          = skinSwitch.addonId(ADDON_ID)
ART = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID, 'resources/art'))
SKIN = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID, 'resources/art/skins'))
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID , 'resources/art/fanart.png'))
ICON = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID, 'icon.png'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + ADDON_ID, 'resources/art/icon.png'))

def MainMenu():
	addItem('arctic.zephyr.plus','url',2,icon,fanart,'')
	addItem('nebula','url',3,icon,fanart,'')
	addItem('eminence','url',4,icon,fanart,'')
	addItem('blackglassnova','url',5,icon,fanart,'')
	addItem('konfluence','url',6,icon,fanart,'')
	addItem('bello.6.nero','url',7,icon,fanart,'')
        addItem('bello.6.sonar','url',8,icon,fanart,'')
        addItem('aeonmq7','url',9,icon,fanart,'')
        addItem('aeonmq8','url',10,icon,fanart,'')
	addItem('confluence','url',11,icon,fanart,'')
	addItem('estuary','url',12,icon,fanart,'')
	addItem('xonfluence.mod','url',13,icon,fanart,'')
	addItem('explore','url',14,icon,fanart,'')
def addItem(name, url, mode, iconimage, fanart, description=None):

	if description == None: description = ''
	description = '[COLOR white]' + description + '[/COLOR]'
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
	liz.setProperty( "fanart_Image", fanart )
	liz.setProperty( "icon_Image", iconimage )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
	return ok

def get_params():
		param=[]
		paramstring=sys.argv[2]
		if len(paramstring)>=2:
				params=sys.argv[2]
				cleanedparams=params.replace('?','')
				if (params[len(params)-1]=='/'):
						params=params[0:len(params)-2]
				pairsofparams=cleanedparams.split('&')
				param={}
				for i in range(len(pairsofparams)):
						splitparams={}
						splitparams=pairsofparams[i].split('=')
						if (len(splitparams))==2:
								param[splitparams[0]]=splitparams[1]
								
		return param

params=get_params(); name=None; url=None; mode=None; iconimage=None; fanartimage=None
try: name=urllib.unquote_plus(params["name"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try: fanartimage=urllib.quote_plus(params["fanartimage"])
except: pass

if mode is None or url is None or len(url)<1: 
	MainMenu()
elif mode==2:skinSwitch.swapSkins('skin.arctic.zephyr.plus')
elif mode==3:skinSwitch.swapSkins('skin.nebula')
elif mode==4:skinSwitch.swapSkins('skin.eminence')
elif mode==5:skinSwitch.swapSkins('skin.blackglassnova')
elif mode==6:skinSwitch.swapSkins('skin.konfluence')
elif mode==7:skinSwitch.swapSkins('skin.bello.6.nero')
elif mode==8:skinSwitch.swapSkins('skin.bello.6.sonar')
elif mode==9:skinSwitch.swapSkins('skin.aeonmq7')
elif mode==10:skinSwitch.swapSkins('skin.aeonmq8')
elif mode==11:skinSwitch.swapSkins('skin.confluence')
elif mode==12:skinSwitch.swapSkins('skin.estuary')
elif mode==13:skinSwitch.swapSkins('skin.xonfluence.mod')
elif mode==14:skinSwitch.swapSkins('skin.explore')
xbmcplugin.endOfDirectory(int(sys.argv[1]))
