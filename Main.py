import logging

from telegram.ext import *
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

TELEGRAM_HTTP_API_TOKEN = '1144634373:AAF7iX0Lyt1k5Mb3Oa-puPAe-N89ZBM7vvY'

CHECK_MES = 0


class Forward_message:
    def __init__(self):
        self.__index = 0
        self.__chat = 0

    def return_message(self, update, context):
        self.__chat = update.message.chat.id
        self.__index = update.message.message_id
        # self.forward(update, context)
        myfile = open("Users.txt", "a")
        myfile.write(
            "{} {} {} {}\n".format(
                update.message.from_user.id,
                update.message.from_user.first_name,
                update.message.from_user.last_name,
                update.message.from_user.username)
        )
        myfile.close()


    def forward(self, update, context, **kwargs):
        context.bot.forward_message(
            chat_id=self.__chat,
            from_chat_id=self.__chat,
            message_id=int(self.__index)-1,
            disable_notification=False, timeout=None, **kwargs
        )


    def main(self):
        updater = Updater(TELEGRAM_HTTP_API_TOKEN, use_context=True)
        dispatcher = updater.dispatcher

        control_handler = ConversationHandler(
            entry_points=[
                CommandHandler('start', self.return_message),
                MessageHandler(Filters.all, self.return_message),

            ],
            states={
                CHECK_MES: [
                    MessageHandler(Filters.all, self.return_message),
                ],
            },
            fallbacks=[
                MessageHandler(Filters.all, self.return_message),
            ]
        )

        dispatcher.add_handler(control_handler)
        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    forward_massage = Forward_message()
    forward_massage.main()
