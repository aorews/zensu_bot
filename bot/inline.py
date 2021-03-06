"""Base for inline functions which are now not used because of their infrequent updates"""
from uuid import uuid4

from telegram import InlineQueryResultArticle, InputTextMessageContent, ParseMode

from commands import get_stat

def inline_stat(update, context) -> None:
    """Handle the inline query."""
    query = update.inline_query.query

    if query == "":
        update.inline_query.answer(
            [
                InlineQueryResultArticle(
                    id=str(uuid4()),
                    title="Получить статистику по пятидневкам",
                    input_message_content=InputTextMessageContent(
                        f"{get_stat(update)}", parse_mode=ParseMode.HTML, disable_web_page_preview = True
                    ),
                    thumb_url="https://i.imgur.com/2G1ZxcU.jpeg",
                    thumb_height=100,
                    thumb_width=100
                )
            ]
        )
