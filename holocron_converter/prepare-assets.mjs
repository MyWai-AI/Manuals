// Stages the docs asset folders into ./public so Vite serves them at the site root.
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const here = path.dirname(fileURLToPath(import.meta.url))
const docsRoot = path.resolve(here, '..')
const publicDir = path.join(here, 'public')

// Folders referenced from the .mdx files as /images/... and /assets/...
const assetDirs = ['images', 'assets']

fs.rmSync(publicDir, { recursive: true, force: true })
fs.mkdirSync(publicDir, { recursive: true })

for (const dir of assetDirs) {
  const src = path.join(docsRoot, dir)
  if (fs.existsSync(src)) {
    fs.cpSync(src, path.join(publicDir, dir), { recursive: true })
  }
}
