from aiogram import Bot, Dispatcher, executor
from aiogram.types import *
from core.config import TOKEN, ADMIN_ID, URL, DOMAIN
from core.utils import get_title_for_json_file
from core.inline import start_inline_button 
from os import system
system("clear")

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


@dp.message_handler(commands = "start")
async def start(message: Message):
    await message.answer(f"Привет", reply_markup=start_inline_button)


@dp.inline_handler()
async def inline_query(zapros_polzovatelya: InlineQuery):
    text = zapros_polzovatelya.query
    results = get_title_for_json_file(text)

    articles = []
    ar_id = 0

    for result in results:
        ar_id += 1

        article = InlineQueryResultArticle(
            id = ar_id,
            title = f"{result['title']}",
            description = f"{result['movie']}",
            # url= f"{result['url']}",
            # hide_url= True,
            thumb_url = f"{result['img']}",


            input_message_content = InputTextMessageContent(
                message_text = f"""<b>Заголовок:</b> {result['title']}
                <b> Тип:</b>  {result['movie']}
                <b> Информация </b> {result ['genre']},{result['country']}
                <b>Год: </b> {result['year']}
                <b>Подробнее </b> <a href='{result['url']}'> Нажмите тут </a>"""
            ) 
        )
        articles.append(article)
        if len(articles) == 50:
            break
    await zapros_polzovatelya.answer(articles, cache_time = 1, is_personal=True)



if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except(KeyboardInterrupt, SystemExit):
        pass