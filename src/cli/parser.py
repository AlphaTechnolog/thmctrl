import argparse
from defs import __version__
from resources.resources import config_path


parser = argparse.ArgumentParser(
    prog='thmctrl',
    description='Manage my dotfiles config - AlphaTechnology',
    epilog=f'Config file path: "{config_path}"'
)


parser.add_argument(
    '-V', '--version',
    action='version', version=__version__
)


subparsers = parser.add_subparsers(title='subcommands')


config_parser = subparsers.add_parser('config', help='Manage config')
config_parser.set_defaults(action='config')


config_parser.add_argument(
    '-G', '--get',
    action='store_true'
)


config_parser.add_argument(
    '-F', '--fetch',
    required=False, help='Fetch by profile name'
)


config_subparsers = config_parser.add_subparsers(title='config subcommands')
config_subparser_create = config_subparsers.add_parser('create', help='Create profile')
config_subparser_create.set_defaults(action='config_create')
config_subparser_create.add_argument('name', help='The profile name')


config_subparser_create.add_argument(
    '-pt', '--pycritty-theme',
    required=True, help='The pycritty theme name'
)


config_subparser_create.add_argument(
    '-po', '--pycritty-opacity',
    required=True, help='The pycritty opacity'
)


config_subparser_create.add_argument(
    '-pf', '--pycritty-font',
    required=True, help='The pycritty font'
)


config_subparser_create.add_argument(
    '-ps', '--pycritty-size',
    required=True, help='The pycritty font size'
)


config_subparser_create.add_argument(
    '-ppx', '--pycritty-padding-x',
    required=True, help='The x of pycritty padding'
)


config_subparser_create.add_argument(
    '-ppy', '--pycritty-padding-y',
    required=True, help='The y of pycritty padding'
)


config_subparser_create.add_argument(
    '-qt', '--qtile-theme',
    required=True, help='The qtile theme name'
)


config_subparser_create.add_argument(
    '-wn', '--wallc-wallpaper-name',
    required=True, help='The wallc wallpaper name'
)


config_subparser_create.add_argument(
    '-we', '--wallc-wallpaper-extension',
    required=False, default='jpg',
    help='The wallc wallpaper extension (default: jpg)'
)


config_subparser_create.add_argument(
    '-gtk', '--gtk-theme',
    required=True, help='The gtk theme'
)


config_subparser_create.add_argument(
    '--gtk-icon',
    required=True, help='The gtk icons'
)


config_subparser_create.add_argument(
    '--gtk-cursor',
    required=True, help='The gtk cursor'
)


config_subparser_create.add_argument(
    '-S', '--shell',
    required=True, help='The shell executable (required in /etc/shells)'
)


config_subparser_create.add_argument(
    '-Si', '--shell-init',
    required=False, help='The first shell argument (used to change a shell theme)'
)


profile_parser = subparsers.add_parser('profile', help='Dispatch profile')
profile_parser.set_defaults(action='profile')


profile_parser.add_argument('name', help='The name of profile to dispatch')


profile_parser.add_argument(
    '-S', '--dispatch',
    required=False, type=str,
    help='The dispatch options',
    choices=('all', 'pycritty', 'wallc', 'qtile', 'gtk', 'shell'),
    default='all'
)


profiles_parser = subparsers.add_parser('profiles', help='Manage the profiles.')
profiles_parser.set_defaults(action='profiles')


profiles_parser.add_argument(
    '-A', '--available',
    action='store_true',
    help='List all available profiles'
)


used_parser = subparsers.add_parser('used', help='Show the used theme')
used_parser.set_defaults(action='used')
used_parser.add_argument('-C', '--compact', action='store_true')
