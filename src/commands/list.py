from commands.config import ConfigCommand
from commands.config_create import ConfigCreateCommand
from commands.profile import ProfileCommand
from commands.profiles import ProfilesCommand
from commands.used import UsedCommand


commands_list = {
    'config': ConfigCommand,
    'config_create': ConfigCreateCommand,
    'profile': ProfileCommand,
    'profiles': ProfilesCommand,
    'used': UsedCommand
}
