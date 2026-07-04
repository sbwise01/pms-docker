# syntax=docker/dockerfile:1

# Upstream Plex base — bump on Plex releases (wrapper semver lives in VERSION).
FROM --platform=linux/amd64 index.docker.io/plexinc/pms-docker:1.43.2.10687-563d026ea

RUN apt update && apt install -y rsync postgresql-client python3 vim

COPY VERSION /etc/pms-docker/VERSION
COPY hashMovies.py /usr/bin
RUN chmod 755 /usr/bin/hashMovies.py
