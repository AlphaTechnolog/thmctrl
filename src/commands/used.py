from resources.resources import Meta, Util
from cli.log import info, error
from typing import Callable, Any, Dict


class UsedCommand:
    meta: Meta = Meta()
    util: Util = Util()

    def __init__(self: Callable, args: Dict[str, Any]) -> Callable:
        self.args = args
        self.used_theme = self.meta.fetch()['used_theme']

        if self.used_theme is None:
            error('No theme used')

        self.profile_name = self.used_theme['profile']
        self.used_theme[self.profile_name] = self.used_theme['raw_profile']
        del self.used_theme['raw_profile']
        del self.used_theme['profile']
        self.show_used()

    def _show_used__compact(self: Callable):
        info(f'Used theme: "{self.profile_name}"')

    def _show_used__complete(self: Callable):
        self.util.pretty(self.used_theme)

    def show_used(self: Callable):
        if self.args['compact']:
            self._show_used__compact()
        else:
            self._show_used__complete()
