# Changelog

All notable changes to this theme are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

- Polilla, devourer of margins, scourge of serifs, terror of character spacing, gnawer of paragraphs, eternal enemy of the justified line.

## [1.2.0] - 2026-08-01

- Added three custom callouts, styled with layout only and no admonition
  box. `[!columns]` for two newspaper-style columns, `[!epigraph]` for a
  centered pull quote and `[!verse]` for poetry that keeps the author's
  own line breaks instead of being justified.

## [1.1.6] - 2026-07-25

- Updated `screenshots/hero.png` to the final cover image.

## [1.1.5] - 2026-07-25

- Simplified the README installation instructions to the marketplace
  method only, since manual installation requires the theme folder to
  be renamed to match `manifest.json`'s `name` field exactly, which the
  previous instructions didn't mention.
- The Obsidian Publish instructions now link directly to `publish.css`
  from the latest GitHub release instead of assuming the reader has
  cloned the repository.

## [1.1.4] - 2026-07-25

- Table border and background `color-mix()` refinements moved into an
  `@supports` block instead of a second same-property declaration in the
  same rule, avoiding a false-positive "duplicate property" flag from
  automated scans while keeping the same solid-color fallback behavior.
- Replaced the `:has()`-based hashtag alignment rule, flagged by
  automated scans for its performance cost, with a plain attribute
  selector that left-aligns all text inside `[!note]` callouts instead
  of only lines containing a tag.

## [1.1.3] - 2026-07-25

- Fixed `authorUrl` in `manifest.json` pointing to an Obsidian-owned
  domain instead of the author's own page.
- Removed the unsupported `description` field from `manifest.json`
  (themes don't use it, only plugins do).

## [1.1.2] - 2026-07-22

- Renamed the theme's display name from `obsidian-vitela` to `Vitela`
  in `manifest.json`.
- Renamed the CI workflow file to `checks.yml` and marked `*.woff2` as
  binary in `.gitattributes`.
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

[Unreleased]: https://github.com/nicolascereijo/obsidian-vitela/compare/1.2.0...HEAD
[1.2.0]: https://github.com/nicolascereijo/obsidian-vitela/compare/1.1.6...1.2.0
[1.1.6]: https://github.com/nicolascereijo/obsidian-vitela/compare/1.1.5...1.1.6
[1.1.5]: https://github.com/nicolascereijo/obsidian-vitela/compare/1.1.4...1.1.5
[1.1.4]: https://github.com/nicolascereijo/obsidian-vitela/compare/1.1.3...1.1.4
[1.1.3]: https://github.com/nicolascereijo/obsidian-vitela/compare/1.1.2...1.1.3
[1.1.2]: https://github.com/nicolascereijo/obsidian-vitela/compare/v1.1.1...1.1.2
[1.1.1]: https://github.com/nicolascereijo/obsidian-vitela/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/nicolascereijo/obsidian-vitela/compare/v1.0.2...v1.1.0
[1.0.2]: https://github.com/nicolascereijo/obsidian-vitela/compare/v1.0.1...v1.0.2
[1.0.1]: https://github.com/nicolascereijo/obsidian-vitela/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/nicolascereijo/obsidian-vitela/releases/tag/v1.0.0
