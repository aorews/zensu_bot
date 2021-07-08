from database import db_query
from bot_functions import bot_message_to_chat


def plus(update, context):
    THRESHOLD = 3
    AUTODESTRUCTION = 10
    print(update)
    chat_id = update.effective_message.chat.id
    replied_message = update.message.message_id
    user_id = update.effective_user.id

    to_chat_ids = db_query(
            f"select parent from chats_connection where child = {chat_id}"
        )
    
    print(to_chat_ids)

    if len(to_chat_ids) == 0:
        return None

    cur_amount, has_voted = db_query(
        f"""select count(1) + 1, coalesce(sum(case when user_id = {user_id} then 1 else 0 end), 0) 
            from plus_data 
            where chat_id = {chat_id} and message_id = {replied_message}"""
    )[0]

    print(cur_amount, has_voted)

    if has_voted != 0:
        text = "Ты уже голосовал, грязный и мерзкий!"
        bot_message_to_chat(context, chat_id, AUTODESTRUCTION, update.message.message_id,
        )
        return None

    if cur_amount == THRESHOLD:
        for chat in to_chat_ids:
            context.bot.copy_message(
                chat_id=chat[0], from_chat_id=chat_id, message_id=replied_message
            )

    elif cur_amount < THRESHOLD:
        post_to = db_query(f"select title from chats where id = {chat_id}")[0][0]
        text = f"{cur_amount} из {THRESHOLD} + до поста в {post_to}"
        bot_message_to_chat(context, chat_id, text, AUTODESTRUCTION, replied_message)

        db_query(
            f"insert into plus_data (chat_id, message_id, user_id) values ({chat_id}, {replied_message}, {user_id})",
            False,
        )

    else:
        text = "Пост уже отправлен!"
        bot_message_to_chat(context, chat_id, text, AUTODESTRUCTION, replied_message)

    return None
