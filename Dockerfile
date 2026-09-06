# syntax=docker/dockerfile:1

# Upstream Plex base — bump on Plex releases (wrapper semver lives in VERSION).
FROM --platform=linux/amd64 index.docker.io/plexinc/pms-docker:1.43.3.10896-cb3ebc72d

RUN apt update && apt install -y rsync postgresql-client python3 vim

COPY VERSION /etc/pms-docker/VERSION
COPY hashMovies.py /usr/bin
RUN chmod 755 /usr/bin/hashMovies.py
