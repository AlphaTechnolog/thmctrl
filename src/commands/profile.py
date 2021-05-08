import json
import re
from colorama import init, Fore
from os import getenv
from os import path
from os import system as exe
from typing import Callable, Dict, Any
from resources.resources import Resource, Util, Meta
from cli.log import error, info, success, warning


init(autoreset=True)
qtile_path = path.join(path.expanduser('~'), '.config', 'qtile', 'config.json')


class ProfileCommand:
    config_resource: Resource = Resource()
    meta_resource: Meta = Meta()
    util: Util = Util()

    def __init__(self: Callable, args: Dict[Any, Any]) -> Callable:
        self._args = args
        self._name = self._args['name']
        self._dispatch = self._args['dispatch']
        self._get = self._args["get"]
        self._to_get = self._get != "no_get"

        self._verificate(self._name)

        if not self._to_get:
            self.dispatch(self._dispatch)
        else:
            self.get(self._get)

    def _verificate(self: Callable, name: str):
        if not name in self.config_resource.get('profiles'):
            error('The requested name doesn\'t exists in config file')

    def _get__modes(self: Callable):
        return {
            "compact": lambda profile: info(f"Profile name: {self._args['name']}"),
            "full": lambda profile: self.util.pretty(profile)
        }

    def get(self: Callable, mode: str):
        profile: Dict[str, Any] = self.config_resource.get("profiles")[self._args["name"]]
        self._get__modes()[mode](profile)

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

    def _dispatch__gtk(self: Callable, profile: Dict[str, Any]):
        gtkrc_2_0_path = path.join(path.expanduser('~'), '.gtkrc-2.0')

        gtkrc_3_0_path = path.join(
            path.expanduser('~'),
            '.config', 'gtk-3.0',
            'settings.ini'
        )

        to_validate = [
            {
                'name': gtkrc_2_0_path,
                'initial': '\n'.join([
                    'gtk-theme-name="Adwaita"',
                    'gtk-icon-theme-name="Adwaita"',
                    'gtk-cursor-theme-name="Adwaita"'
                ])
            },
            {
                'name': gtkrc_3_0_path,
                'initial': '\n'.join([
                    '[Settings]',
                    'gtk-theme-name=Adwaita',
                    'gtk-icon-theme-name=Adwaita',
                    'gtk-cursor-theme-name=Adwaita'
                ])
            }
        ]

        for item in to_validate:
            if not path.isfile(item['name']):
                warning(f"Writing a default: `{item['name']}`")
                print(self.util.syntaxer(item['initial']))
                open(item['name'], 'x')

                with open(item['name'], 'w') as raw_file:
                    raw_file.write(item['initial'])

        info('Changing gtk 2 theme')

        gtkrc_2_0 = open(gtkrc_2_0_path, 'r')
        gtkrc_2_0_content = gtkrc_2_0.read()
        gtkrc_2_0.close()
        gtkrc_2_0 = open(gtkrc_2_0_path, 'w')

        gtkrc_2_0_content = re.sub(
            r'gtk-theme-name=".*"',
            'gtk-theme-name="' + profile['gtk']['theme'] + '"',
            gtkrc_2_0_content
        )

        gtkrc_2_0_content = re.sub(
            r'gtk-icon-theme-name=".*"',
            'gtk-icon-theme-name="' + profile['gtk']['icon'] + '"',
            gtkrc_2_0_content
        )

        gtkrc_2_0_content = re.sub(
            r'gtk-cursor-theme-name=".*"',
            'gtk-cursor-theme-name="' + profile['gtk']['cursor'] + '"',
            gtkrc_2_0_content
        )

        gtkrc_2_0.write(gtkrc_2_0_content)
        success('Changed the gtk 2 theme')
        info('Content:')
        print(self.util.syntaxer(gtkrc_2_0_content).rstrip())

        info('Changing gtk 3 theme')
        gtkrc_3_0 = open(gtkrc_3_0_path, 'r')
        gtkrc_3_0_content = gtkrc_3_0.read()
        gtkrc_3_0.close()
        gtkrc_3_0 = open(gtkrc_3_0_path, 'w')

        gtkrc_3_0_content = re.sub(
            r'gtk-theme-name=.*',
            'gtk-theme-name=' + profile['gtk']['theme'],
            gtkrc_3_0_content
        )

        gtkrc_3_0_content = re.sub(
            r'gtk-icon-theme-name=.*',
            'gtk-icon-theme-name=' + profile['gtk']['icon'],
            gtkrc_3_0_content
        )

        gtkrc_3_0_content = re.sub(
            r'gtk-cursor-theme-name=.*',
            'gtk-cursor-theme-name=' + profile['gtk']['cursor'],
            gtkrc_3_0_content
        )

        gtkrc_3_0.write(gtkrc_3_0_content)
        success('Changed gtk 3 theme')
        info('Content:')
        print(self.util.syntaxer(gtkrc_3_0_content).rstrip())

    def _dispatch__shell(shell: Callable, profile: Dict[str, Any]):
        shell = profile['shell']['executable']
        user = getenv('USER')
        info(f'Changing default shell for user {user}, to shell: {shell}')
        cmd = f'sudo usermod --shell {shell} {user}'
        warning('If the password is prompted please write it')
        info(f'> {cmd}')
        exe(cmd)
        success('Changed shell successfully')

        try:
            init_command = profile['shell']['init']
            info('Executing the first command for the shell')
            cmd = f'{shell} -c "{init_command}"'
            info(f'> {cmd}')
            exe(cmd)
            success('Executed command successfully')
        except KeyError:
            pass

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
            self._dispatch__gtk(profile)
            self._dispatch__shell(profile)

        if to_dispatch == 'pycritty':
            self._dispatch__pycritty(profile)

        if to_dispatch == 'wallc':
            self._dispatch__wallc(profile)

        if to_dispatch == 'qtile':
            self._dispatch__qtile(profile)

        if to_dispatch == 'gtk':
            self._dispatch__gtk(profile)
        
        if to_dispatch == 'shell':
            self._dispatch__shell(profile)

        info('Updating meta information...')

        updated: bool = self.meta_resource.write({'used_theme': {
            'profile': name,
            'raw_profile': profile
        }})
        if updated is False:
            error('Unexpected error at update the meta information')

        success('Update meta information successfully')
