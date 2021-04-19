from typing import Callable, Dict, Any
from resources.resources import Resource
from cli.log import error, info, success


class ConfigCreateCommand:
    def __init__(self: Callable, args: Dict[Any, Any]) -> Callable:
        self._args = args
        self._config = Resource()

        if args['name'] in self._config.get('profiles'):
            error(args['name'] + ' already exists in profiles')

        info('Validating shell')
        ok = self._validate__shell(self._args['shell'])
        
        if not ok:
            error('Invalid shell it isn\'t in /etc/shells')
        
        success('Valid shell')
        info('Generating the object to save in your config')

        data = {
            'qtile': {
                'theme': args['qtile_theme']
            },
            'gtk': {
                'theme': args['gtk_theme'],
                'icon': args['gtk_icon'],
                'cursor': args['gtk_cursor'],
            },
            'shell': {
                'executable': args['shell']
            },
            'pycritty': {
                'theme': args['pycritty_theme'],
                'opacity': args['pycritty_opacity'],
                'font': args['pycritty_font'],
                'size': args['pycritty_size'],
                'padding': {
                    'x': args['pycritty_padding_x'],
                    'y': args['pycritty_padding_y']
                },
            },
            'wallc': {
                'wallpaper': args['wallc_wallpaper_name'],
                'extension': args['wallc_wallpaper_extension']
            }
        }

        if args['shell_init']:
            data['shell']['init'] = args['shell_init']

        success('Object generated successfully')
        info('Writing config')
        self._to_write_config = self._config.fetch()
        self._to_write_config['profiles'][args['name']] = data
        self._config.write(self._to_write_config)
        success('Config writed successfully')

    def _validate__shell(self: Callable, shell: str) -> bool:
        with open('/etc/shells', 'r') as fshells:
            shells = fshells.read().split('\n')
            return shell in shells