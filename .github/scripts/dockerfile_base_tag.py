#!/usr/bin/env python3
"""Extract the base image tag from the first FROM line in a Dockerfile.

Usage: dockerfile_base_tag.py [path-to-dockerfile]   (defaults to ./Dockerfile)

Parses the image reference on the first FROM line (skipping flags like
--platform=...) and prints the tag portion after the final colon.
"""
import re
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "Dockerfile"
with open(path, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if not line.upper().startswith("FROM"):
            continue
        rest = line[4:].strip()
        rest = re.split(r"\s+AS\s+", rest, maxsplit=1, flags=re.I)[0].strip()
        tokens = rest.split()
        if not tokens:
            sys.exit(f"invalid FROM line in {path}")
        image = tokens[-1]
        if "@" in image:
            sys.exit(f"FROM uses a digest, not a tag: {image}")
        if ":" not in image:
            sys.exit(f"no tag in FROM image reference: {image}")
        tag = image.rsplit(":", 1)[1]
        if not tag:
            sys.exit(f"empty tag in FROM line: {line}")
        print(tag)
        sys.exit(0)

sys.exit(f"no FROM line found in {path}")
