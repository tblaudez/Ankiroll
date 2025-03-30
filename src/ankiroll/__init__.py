from typing import TYPE_CHECKING

from aqt import mw as main_window

from ._version import __version__  # noqa: F401
from .config import config
from .consts import ADDON
from .libaddon.consts import set_addon_properties
from .rickroll import AnkiRoll
from .views import initialize_views

if TYPE_CHECKING:
    assert main_window is not None

set_addon_properties(ADDON)

ankiroll = AnkiRoll(main_window, config)
main_window._ankiroll = ankiroll  # type: ignore[attr-defined]
initialize_views(ankiroll)

main_window.addonManager.setWebExports(__name__, r"assets/.*gif")