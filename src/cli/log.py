"""Tools to print messages."""


from colorama import init, Fore
from typing import Callable, Dict, Any


init(autoreset=True)


class BaseMessage:
    def __init__(self: Callable, **options: Dict[str, Any]) -> Callable:
        self._options = options

    def log(self: Callable):
        print(self._options['color'] + f'=> {self._options["prefix"]} ' + Fore.RESET + self._options['message'])

        if self._options['exit']['val']:
            exit(self._options['exit']['status_code'])


def success(message: str):
    options = {
        'color': Fore.GREEN,
        'message': message,
        'prefix': '[SUCCESS]',
        'exit': {
            'val': False,
            'status_code': 0
        }
    }

    messager: BaseMessage = BaseMessage(**options)
    messager.log()


def error(message: str):
    options = {
        'color': Fore.RED,
        'message': message,
        'prefix': '[  ERR  ]',
        'exit': {
            'val': True,
            'status_code': 1
        }
    }

    messager: BaseMessage = BaseMessage(**options)
    messager.log()


def warning(message: str):
    options = {
        'color': Fore.YELLOW,
        'message': message,
        'prefix': '[WARNING]',
        'exit': {
            'val': False,
            'status_code': 0
        }
    }

    messager: BaseMessage = BaseMessage(**options)
    messager.log()

def info(message: str):
    options = {
        'color': Fore.BLUE,
        'message': message,
        'prefix': '[  INF  ]',
        'exit': {
            'val': False,
            'status_code': 0
        }
    }

    messager: BaseMessage = BaseMessage(**options)
    messager.log()