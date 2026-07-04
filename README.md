# pms-docker

Wrapper image for Plex Media Server used in the wise-k8s homelab.

Extends the upstream [`plexinc/pms-docker`](https://hub.docker.com/r/plexinc/pms-docker)
image with extra CLI tools and `hashMovies.py` for media metadata management.

## Versioning

- **`VERSION`** — wrapper semver (`X.Y.Z`); single source of truth for the published
  image tag `sbwise/pms-docker:<VERSION>`.
- **`Dockerfile` `FROM`** — upstream Plex base pin only (not the publish tag).

Inside the image, the wrapper version is at `/etc/pms-docker/VERSION`.

## CI/CD

- **`pr.yml`** — Conventional Commit PR title drives a semver bump to `VERSION`, then
  a Docker test build.
- **`release.yml`** — on merge to `main`, tags git + pushes `sbwise/pms-docker:<VERSION>`.

**Bootstrap:** the first merge introducing `VERSION`/`2.0.0` should land on `main`
directly (or merge as admin) so `release.yml` can create the initial `2.0.0` tag;
subsequent PRs then pass the baseline tag check.
