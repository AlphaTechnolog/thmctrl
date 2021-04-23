"""Class to manage the config"""


import yaml
import re
from colorama import init, Fore
from typing import Callable, Dict, Any, List
from cli.log import warning
from os import path


init(autoreset=True)


config_path = path.join(path.expanduser('~'), '.thmctrl.yaml')
default_config = {'profiles': {}}
meta_path = path.join(path.expanduser('~'), '.thmctrl.meta.yaml')
default_meta = {'used_theme': None}


class Resource:
    def __init__(self: Callable) -> Callable:
        self._verificate()

    def _verificate__create_default_file(self: Callable, pth: str, default: Dict[str, Any]) -> bool:
        if not path.isfile(pth):
            open(pth, 'x')

            with open(pth, 'w') as file:
                yaml.dump(default, file)
                return True

        return False

    def _verificate(self: Callable):
        self._verificate__config()
        self._verificate__meta()

    def _verificate__meta(self: Callable):
        ok = self._verificate__create_default_file(
            pth=meta_path,
            default=default_meta
        )

        if ok:
            warning('Created missing meta information resource: ' + meta_path)

    def _verificate__config(self: Callable):
        ok = self._verificate__create_default_file(
            pth=config_path,
            default=default_config
        )

        if ok:
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

    def display_list(self: Callable, lst: List[Any]):
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


class Meta:
    def __init__(self: Callable) -> Callable:
        self.meta_path = meta_path

    def fetch(self: Callable) -> Dict[str, Any]:
        with open(self.meta_path, 'r') as meta:
            return yaml.load(meta, Loader=yaml.FullLoader)

    def write(self: Callable, data: Dict[str, Any]) -> bool:
        try:
            with open(self.meta_path, 'w') as meta:
                yaml.dump(data, meta)
                return True
        except:
            return False
