# ---- IMPORTANT ----
# 1. Install FFmpeg and make sure the path to the executable is correct
# (e.g., C:\ffmpeg\bin\ffmpeg.exe on Windows).
#
# 2. Create an app and a bot on the Discord developer website:
# https://discord.com/developers/applications
# - Copy your bot's token and paste it into the 'Api Key' field at the bottom of the program.
# - Add the bot to your server with the appropriate permissions (including reading messages and connecting to voice).
#
# 3. Prepare a music folder (e.g., 'knot') and place the .mp3 files in it.
# You can change the folder name in the MUSIC_FOLDER variable.
#
# 4. Run the program. The bot responds to text commands in chat:
# - $join -> joins your voice channel
# - $leave -> leaves the channel
# - $knot -> starts playing random songs from the folder
# - $pause -> pauses playback
# - $resume -> resumes playback
# - $next -> skips to the next random song
#
# 5. The program runs in a loop – when one song ends, it automatically randomizes the next one.
#
# Feel free to customize: change the music folder, add your own commands, and expand the bot's logic :D


import discord
import os
import random

MUSIC_FOLDER = 'knot'
FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"

def get_song():
    files = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
    return os.path.join(MUSIC_FOLDER, random.choice(files))

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        # Join Voice Chat
        if message.content.startswith('$join'):
            if message.author.voice:
                channel = message.author.voice.channel
                await channel.connect()
                await message.channel.send(f"I joined {channel}!")
            else:
                await message.channel.send("You have to be in the voice chat!")

        # Leave Voice Chat
        if message.content.startswith('$leave'):
            if message.guild.voice_client:
                await message.guild.voice_client.disconnect()
                await message.channel.send("I left")
            else:
                await message.channel.send("I'm not in any voice chat")

        # Play some knot
        if message.content.startswith('$knot'):
            if message.guild.voice_client:
                await self.play_random_song(message.guild.voice_client, message.channel)

        # Pause
        if message.content.startswith('$pause'):
            if message.guild.voice_client and message.guild.voice_client.is_playing():
                message.guild.voice_client.pause()
                await message.channel.send("⏸️ Paused")

        # Resume
        if message.content.startswith('$resume'):
            if message.guild.voice_client and message.guild.voice_client.is_paused():
                message.guild.voice_client.resume()
                await message.channel.send("▶️ Resumed")

        # Skip a Song
        if message.content.startswith('$next'):
            if message.guild.voice_client and (message.guild.voice_client.is_playing() or message.guild.voice_client.is_paused()):
                message.guild.voice_client.stop()
                await message.channel.send("⏭️ Next song")


    # Rolling a new song
    async def play_random_song(self, voice_client, text_channel):
        song = get_song()
        source = discord.FFmpegPCMAudio(song, executable=FFMPEG_PATH)

        # Checking if there are any errors
        def after_playing(error):
            if error:
                print(f"ERROR: {error}")
            self.loop.call_soon_threadsafe(
                lambda: self.loop.create_task(self.play_random_song(voice_client, text_channel))
            )

        voice_client.play(source, after=after_playing)
        await text_channel.send(f"🎵 Playing: {os.path.basename(song)}")

# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

client = MyClient(intents=intents)

client.run('API KEY')
