import discord
from discord.ext import commands
from yandex_requests import YandexMusicApi
from my_queue import Queue
# import asyncio

with open("discord_token.txt", 'r') as f:
    TOKEN = f.readline()

PREFIX = '?'


class RandomThings(commands.Cog):
    def __init__(self, bot):
        self.songsAPI = YandexMusicApi()
        self.bot = bot
        self.guild_statuses = {}
        self.messages = []

    def play_next_song(self, ctx):
        pass

    # function for initialize smth extra information
    @commands.command(name='init')
    async def extra_init(self, ctx):
        self.guild_statuses = {i.id: {'queue': Queue(self), 'song': None} for i in self.bot.guilds}
        await ctx.send('initialized')

    @commands.command(name='test')  # имя команды из дискорда
    async def test(self, ctx: commands.context.Context, mess):  # явно указываем тип для подсказок PyCharm:
        await ctx.send(str(mess))

    @commands.command(name='join')
    async def join_voice_channel(self, ctx: commands.context.Context):
        chnl = ctx.author.voice
        if chnl:
            print(chnl)
            await chnl.channel.connect()

    @commands.command(name='play')
    async def play(self, ctx, *args):
        chnl = ctx.author.voice
        track = self.songsAPI.get_quest(' '.join(list(args)))
        # a = [chnl in x.channel for x in self.bot.voice_clients]
        if not any([chnl.channel == x.channel for x in self.bot.voice_clients]):
            vc = await chnl.channel.connect()
            await ctx.send('connecting...')
        else:
            for vc in self.bot.voice_clients:
                if vc.guild == ctx.guild:
                    break
            # vc = self.bot.voice_clients
            await ctx.send("I'm already connected")
        if vc.source:
            a = self.guild_statuses[ctx.guild.id]['queue'].add((ctx, *args))
            await ctx.send("It's added to the queue")
        else:
            vc.play(discord.FFmpegPCMAudio(executable="ffmpeg/ffmpeg.exe", source=track),
                    after=self.guild_statuses[ctx.guild.id]['queue'].next)
            await ctx.send("It's just a warm-up!")

    @commands.command(name='stop')
    async def stop(self, ctx):
        chnl = ctx.author.voice
        found = False
        for vc in self.bot.voice_clients:
            found = True
            if vc.guild == ctx.guild:
                break
        if not found:
            await ctx.send("It's nothing to pause")
            return None
        if not vc.is_paused():
            await ctx.send("paused")
            vc.pause()
        else:
            await ctx.send("I'm paused yet")

    @commands.command(name='continue')
    async def continuing(self, ctx):
        chnl = ctx.author.voice
        for vc in self.bot.voice_clients:
            if vc.guild == ctx.guild:
                break
        if not vc.is_playing():
            await ctx.send("continuing..")
            vc.resume()
        else:
            await ctx.send("I'm already playing")

    @commands.command(name='skip')
    async def skip(self, ctx):
        chnl = ctx.author.voice
        for vc in self.bot.voice_clients:
            if vc.guild == ctx.guild:
                break
        if vc.source:
            await ctx.send("skipping")
            vc.stop()
            play_next = self.guild_statuses[ctx.guild.id]['queue'].next
            await play_next()
            await ctx.send("skipped")
        else:
            await ctx.send("it's nothing to skip")



bot = commands.Bot(command_prefix=PREFIX)
my_bot = RandomThings(bot)
bot.add_cog(my_bot)
bot.run(TOKEN)
