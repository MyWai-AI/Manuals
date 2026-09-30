# Build context: the repository root (docker build -f holocron_converter/Dockerfile .)
FROM node:22-slim

WORKDIR /app

# Install deps first (better layer caching)
COPY holocron_converter/package.json holocron_converter/package-lock.json ./holocron_converter/
RUN cd holocron_converter && npm ci

# Bring in the converter project and the docs content (untouched, in the repo root)
COPY . .

WORKDIR /app/holocron_converter

# Known content issues inherited from the GitBook migration (broken links,
# leftover README pages). Bypass so the build can finish; remove once fixed.
ENV HOLOCRON_SKIP_BUILD_ERRORS=true

# `npm run build` stages images/assets into public/ (prebuild) and runs vite build
RUN npm run build

ENV PORT=3000
EXPOSE 3000

CMD ["node", "/app/dist/rsc/index.js"]
