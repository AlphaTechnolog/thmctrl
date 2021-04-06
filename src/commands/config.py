from typing import Dict, Any, Callable
from resources.resources import Resource, Util, Dict, Any
from cli.log import error, success, info


class ConfigCommand:
    config_resource: Resource = Resource()

    def __init__(self: Callable, args: Dict[Any, Any]) -> Callable:
        self._args = args
        
        if self._args['get']:
            self._get_config()

        if self._args['fetch']:
            profile_data = self._fetch(self._args['fetch'])
            util: Util = Util()
            util.pretty(profile_data)

    def _fetch(self: Callable, name: str) -> Dict[str, Any]:
        if not name in self.config_resource.get('profiles'):
            error('The requested name doesn\'t exists')
        
        profiles: list[Dict[str, Any]] = self.config_resource.get('profiles')
        profile: Dict[str, Any] = profiles[name]
        data: Dict[str, Any] = dict()
        data[name] = profile
        return data

    def _get_config(self: Callable):
        config = self.config_resource.fetch()

        if len(config) == 0:
            error('Config doesn\'t have data')

        util: Util = Util()
        util.pretty(config)