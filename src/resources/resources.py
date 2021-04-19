"""Class to manage the config"""


import yaml
import re
from colorama import init, Fore
from typing import Callable, Dict, Any
from cli.log import warning
from os import path


init(autoreset=True)


config_path = path.join(path.expanduser('~'), '.thmctrl.yaml')
default_config = {'profiles': {}}


class Resource:
    def __init__(self: Callable) -> Callable:
        self._verificate()

    def _verificate(self: Callable):
        if not path.isfile(config_path):
            open(config_path, 'x')

            with open(config_path, 'w') as conf:
                yaml.dump(default_config, conf)
                warning('Created missing resource: ' + config_path)

    def get(self: Callable, key: str) -> Any:
        with open(config_path, 'r') as conf:
            config = yaml.load(conf, Loader=yaml.FullLoader)

        return config[key]

    def fetch(self: Callable) -> Dict[Any, Any]:
        with open(config_path, 'r') as conf:
            config = yaml.load(conf, Loader=yaml.FullLoader)

        return config

    def write(self: Callable, to_write: Dict[Any, Any]) -> bool:
        with open(config_path, 'w') as conf:
            yaml.dump(to_write, conf)
        
        return True


class Util:
    def get_type(self: Callable, to_check: Any) -> str:
        raw_type: str = str(type(to_check))
        regex = r'^\<class \'(.*)\'\>'
        the_type = re.findall(regex, raw_type)[0]
        return the_type

    def display_list(self: Callable, lst: list[Any]):
        if not len(lst) == 0:
            for item in lst:
                print(Fore.BLUE + '  => ' + Fore.RESET + item)

    def pretty(self: Callable, dct: Dict[Any, Any], indent: int=0):
        for key, value in dct.items():
            print('  ' * indent + Fore.BLUE + str(key) + Fore.RESET + ':')
            
            if isinstance(value, dict):
                if len(value) != 0:
                    self.pretty(value, indent + 1)
                else:
                    print('  ' * (indent + 1) + Fore.MAGENTA + 'Empty')
            else:
                print('  ' * (indent + 1) + Fore.GREEN + str(value))

    def syntaxer(self: Callable, content: str) -> str:
        content = content.replace('=', Fore.YELLOW + '=' + Fore.GREEN)
        content = content.replace('"', Fore.GREEN + '"')
        content = content.replace('\n', Fore.RESET + '\n')
        return content
