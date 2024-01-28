from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault



"""
if i'm not mistaken
    create bot command: BotCommand, 
    draw those command in "Menu"(pop up menu): BotCommandScopeDefault
"""


async def set_commands(bot: Bot):

    commands = [
        BotCommand(
            command="start",
            description="Bot's start"
        ),
        BotCommand(
            command="help",
            description="Help with something"
        ),
        BotCommand(
            command="description",
            description="Bot's description" 
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())