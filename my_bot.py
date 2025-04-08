from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Функция обработки команды /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет! Отправь мне список слов через пробел, и я выведу их через запятую.')

# Функция обработки текста
async def process_words(update: Update, context: CallbackContext) -> None:
    # Получаем текст сообщения пользователя
    user_input = update.message.text

    # Разделяем текст на слова по пробелам
    words = user_input.split()

    # Функция для разбиения массива на части по 20 элементов
    def chunk_array(arr, chunk_size):
        return [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

    # Разделим на массивы по 20 элементов
    chunked_list = chunk_array(words, 20)

    for chunk in chunked_list:
        output = ', '.join(chunk)
        await update.message.reply_text('Слова через запятую:')
        await update.message.reply_text(f'{output} ')


    #await update.message.reply_text(f'Слова через запятую: {output} {len(words)}')


# Основная функция для запуска бота
def main():
    # Вставьте сюда ваш токен, полученный от BotFather
    token = '7509615548:AAG2SCa3rIk7tCRQeNgzKL3BCPcOyVYg-_w'  # Замените на ваш токен

    # Создаем объект Application и передаем токен
    application = Application.builder().token(token).build()

    # Регистрируем обработчики
    application.add_handler(CommandHandler('start', start))  # Обработчик команды /start
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_words))  # Обработчик текстовых сообщений

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
