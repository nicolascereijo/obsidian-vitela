# obsidian-vitela

A minimal serif theme for long-form reading and writing in Obsidian.

- **[Lora](https://fonts.google.com/specimen/Lora)** for body text, a serif optimized for screen reading.
- **[EB Garamond](https://fonts.google.com/specimen/EB+Garamond)** for blockquotes, a low-contrast classic serif that sets quotes apart from body text.
- **[IBM Plex Mono](https://fonts.google.com/specimen/IBM+Plex+Mono)** for code blocks and inline code, a monospace typeface.
- A teal accent color, replacing Obsidian's default purple.
- Justified body text, for a cleaner block shape in long-form reading.
- Tables with accent-tinted borders and row striping, instead of plain grey.

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
IPs and a render-blocking external request**. Both `theme.css` and
`publish.css` embed them as base64, Obsidian blocks network requests from
theme CSS, and Obsidian Publish's media pipeline only accepts images, video,
audio and PDF as standalone assets, not font files, so a plain file `url()`
doesn't work reliably in either case. `publish.css` is published as-is
regardless, so inlining the fonts there sidesteps that limitation, no
separate file to upload. After adding, removing or replacing a file in
`fonts/`, regenerate both embedded blocks with:

```sh
./scripts/build-fonts.sh
```

## Author

Nicolás Cereijo Ranchal.

- [Welcome page](https://publish.obsidian.md/nicolascereijo/welcome) (English)
- [Página de bienvenida](https://publish.obsidian.md/nicolascereijo/bienvenida) (Spanish)

## License

MIT, see [LICENSE](LICENSE).
