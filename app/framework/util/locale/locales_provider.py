import json
from .localization import *

localization = Localization()
def lang(key: str, **kwargs):
    loclaes = localization.get_current_locales()


