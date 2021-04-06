import json
from os import path
from os import system as exe
from typing import Callable, Dict, Any
from resources.resources import Resource, Util
from cli.log import error, info, success


qtile_path = path.join(path.expanduser('~'), '.config', 'qtile', 'config.json')


class ProfileCommand:
    config_resource: Resource = Resource()
    util: Util = Util()

    def __init__(self: Callable, args: Dict[Any, Any]) -> Callable:
        self._args = args
        self._name = self._args['name']
        self._dispatch = self._args['dispatch']
        self._verificate(self._name)
        self.dispatch(self._dispatch)

    def _verificate(self: Callable, name: str):
        if not name in self.config_resource.get('profiles'):
            error('The requested name doesn\'t exists in config file')

    def _dispatch__pycritty(self: Callable, profile: Dict[str, Any]):
        pycritty_command = ' '.join([
            'pycritty', '-t', profile['pycritty']['theme'],
            '-o', profile['pycritty']['opacity'],
            '-p', profile['pycritty']['padding']['y'],
            profile['pycritty']['padding']['x'],
            '-s', profile['pycritty']['size'],
            '-f', profile['pycritty']['font']
        ])

        info('Dispatching pycritty command')
        info('> ' + pycritty_command)
        exe(pycritty_command)
        success('Dispatched pycritty command')

    def _dispatch__wallc(self: Callable, profile: Dict[str, Any]):
        wallc_command = ' '.join([
            'wallc', 'set', '-w',
            profile['wallc']['wallpaper'],
            '-e', profile['wallc']['extension']
        ])

        info('Dispatching wallc command')
        info('> ' + wallc_command)
        exe(wallc_command)
        success('Dispatched wallc command')

    def _dispatch__qtile(self: Callable, profile: Dict[str, Any]):
        info('Changing qtile theme')
        with open(qtile_path, 'w') as qtile_conf:
            json.dump({'theme': profile['qtile']['theme']}, qtile_conf)
            success('Changed qtile theme, Reload it!')

    def dispatch(self: Callable, to_dispatch: str):
        name = self._args['name']
        profile: Dict[str, Any] = self.config_resource.get('profiles')[name]

        if (to_dispatch != 'all'
            and not to_dispatch in profile):
            error('Invalid config file, please, provide the requested option in the config file')

        if to_dispatch == 'all':
            if (not 'pycritty' in profile
                or not 'wallc' in profile
                or not 'qtile' in profile):
                error('The data of profile is corrupted please recreate it profile')

        if to_dispatch == 'all':
            self._dispatch__pycritty(profile)
            self._dispatch__wallc(profile)
            self._dispatch__qtile(profile)

        if to_dispatch == 'pycritty':
            self._dispatch__pycritty(profile)

        if to_dispatch == 'wallc':
            self._dispatch__wallc(profile)

        if to_dispatch == 'qtile':
            self._dispatch__qtile(profile)