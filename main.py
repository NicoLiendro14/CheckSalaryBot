from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import check_salary
import logging
import os
import settings

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = settings.TOKEN
PORT = int(os.environ.get('PORT', '8443'))


def get_salary(update, context):
    input_salary = context.args[0]
    actual_salary = check_salary.get_salary(input_salary)
    converted_salary = check_salary.convert_salary(actual_salary)
    update.message.reply_text("Tu salario es de: " + str(converted_salary))


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('get_salary', get_salary))
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.set_webhook("https://checksalarybot.herokuapp.com/" + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()
