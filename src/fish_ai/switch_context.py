# -*- coding: utf-8 -*-

from simple_term_menu import TerminalMenu
from configparser import ConfigParser
from os import path


def switch_context():
    config = ConfigParser()
    config.read(path.expanduser('~/.config/fish-ai.ini'))
    sections = config.sections()
    sections.remove('fish-ai')
    options = [
        '{} (provided by {})'.format(section, config.get(
            section=section,
            option='provider'))
        for section in sections]
    terminal_menu = TerminalMenu(options)
    terminal_menu.title = 'Select context'
    index = terminal_menu.show()
    if index is None:
        return
    active_section = options[index].split(' ')[0]
    config.set(section='fish-ai', option='configuration', value=active_section)
    config.write(open(path.expanduser('~/.config/fish-ai.ini'), 'w'))
    print("💪 Now using '{}'.".format(active_section))
