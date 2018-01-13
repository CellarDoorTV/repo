################################################################################
#      Copyright (C) 2015 OpenELEQ   Modded by FTG                             #
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

import os, re, shutil, time, xbmc, xbmcaddon, thread
try:
	import json as simplejson 
except:
	import simplejson

ADDON_ID = 'script.skinswitch'
HOME             = xbmc.translatePath('special://home/')
ADDONS           = os.path.join(HOME,      'addons')
USERDATA         = os.path.join(HOME,      'userdata')
PLUGIN           = os.path.join(ADDONS,    ADDON_ID)
ICON             = os.path.join(PLUGIN,    'icon.png')
#####################################################################
def currSkin():
	return xbmc.getSkinDir()

def swapSkins(skin, title="Error"):
	old = 'lookandfeel.skin'
	value = skin
	current = getOld(old)
	new = old
	setNew(new, value)
	x = 0
	while not xbmc.getCondVisibility("Window.isVisible(yesnodialog)") and x < 100:
		x += 1
		xbmc.sleep(100)
	if xbmc.getCondVisibility("Window.isVisible(yesnodialog)"):
		xbmc.executebuiltin('SendClick(11)')
	else: LogNotify("[COLOR yellow]Skin Swap[/COLOR]", '[COLOR red]%s: Skin Swap Timed Out![/COLOR]' % (title)); return False
	return True

def getOld(old):
	try:
		old = '"%s"' % old 
		query = '{"jsonrpc":"2.0", "method":"Settings.GetSettingValue","params":{"setting":%s}, "id":1}' % (old)
		response = xbmc.executeJSONRPC(query)
		response = simplejson.loads(response)
		if response.has_key('result'):
			if response['result'].has_key('value'):
				return response ['result']['value'] 
	except:
		pass
	return None

def setNew(new, value):
	try:
		new = '"%s"' % new
		value = '"%s"' % value
		query = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue","params":{"setting":%s,"value":%s}, "id":1}' % (new, value)
		response = xbmc.executeJSONRPC(query)
	except:
		pass
	return None

def ebi(proc):
	xbmc.executebuiltin(proc)

def refresh():
	ebi('Container.Refresh()')

def LogNotify(title,message,times=2000,icon=ICON):
	ebi('XBMC.Notification(%s, %s, %s, %s)' % (title, message, times, icon))

def addonId(add):
	try: 
		return xbmcaddon.Addon(id=add)
	except:
		return False