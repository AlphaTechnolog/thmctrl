from resources.resources import Util, Resource
from typing import Callable, Dict, Any
from cli.log import error
from colorama import init, Fore


init(autoreset=True)


class ProfilesCommand:
    config_resource: Resource = Resource()
    util: Util = Util()

    def __init__(self: Callable, args: Dict[Any, Any]) -> Callable:
        self._args = args

        if self._args['available']:
            availables = self._get_profiles_list()

            if len(availables) == 0:
                error('No profiles created, please create one using config create command')
            else:
                print(Fore.YELLOW + 'Showing available profiles')

            self.util.display_list(availables)

    def _get_profiles_list(self: Callable) -> list[str]:
        profiles: Dict[str, Any] = self.config_resource.get('profiles')
        return list(profiles.keys())