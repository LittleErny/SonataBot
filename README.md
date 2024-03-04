# Discord-bot "Sonata"

**Teacher:** Sergey Andreevich Glushenko  
**Yandex Lyceum at RSEU(RINH), Rostov-on-Don**  
**May 2020**

"Sonata" is a Discord bot (hereinafter referred to as the bot), written in Python 3.8, designed to listen to music. The bot utilizes Discord.py - an API for interaction with Discord servers, and Yandex-music API - an unofficial API for searching and downloading tracks from the online service Yandex.music. The bot is intended for personal, non-commercial use.

## Brief instructions:
- **Prefix**: "?" - a symbol to be written before each message to the bot (a kind of address to the bot)
- `?join`: Join the voice channel you are in (you must be in the channel).
- `?play <song name>`: Join the channel, download the track, and play it in the channel. If the bot is already playing, the song will be added to the queue.
- `?stop`: Pause playback.
- `?continue`: Unpause playback.
- `?skip`: Skip the current track.
- In case of an error, restart the bot.

---

**Disclaimer**: This bot was developed in 2020 and may not work correctly with current versions of Discord.py and Yandex-music API, as it was not supported or maintained beyond that time.
