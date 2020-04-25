# beets-playlistc

This [beets](https://beets.readthedocs.io/en/latest/index.html) plugin
allows for the creation of playlists based on your beets database. Take
advantage of beets's rich query system.

## Usage

The options `playlist_dir` and `relative_to` must be specified in
beets's configuration file.

    playlistc:
      playlist_dir: ~/files/music/playlists
      relative_to: ~/files/music/library

Playlists are created using the subcommand `playlistc create`:

    $ beet playlistc create NAME QUERY

The paths of the matching items relative to the path specified in
`relative_to` are written to `playlist_dir/NAME.m3u`.
