import argparse

from os import path
from typing import Callable, List

from beets.dbcore.query import ParsingError
from beets.library import Item, Library, parse_query_string
from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
from beets.util import bytestring_path, normpath


class PlaylistcPlugin(BeetsPlugin):
    def __init__(self):
        super(PlaylistcPlugin, self).__init__()

    def commands(self) -> List[Subcommand]:
        cmd = PlaylistcCommand(self)
        return [cmd]

    def playlist_dir(self) -> str:
        key = 'playlist_dir'
        return normpath(self.config[key].get(str))

    def relative_to(self) -> str:
        key = 'relative_to'
        return normpath(self.config[key].get(str))

    def create(self, lib: Library, name: str, qs: str):
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
            item.path, self.relative_to()).decode('utf-8')
        paths: List[str] = map(item_path, items)

        playlist_dir = self.playlist_dir()
        if playlist_dir is None:
            return
        filename = path.join(self.playlist_dir(),
                             bytestring_path(name + '.m3u'))
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
        create_parser.add_argument('name', metavar='NAME')
        create_parser.add_argument('query', metavar='QUERY', nargs='*')

        super(PlaylistcCommand, self).__init__(
            self.name, parser, self.help, aliases=self.aliases)

    def create(self, lib, opts):
        self.plugin.create(lib, opts.name, ' '.join(opts.query))

    def func(self, lib, opts, _):
        opts.func(lib, opts)

    def parse_args(self, args):
        return self.parser.parse_args(args), []
