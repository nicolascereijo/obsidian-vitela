# Changelog

All notable changes to this theme are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

- Renamed the CI workflow file to `checks.yml` and marked `*.woff2` as
  binary in `.gitattributes`.

## [1.1.2] - 2026-07-22

- Table cells and header backgrounds now fall back to a solid color on
  browsers without `color-mix()` support, documented alongside the
  existing border fallback.
- Raised the dark mode accent lightness so accent-colored text meets
  WCAG AA contrast (4.5:1) against the dark background.
- Added `scripts/validate-manifest.py` and a matching CI job to catch a
  malformed or incomplete `manifest.json`.
- Added Dependabot configuration to keep GitHub Actions up to date.
- Added a `.gitattributes` entry so GitHub Linguist keeps counting
  `theme.css`/`publish.css` as CSS despite the embedded font base64
  pushing them past its minified-file threshold.
- Added license files for the three bundled fonts (Lora, EB Garamond,
  IBM Plex Mono).
- `scripts/build-publish-css.sh` now detects the end of the banner
  comment dynamically instead of assuming a fixed line count.

## [1.1.1] - 2026-07-22

- Added automatic hyphenation to body text and blockquotes, for a
  cleaner block shape under justification.
- Font size is now set in `rem` instead of a fixed unit, so it respects
  the reader's own text size settings.

## [1.1.0] - 2026-07-22

- Added `scripts/build-publish-css.sh`, generating `publish.css` from
  `theme.css` so both stay in sync, and documented how to use it with
  Obsidian Publish.
- Added a CI workflow that fails if regenerating the theme's build
  output changes anything.

## [1.0.2] - 2026-07-22

- Fonts (Lora, EB Garamond, IBM Plex Mono) are now self-hosted and
  embedded as base64, instead of imported from Google Fonts, to avoid
  leaking visitor IPs and a render-blocking external request. Added
  `scripts/build-fonts.sh` to regenerate the embedded font block.

## [1.0.1] - 2026-07-22

- Synced `manifest.json`'s description with the feature list in the
  README.
- Reformatted the `theme.css`/`publish.css` header banners to match the
  section dividers below them.

## [1.0.0] - 2026-07-18

Initial release.

- MIT license.
- Lora for body text, EB Garamond for blockquotes, IBM Plex Mono for
  code, justified body text.
- Teal accent color, replacing Obsidian's default purple.
- Accent-tinted table borders and row striping.
- Left-aligned headings, and left-aligned hashtag lines inside metadata
  callouts, kept separate from the surrounding justified text.
- README with feature overview, installation steps and license
  documentation.
- Theme screenshots.

[Unreleased]: https://github.com/nicolascereijo/obsidian-vitela/compare/v1.1.2...HEAD
[1.1.2]: https://github.com/nicolascereijo/obsidian-vitela/compare/v1.1.1...v1.1.2
[1.1.1]: https://github.com/nicolascereijo/obsidian-vitela/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/nicolascereijo/obsidian-vitela/compare/v1.0.2...v1.1.0
[1.0.2]: https://github.com/nicolascereijo/obsidian-vitela/compare/v1.0.1...v1.0.2
[1.0.1]: https://github.com/nicolascereijo/obsidian-vitela/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/nicolascereijo/obsidian-vitela/releases/tag/v1.0.0
