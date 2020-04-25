import argparse

from os import path
from typing import Callable, List

from beets.dbcore.query import ParsingError
from beets.library import Item, Library, parse_query_string
from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
from beets.util import normpath


class PlaylistcPlugin(BeetsPlugin):
    def __init__(self):
        super(PlaylistcPlugin, self).__init__()

    def commands(self) -> List[Subcommand]:
        cmd = PlaylistcCommand(self)
        return [cmd]

    def config_playlist_dir(self) -> str:
        key = 'playlist_dir'
        return normpath(self.config[key].get(str)).decode('utf-8')

    def config_relative_to(self) -> str:
        key = 'relative_to'
        return normpath(self.config[key].get(str)).decode('utf-8')

    def create(self, lib: Library, name: str, qs: str,
               playlist_dir: str, relative_to: str):
        if playlist_dir is None:
            playlist_dir = self.config_playlist_dir()
        if relative_to is None:
            relative_to = self.config_relative_to()

        # Try to parse the query
        try:
            if qs is None:
                query, sort = None, None
            else:
                query, sort = parse_query_string(qs, Item)
        except ParsingError as ex:
            self._log.warning(u'invalid query: {}', ex)
            return

        # Map items to their paths
        items = lib.items(query, sort)
        item_path: Callable[Item, str] = lambda item: path.relpath(
            item.path.decode('utf-8'), relative_to)
        paths: List[str] = map(item_path, items)

        filename = path.join(playlist_dir, name + '.m3u')
        file = open(filename, 'w+')

        write_str = '\n'.join(paths)
        file.write(write_str)
        file.close()


class PlaylistcCommand(Subcommand):
    name = 'playlistc'
    aliases = ('plc',)
    help = 'create a playlist'

    plugin: PlaylistcPlugin = None

    def __init__(self, plugin: PlaylistcPlugin):
        self.plugin = plugin

        parser = argparse.ArgumentParser()
        subparsers = parser.add_subparsers(
            prog=parser.prog + ' playlistc', dest='command', required=True)

        create_parser = subparsers.add_parser('create')
        create_parser.set_defaults(func=self.create)
        create_parser.add_argument(
            '--playlist-dir', dest='playlist_dir', metavar='PATH')
        create_parser.add_argument(
            '--relative-to', dest='relative_to', metavar='PATH')
        create_parser.add_argument('name', metavar='NAME')
        create_parser.add_argument('query', metavar='QUERY', nargs='*')

        super(PlaylistcCommand, self).__init__(
            self.name, parser, self.help, aliases=self.aliases)

    def create(self, lib, opts):
        self.plugin.create(lib, opts.name, ' '.join(
            opts.query), opts.playlist_dir, opts.relative_to)

    def func(self, lib, opts, _):
        opts.func(lib, opts)

    def parse_args(self, args):
        return self.parser.parse_args(args), []
