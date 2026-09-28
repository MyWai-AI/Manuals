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

Only the fully local (`full`/`sso`) flavor bundles the manual. The `external-sso` flavor, base compose, nginx, `release-services.json` and its release pipeline are untouched.

- `deploy/platform/docker-compose.sso.yaml`: `user-manual` service on `USER_MANUAL_HTTP_PORT` (default 18447), image tag from `USER_MANUAL_VERSION`. The webapp gets `EndPoints__ManualUrl` pointing at it.
- Frontend: `Platform/MywAi.Web/Scripts/Services/Helpers/manualHelper.js` `getUrl()` prefers `window.manualUrl` (injected by `_Layout.cshtml` and `_LayoutMarketplace.cshtml` from `EndPoints:ManualUrl`) and falls back to the public GitBook. Used by the Help button (`nav-bar-tool.vue`, `left-menu.vue`), `getting-started.vue` and `dialog-algorithm-details.vue` (SDK docs link).

## Status

Both repos have `features/user-manual` committed locally (Manuals `024ba52`, MYWAI `7870c29f4`). Not pushed, no PR.

## Open points (start here)

1. **`USER_MANUAL_VERSION`**: decide the default in `docker-compose.sso.yaml` and how a deployment gets the right tag from the `user-manual` release pipeline.
2. **Azure DevOps pipeline**: create it from `azure-pipelines.yml` and run it once. The first run has never happened, so the shared template, the multi-arch build and the version gate are untested.
3. **Frontend bundle**: regenerate the MYWAI webapp bundle and check that Help, getting-started and SDK docs open the bundled manual. The Vue/JS changes were never built or verified.
4. **Firewall**: decide whether port 18447 must be opened on the hosts running the `sso` flavor.
5. **Push and PR**: push both `features/user-manual` branches and open PRs (targets: Manuals `main`, MYWAI `master`).
6. **Local Docker cleanup** (optional): remove the `user-manual` container and the `user-manual` and `manuals-docs` images left from testing, to free disk.

In MYWAI the unrelated `deploy/legacy/` deletions and `docs/architecture/platform-orchestrator-elsa-next-steps.md` are uncommitted and not part of this work.
