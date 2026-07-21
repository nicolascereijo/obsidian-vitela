#!/usr/bin/env bash
# Single entry point. Regenerates the embedded font block in theme.css,
# then regenerates publish.css from theme.css. Run after touching fonts/
# or theme.css.
set -euo pipefail
cd "$(dirname "$0")"

./build-fonts.sh
./build-publish-css.sh
