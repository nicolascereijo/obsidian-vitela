# obsidian-vitela

A minimal serif theme for long-form reading and writing in Obsidian.

- **[Lora](https://fonts.google.com/specimen/Lora)** for body text, a serif optimized for screen reading.
- **[EB Garamond](https://fonts.google.com/specimen/EB+Garamond)** for blockquotes, a low-contrast classic serif that sets quotes apart from body text.
- **[IBM Plex Mono](https://fonts.google.com/specimen/IBM+Plex+Mono)** for code blocks and inline code, a monospace typeface.
- A teal accent color, replacing Obsidian's default purple.
- Justified body text with automatic hyphenation, for a cleaner block shape
  in long-form reading without ragged whitespace.
- Tables with accent-tinted borders and row striping, instead of plain grey.
- Font size set in `rem`, so it respects the reader's own text size
  settings instead of overriding them, for anyone who needs a larger size.

![Dark mode](screenshots/dark.png)
![Light mode](screenshots/light.png)

## Installation

1. Download or clone this repository.
2. Copy the folder into `<vault>/.obsidian/themes/`. The containing folder's
   name doesn't matter, Obsidian reads `manifest.json` from every subfolder.
3. In Obsidian, go to **Settings → Appearance → Themes**, and select
   **obsidian-vitela**.

## Use with Obsidian Publish

Obsidian Publish does not read a vault's local theme files. To apply this
theme to a published site, copy `publish.css` to the root of the vault being
published. Obsidian Publish detects and applies it automatically.

## Fonts

Lora, EB Garamond and IBM Plex Mono are **self-hosted** from `fonts/` (latin
subset only, which covers Spanish, English and most other Latin-script
languages) instead of imported from Google Fonts, **to avoid leaking visitor
IPs and a render-blocking external request**. They're embedded as base64,
Obsidian blocks network requests from theme CSS, and Obsidian Publish's
media pipeline only accepts images, video, audio and PDF as standalone
assets, not font files, so a plain file `url()` doesn't work reliably in
either case.

## Development

`theme.css` is the only file meant to be hand-edited. `publish.css` is
generated from it (same rules, minus the editor-only half of each
selector, since a published page has no Live Preview), so the two can't
drift out of sync by hand. Run this after touching `theme.css` or a file
in `fonts/`:

```sh
./scripts/build.sh
```

It regenerates the embedded font block in `theme.css` first, then
regenerates `publish.css` from it. The two steps also run separately as
`scripts/build-fonts.sh` and `scripts/build-publish-css.sh`.

## Author

Nicolás Cereijo Ranchal.

- [Welcome page](https://publish.obsidian.md/nicolascereijo/welcome) (English)
- [Página de bienvenida](https://publish.obsidian.md/nicolascereijo/bienvenida) (Spanish)

## License

The theme itself is MIT, see [LICENSE](LICENSE). The fonts bundled in
`fonts/` are separately licensed under the SIL Open Font License 1.1 by
their respective authors, see `fonts/LICENSE-lora.txt`,
`fonts/LICENSE-eb-garamond.txt` and `fonts/LICENSE-ibm-plex-mono.txt`.
