# License and Attribution Notices

## Hybrid Spotify Downloader

**License:** MIT
**Copyright:** 2024 CHAIBERI

See LICENSE file for full MIT license text.

---

## Dependencies and Third-Party Code

### Spotipy
- **License:** MIT
- **Repository:** https://github.com/plamere/spotipy
- **Copyright:** Paul Lamere
- **Usage:** Spotify Web API wrapper for metadata extraction

### yt-dlp
- **License:** Unlicense (Public Domain)
- **Repository:** https://github.com/yt-dlp/yt-dlp
- **Usage:** YouTube audio downloading

### Mutagen
- **License:** GPLv2 (with permission for GPL-compatible projects)
- **Repository:** https://github.com/quodlibet/mutagen
- **Usage:** Audio metadata tag manipulation (ID3, Vorbis, etc.)

### Click
- **License:** BSD 3-Clause
- **Repository:** https://github.com/pallets/click
- **Usage:** CLI framework

### Platformdirs
- **License:** MIT
- **Repository:** https://github.com/platformdirs/platformdirs
- **Usage:** Platform-specific directory paths

---

## Inspiration and References

This project was inspired by and makes reference to the following projects:

### Savify
- **License:** MIT
- **Repository:** https://github.com/LaurenceRawlings/savify
- **Author:** Laurence Rawlings
- **Inspiration:** Architecture for Spotify metadata extraction and local file organization
- **Note:** Code was not directly copied; instead, the project implements a similar pattern with original code.

### spotDL
- **License:** MIT
- **Repository:** https://github.com/spotDL/spotify-downloader
- **Usage:** Reference for project structure and CLI patterns
- **Note:** Code was not directly copied; spotDL uses yt-dlp as we do.

---

## Important Legal Notice

**Audio Sourcing:**
- This application uses Spotify API ONLY for metadata extraction (track info, album art, etc.)
- Audio files are downloaded from YouTube, NOT from Spotify
- This complies with Spotify Terms of Service
- Users are responsible for respecting copyright and local laws when downloading music
- This tool is for personal use only

**Disclaimer:**
This software is provided "as is" without warranty. Users must comply with all applicable laws and service terms.

---

## GPL Compatibility Note

This project uses Mutagen (GPLv2) for metadata operations. Since Mutagen is dual-licensed and we are using it as a library with proper attribution, this complies with GPL v2 requirements:

- Source code is available: https://github.com/CHAIBERI/spotify-hybrid-downloader
- Mutagen library can be replaced or removed
- This project is distributed under MIT (compatible with GPL v2 as downstream)
- Attribution: See this file
