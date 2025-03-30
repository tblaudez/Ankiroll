from random import random
from typing import TYPE_CHECKING

from .consts import ADDON

if TYPE_CHECKING:
    from aqt.main import AnkiQt

from .libaddon.anki.configmanager import ConfigManager


class AnkiRoll:
    RICKROLL_FILE = "assets/rickroll.gif"

    def __init__(self, mw: "AnkiQt", config: ConfigManager):
        self._mw = mw
        self._config = config

    def maybe_show_rickroll(self, html, _card, context):
        if (context != "reviewAnswer") or (random() > self._config["local"]["probability"]):
            return html

        addon_package = self._mw.addonManager.addonFromModule(ADDON.MODULE)
        file_path = f"/_addons/{addon_package}/{self.RICKROLL_FILE}"

        return f"""
            <div id="new-html" style="text-align: center;">
                <img src="{file_path}" style="height: 80vh;">
                <br>
                <button id="show-real-answer" style="margin-top:10px; padding:10px; font-size:16px;">
                    Never Gonna Give You Up !
                </button>
            </div>
            <div id="old-html" style="visibility: hidden;">
            {html}
            </div>
            <script>
                document.getElementById("show-real-answer").onclick = function() {{
                    document.getElementById("new-html").remove();
                    document.getElementById("old-html").style.visibility = "visible";
                }};
            </script>
            """