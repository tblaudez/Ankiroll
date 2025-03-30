"""
Addon-wide constants
"""

from ._version import __version__

__all__ = ["ADDON"]

# PROPERTIES DESCRIBING ADDON

class ADDON:
    """Class storing general add-on properties
    Property names need to be all-uppercase with no leading underscores
    """

    NAME = "Ankiroll"
    MODULE = "ankiroll"
    ID = "597778000"
    VERSION = __version__
    LICENSE = "GNU AGPLv3"
    AUTHORS = (
        {
            "name": "Tristan Blaudez (tblaudez)",
            "years": "2025",
            "contact": "https://github.com/tblaudez",
        },
    )
    AUTHOR_MAIL = "tristan.urbainblaudez@yahoo.com"
    LIBRARIES = ()
    CONTRIBUTORS = ("glutanimate", "marvinruder",)
    SPONSORS = ()
    LINKS = {
        "patreon": "",
        "bepatron": "",
        "coffee": "",
        "description": "https://ankiweb.net/shared/info/{}".format(ID),
        "rate": "https://ankiweb.net/shared/review/{}".format(ID),
        "twitter": "",
        "youtube": "",
        "help": "",
    }