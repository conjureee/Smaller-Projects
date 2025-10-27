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
        print(f'Zalogowano jako {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        # Join Voice Chat
        if message.content.startswith('$join'):
            if message.author.voice:
                channel = message.author.voice.channel
                await channel.connect()
                await message.channel.send(f"Dołączyłem do {channel}!")
            else:
                await message.channel.send("Musisz być na kanale głosowym!")

        # Leave Voice Chat
        if message.content.startswith('$leave'):
            if message.guild.voice_client:
                await message.guild.voice_client.disconnect()
                await message.channel.send("Wyszedłem")
            else:
                await message.channel.send("Nie jestem na żadnym kanale głosowym.")

        # Play some knot
        if message.content.startswith('$knot'):
            if message.guild.voice_client:
                await self.play_random_song(message.guild.voice_client, message.channel)
            else:
                await message.channel.send("Najpierw użyj $join!")

        # Pause
        if message.content.startswith('$pause'):
            if message.guild.voice_client and message.guild.voice_client.is_playing():
                message.guild.voice_client.pause()
                await message.channel.send("⏸️ Pauza")

        # Resume
        if message.content.startswith('$resume'):
            if message.guild.voice_client and message.guild.voice_client.is_paused():
                message.guild.voice_client.resume()
                await message.channel.send("▶️ Wznowiono")

        # Skip a Song
        if message.content.startswith('$next'):
            if message.guild.voice_client and (message.guild.voice_client.is_playing() or message.guild.voice_client.is_paused()):
                message.guild.voice_client.stop()
                await message.channel.send("⏭️ Następny utwór")


    # Rolling a new song
    async def play_random_song(self, voice_client, text_channel):
        song = get_song()
        source = discord.FFmpegPCMAudio(song, executable=FFMPEG_PATH)

        # Checking if there are any errors
        def after_playing(error):
            if error:
                print(f"Błąd: {error}")
            self.loop.call_soon_threadsafe(
                lambda: self.loop.create_task(self.play_random_song(voice_client, text_channel))
            )

        voice_client.play(source, after=after_playing)
        await text_channel.send(f"🎵 Gram: {os.path.basename(song)}")

# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

client = MyClient(intents=intents)
client.run('API KEY')