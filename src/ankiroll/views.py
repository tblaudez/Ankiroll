from aqt.gui_hooks import card_will_show

from .rickroll import AnkiRoll


def initialize_views(ankiroll: AnkiRoll):
    card_will_show.append(ankiroll.maybe_show_rickroll)