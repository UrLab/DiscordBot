import nextcord
from DiscordBot.logger import log


# TODO: make it actually log the channels to a .json or a db

async def emoji(message: nextcord.Message, client):
    await message.channel.send("Which channel do you want me to use for the emoji reaction system? (Enter the "
                               "channel ID or 'new' to create a new channel)")
    channel_response = await client.wait_for("message")

    if channel_response.content.lower() == "new":
        channel = await message.guild.create_text_channel('emoji')
        log("command", f"New emoji channel {channel.id} in {message.guild.name}")

    else:
        channel = client.get_channel(int(channel_response.content))

    await channel.send(f"{message.author.mention} Which emojis do you want me to associate with which roles? ("
                       f"Enter each association in the format 'emoji: role', or 'done' when finished)")

    associations = {}

    while True:
        association_response = await client.wait_for("message")
        if association_response.content.lower() == "done":
            break

        emoji, role = association_response.content.split(":")

        emoji = emoji.strip()
        role = role.strip()
        associations[emoji] = role

    await channel.send('Please send the message you want me to react to with the corresponding emojis:')

    user_message = await client.wait_for("message")
    log("command", f"Logged message {user_message.id} in {message.guild.name}")

    for emoji in associations:
        await user_message.add_reaction(emoji)

    @client.event
    async def on_raw_reaction_add(payload):
        if payload.member == client.user:
            return

        if payload.emoji.name in associations:
            user = payload.member
            role = nextcord.utils.get(message.guild.roles, name=associations[payload.emoji.name])

            await user.add_roles(role)
