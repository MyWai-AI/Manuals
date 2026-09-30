# Manuals: MYW.AI user manual

Shared context for AI coding agents (Cursor reads this file directly; `CLAUDE.md` imports it for Claude Code, so edit only here).

Sources are the `.mdx` pages at the repo root plus `docs.json` (Mintlify format). Only pages listed in `docs.json` navigation are published, so this file is not part of the manual.

## Self-hosted build (Holocron)

- `holocron_converter/` is a Vite + `@holocron.so/vite` project that reads the docs from the repo root without moving them. `prepare-assets.mjs` stages `images/` and `assets/` into `public/` (gitignored).
- Build only through Docker (Linux). A native Windows build fails in the spiceflow prerender step.
- `docker-compose.yml` builds the `user-manual` image. A local container serves it on `localhost:3000`.
- `azure-pipelines.yml` uses the same shared release template as Embedding-Service (image `user-manual`, multi-arch). The version comes from `deploy/versioning/version.json` (`1.0.N[-env]`, N is not a CI counter, see its `notes`).
- To free disk: `node_modules/` and `holocron_converter/public/` are regenerable (`npm ci`, `npm run build`).

## MYWAI side (repo `MYWAI`, branch `features/user-manual`, from `master`)

Only the fully local (`full`/`sso`) flavor bundles the manual. The `external-sso` flavor, base compose, nginx and its release pipeline are otherwise untouched.

- Versioning matches `embedding-service`/`flowise`: `user-manual` is in `pipelines/release-dev.yml`'s `externalImageNames`, so the platform release manifest records its newest published ACR tag (never `latest`) and pins it by digest — no `USER_MANUAL_VERSION` variable. `docker-compose.sso.yaml` uses the sentinel `${REGISTRY}/user-manual:pinned-by-release-manifest`, which fails fast if unpinned.
- `release-services.json` is shared with `external-sso` (same `pin-release.sh` for both flavors), but `user-manual` only exists in `docker-compose.sso.yaml`. Pinning it there too would otherwise add a phantom, portless `user-manual` container to `external-sso`'s project on a plain `up -d`. Fixed with a compose profile: a `user-manual: profiles: ["full"]` stub lives in `docker-compose.base.yaml` (loaded by both flavors, so the gate applies even where `docker-compose.sso.yaml` is absent); `docker-compose.sso.yaml` adds the rest (image/ports/network) on top. `update.sh`/`update.ps1` pass `--profile full` whenever `--flavor full` is requested; README documents it for manual compose commands. `mywai-cli` needed no change — its `--profile` flag was already generic.
- `docker-compose.sso.yaml`: `user-manual` on `USER_MANUAL_HTTP_PORT` (default 18447). The webapp gets `EndPoints__ManualUrl` pointing at it.
- Frontend: `Platform/MywAi.Web/Scripts/Services/Helpers/manualHelper.js` `getUrl()` prefers `window.manualUrl` (injected by `_Layout.cshtml` and `_LayoutMarketplace.cshtml` from `EndPoints:ManualUrl`) and falls back to the public GitBook. Used by the Help button (`nav-bar-tool.vue`, `left-menu.vue`), `getting-started.vue` and `dialog-algorithm-details.vue` (SDK docs link).

## Status

Both repos have `features/user-manual` committed locally (Manuals `024ba52`, `bdbc8d1`, `f8705ee`; MYWAI `7870c29f4`, `08fc60a47`). Not pushed, no PR.

Verified locally: `docker compose build --no-cache` + `up` for the Holocron site (home and two content pages return HTTP 200). The `--profile full` gating was verified with `docker compose config` against a dummy `.env`, for all four combinations (each flavor, with/without the profile, plus a simulated `docker-compose.release.yml` override) — `user-manual` is absent by default on both flavors, present only on `full` with `--profile full`.

## Open points (start here)

1. **Azure DevOps pipeline**: create it from `azure-pipelines.yml` (Manuals) and run it once. The first run has never happened, so the shared template, the multi-arch build, the version gate, and the new `externalImageNames`/`release-services.json` wiring in MYWAI are all untested end to end.
2. **Frontend bundle**: regenerate the MYWAI webapp bundle and check that Help, getting-started and SDK docs open the bundled manual. The Vue/JS changes were never built or verified.
3. **Firewall**: decide whether port 18447 must be opened on the hosts running the `full`/`sso` flavor.
4. **Push and PR**: push both `features/user-manual` branches and open PRs (targets: Manuals `main`, MYWAI `master`).
5. **Local Docker cleanup** (optional): remove the `user-manual` container and the `user-manual`/`manuals-docs` images left from testing, to free disk.

In MYWAI the unrelated `deploy/legacy/` deletions and `docs/architecture/platform-orchestrator-elsa-next-steps.md` are uncommitted and not part of this work. Also: the MYWAI checkout's current branch flipped under this session more than once (between `features/user-manual`, `features/label_and_embeddings` and `master`), presumably from Cursor working the same clone concurrently. Double-check the current branch before continuing there.
