#!/bin/sh
set -e

# first arg is `-f` or `--some-option`
# or first arg is `something.conf`
if [ "${1#-}" != "$1" ] || [ "${1%.conf}" != "$1" ]; then
        set -- jekyll_server "$@"
fi

# allow the container to be started with `--user`
if [ "$1" = 'jekyll_server' -a "$(id -u)" = '0' ]; then
        chown -R bitcoin .
        exec gosu bitcoin "$0" "$@"
fi

exec "$@"


