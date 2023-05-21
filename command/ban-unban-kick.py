from disnake.ext import commands

intents = disnake.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# kick user
@bot.slash_command(description="Kick user: /kick [@user] [reason]")
async def kick(inter, user: disnake.Member, *, reason = None):
    if not reason:
        emb = disnake.Embed(title="", color=inter.author.color)
        emb.add_field(name="", value=f"<@{user.id}> was kicked <@{inter.author.id}> for a reason **no reason**.", inline=True)
        await user.kick()
        await inter.send(embed=emb)
    else:
        emb = disnake.Embed(title="", color=inter.author.color)
        emb.add_field(name="", value=f"<@{user.id}> was kicked <@{inter.author.id}> for a reason **{reason}**.", inline=True)
        await user.kick(reason=reason)
        await inter.send(embed=emb)

# ban user
@bot.slash_command(description="Ban user: /ban [@user] [reason]")
async def ban(inter, user: disnake.Member, *, reason=None):
    if not reason:
        emb = disnake.Embed(title="", color=inter.author.color)
        emb.add_field(name="", value=f"<@{user.id}> was banned <@{inter.author.id}> for a reason **no reason**.", inline=True)
        await user.ban()
        await inter.send(embed=emb)
    else:
        emb = disnake.Embed(title="", color=inter.author.color)
        emb.add_field(name="", value=f"<@{user.id}> was kicked <@{inter.author.id}> for a reason **{reason}**.", inline=True)
        await user.ban(reason=reason)
        await inter.send(embed=emb)

# unban user
@bot.slash_command(description="Unban user: /unban [@user]")
async def unban(inter, *, member):
    banned_users = inter.guild.bans()
    member_name, member_discriminator = member.split('#')
    async for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            emb = disnake.Embed(title="", color=inter.author.color)
            emb.add_field(name="", value=f"<@{inter.author.id}> unbanned <@{user.id}>", inline=True)
            await inter.guild.unban(user)
            await inter.send(embed=emb)
        return
bot.run("YOUR_TOKEN")
