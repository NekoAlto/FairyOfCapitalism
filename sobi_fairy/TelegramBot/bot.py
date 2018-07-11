from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

DEBUG = True

if DEBUG is True:
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    logger = logging.getLogger(__name__)

BOT_TOKEN = '576453889:AAHWmOtjiKTJOjp2rzQplViVq1OveXWopmU'


def start(bot, update):
    update.message.reply_text('HI!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot"""
    updater = Updater()
