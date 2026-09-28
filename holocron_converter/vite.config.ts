import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { defineConfig } from 'vite'
import { holocron } from '@holocron.so/vite'

const __dirname = path.dirname(fileURLToPath(import.meta.url))

// The docs (docs.json + .mdx) live in the repo root, one level up.
// We never copy/move them - Holocron just reads them from there.
const docsRoot = path.resolve(__dirname, '..')

// Vite only copies a dedicated publicDir, which can't be `root` itself
// (outDir is nested inside it). prepare-assets.mjs stages the asset folders
// into ./public before every dev/build.
const publicDir = path.resolve(__dirname, 'public')

export default defineConfig({
  root: docsRoot,
  publicDir,
  plugins: [holocron({ pagesDir: '.' })],
})
