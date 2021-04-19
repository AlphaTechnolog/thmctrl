#!/usr/bin/env python3

from colorama import init, Fore
from cli.parser import parser
from cli.log import error
from commands.list import commands_list
from typing import Dict, Any


init(autoreset=True)


def main():
    args: Dict[Any, Any] = vars(parser.parse_args())

    if len(args) == 0:
        error('Nothing to do, use -h to get help')

    commands_list[args['action']](args)


if __name__ == '__main__':
    main()
