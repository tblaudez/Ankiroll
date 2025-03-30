"""
Handles add-on configuration
"""

from aqt import mw

from .libaddon.anki.configmanager import ConfigManager

config = ConfigManager(mw)