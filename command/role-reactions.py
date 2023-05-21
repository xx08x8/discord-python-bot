from disnake.ext import commands

intents = disnake.Intents.default()
intents.members = True
intents.reactions = True
bot = commands.Bot(command_prefix="!", intents=intents)

ROLE_MESSAGE_ID = 1234567890  # message ID
EMOJI_TO_ROLE = {
    disnake.PartialEmoji(name="🔴"): 123,  # ID of the role associated with unicode emoji '🔴'.
    disnake.PartialEmoji.from_str(":emoji:emoji_id"): 123, # Role ID associated with emoji ID
    # You can get an emoji ID by typing \ in front of the emoji.
}

@bot.event
async def on_raw_reaction_add(payload: disnake.RawReactionActionEvent):
        if payload.guild_id is None or payload.member is None:
            return
        if payload.message_id != ROLE_MESSAGE_ID:
            return
        guild = bot.get_guild(payload.guild_id)
        if guild is None:
            return
        try:
            role_id = EMOJI_TO_ROLE[payload.emoji]
        except KeyError:
            return
        role = guild.get_role(role_id)
        if role is None:
            return
        try:
            await payload.member.add_roles(role)
        except disnake.HTTPException:
            pass

@bot.event
async def on_raw_reaction_remove(payload: disnake.RawReactionActionEvent):
    if payload.guild_id is None:
        return
    if payload.message_id != ROLE_MESSAGE_ID:
        return
    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        return
    try:
        role_id = EMOJI_TO_ROLE[payload.emoji]
    except KeyError:
        return
    role = guild.get_role(role_id)
    if role is None:
        return
    member = guild.get_member(payload.user_id)
    if member is None:
        return
    try:
        await member.remove_roles(role)
    except disnake.HTTPException:
        pass

bot.run("YOUR_TOKEN")
