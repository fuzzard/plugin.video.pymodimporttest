# -*- coding: utf-8 -*-

import routing
import logging
import requests
import re
import urllib
import xbmcaddon
from sys import exit, version_info
from resources.lib import kodiutils
from resources.lib import kodilogging
from xbmcgui import ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory, setResolvedUrl


if kodiutils.PY3:
    from urllib.parse import urlencode
else:
    from urllib import urlencode


ADDON = xbmcaddon.Addon()
ICON = ADDON.getAddonInfo("icon")
logger = logging.getLogger(ADDON.getAddonInfo('id'))
kodilogging.config()
plugin = routing.Plugin()

@plugin.route('/')
def index():

    try:
        print("Import: Attempting Cryptodome")
        from Cryptodome.Cipher import AES
    except ImportError:
        print("FAILED! Import: Cryptodome failed")

    try:
        print("Import: Attempting Pillow")
        from PIL import Image
    except ImportError:
        print("FAILED! Import: Pillow failed")

    try:
        print("Import: Attempting numpy")
        import numpy as np
    except ImportError:
        print("FAILED! Import: numpy failed")

    try:
        print("Import: Attempting lxml")
        from lxml import etree as lxmlet
    except ImportError:
        print("FAILED! Import: lxml failed")

    try:
        print("Import: Attempting bz2")
        import bz2
    except ImportError:
        print("FAILED! Import: BZ2 failed")
    
    try:
        print("Import: Attempting ElementTree")
        import xml.etree.ElementTree
    except ImportError:
        print("FAILED! Import: ElementTree failed")
    
    try:
        print("Import: Attempting json")
        import json
    except ImportError:
        print("FAILED! Import: json failed")

    try:
        print("Import: Attempting pwd")
        import pwd
    except ImportError:
        print("FAILED! Import: pwd failed")

    try:
        print("Import: Attempting math")
        import math
    except ImportError:
        print("FAILED! Import: math failed")

    try:
        print("Import: Attempting csv")
        import csv
    except ImportError:
        print("FAILED! Import: csv failed")

    try:
        print("Import: Attempting zlib")
        import zlib
    except ImportError:
        print("FAILED! Import: zlib failed")

    try:
        print("Import: Attempting socket")
        import socket
    except ImportError:
        print("FAILED! Import: socket failed")


def raise_notification():
    kodiutils.ok(kodiutils.get_string(32000),kodiutils.get_string(32002))
    exit(0)


def run():
    plugin.run()
