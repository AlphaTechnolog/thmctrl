from typing import Callable, Dict, Any
from resources.resources import Resource
from cli.log import error, info, success


class ConfigCreateCommand:
    def __init__(self: Callable, args: Dict[Any, Any]) -> Callable:
        self._args = args
        self._config = Resource()

        if args['name'] in self._config.get('profiles'):
            error(args['name'] + ' already exists in profiles')

        info('Generating the object to save in your config')

        data = {
            'qtile': {
                'theme': args['qtile_theme']
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

        success('Object generated successfully')
        info('Writing config')
        self._to_write_config = self._config.fetch()
        self._to_write_config['profiles'][args['name']] = data
        self._config.write(self._to_write_config)
        success('Config writed successfully')