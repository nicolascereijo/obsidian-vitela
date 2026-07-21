# obsidian-vitela

A minimal serif theme for long-form reading and writing in Obsidian.

- **Lora** for body text.
- **EB Garamond** for blockquotes.
- **IBM Plex Mono** for code.
- A teal accent color, replacing Obsidian's default purple.

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
theme to a published site, copy `publish.css` (a trimmed version of
`theme.css`, without editor-only rules that don't apply to published pages)
to the root of the vault being published, renamed to `publish.css`. Obsidian
Publish detects and applies it automatically.
