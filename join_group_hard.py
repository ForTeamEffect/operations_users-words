import random
import sqlite3
import time
import asyncio
from python_socks import ProxyType
from pprint import pprint
from pyrogram import Client

# Создание соединения с базой данных (если базы данных 'user.db' не существует, она будет создана)
conn = sqlite3.connect('user.db')
cursor = conn.cursor()

# Создание таблицы, если она еще не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY,
    api_id TEXT NOT NULL,
    api_hash TEXT NOT NULL,
    bot_token TEXT NOT NULL
)
''')


def add_user(api_id, api_hash, bot_token):
    cursor.execute("INSERT INTO user (api_id, api_hash, bot_token) VALUES (?, ?, ?)", (api_id, api_hash, bot_token))
    conn.commit()


# Пример добавления пользователя
# add_user("API_ID_1", "API_HASH_1", "BOT_TOKEN_1")

# Закрытие соединения с базой данных
conn.close()


# u3 = {"api_id": "29245102", "api_hash": "33da7c3b7a3eec1311951e4df57e1d86", "phone_number": "+212600376246"}
# user3 = Client(f'{u3["phone_number"]}',
#                u3["api_id"],
#                u3["api_hash"],
#                phone_number=u3["phone_number"])
#
u4 = {"api_id": "25648258", "api_hash": "1c69ef71a5c50c94c1a649c6fd327364", "phone_number": "+79891130433",}
      # 'my_proxy': {'scheme': "socks5", 'hostname': "185.181.247.121", 'port': 5501, 'username': "TG", "password": "proxysoxybot"}}
user4 = Client(f'{u4["phone_number"]}',
               u4["api_id"],
               u4["api_hash"],
               phone_number=u4["phone_number"],)
               # proxy=u4['my_proxy'])



text = '    Сальма Хайек в компании чаек — вчера самой горячей чиките Голливуда стукнуло 57'
print(len(text.split(' ')))
users = [user4]
# channel_list = [-1001126871063, -1001784551056, -1001521738843, -1001362421374,
#                 -1001340491832, -1001217929879, -1001736325790, -1001561871175,
#                 -1001180671955, -1001759640913, -1001471122080, -1001679289549,
#                 -1001509528650, -1001515639463]

channel_list = []
# channel_list = ['Helen_yes1', 'irena_ponaroshku', 'rina_sara', 'GALICH_onok',
#                 'Moms_Secrets_ru', 'keremoney', 'mama_2h', 'katerina_shikina',
#                 'ya_i_semya', 'lpetranovskaya', 'dvornikova_live', 'ta_mamasha',
#                 'rina_sara', 'velichkinaekaterina', 'usmanovakaterina', 'irapinchukofficial',
#                 'vikatresss_official', 'papiny_skazki_official', ]
with open('channel_names2.txt', 'r') as f:
    for line in f:
        name = line.strip()
        channel_list.append(name)
print(len(channel_list))
print(len(set(channel_list)))
unique_channel_list = set(channel_list)

already_joined_chats = []


async def gain():
    async with user4:
        async for dialog in user4.get_dialogs():
            already_joined_chats.append(dialog.chat.title or dialog.chat.first_name)
# asyncio.create_task(gain())
# удалить все каналы с 'i'
user4.run(gain())

def main():
    with open('channel_names2.txt', 'r+') as f:
        for user in users:
            user.start()
            # print(user.get_dialogs_count())
            # print(user.get_dialogs())
            # print(list(unique_channel_list)[:10])
        lines = f.readlines()
        # print(lines[:10])
        for channel in unique_channel_list:
            print(user.get_dialogs_count())
            print(already_joined_chats[:10])
            if channel+'\n' in lines:
                lines.remove(channel+'\n')
                f.seek(0)
                f.writelines(lines)
                if channel in already_joined_chats:
                    time.sleep(15)
                    continue
            for user in users:
                try:
                    print(channel)
                    user.join_chat(channel)

                except Exception as err:
                    print(err)
            time.sleep(random.randint(88, 255))
        for user in users:
            user.stop()


main()
# if you need take user info from db
# import time
# import sqlite3
# from pyrogram import Client
# import logging
#
# logging.basicConfig(level=logging.INFO)  # Настройка логирования
#
# DB_PATH = 'path_to_your_database.db'
# GROUPS_TO_JOIN = ["link_or_username1", "link_or_username2", ...]  # список из 100 групп
#
#
# def get_users_from_db():
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("SELECT user_id, api_id, api_hash FROM users")  # предполагаемая структура таблицы
#     users = cursor.fetchall()
#     conn.close()
#     return users
#
#
# def join_groups(user):
#     user_id, api_id, api_hash = user
#     session_name = f"user_{user_id}"
#
#     with Client(session_name, api_id=api_id, api_hash=api_hash) as app:
#         for group in GROUPS_TO_JOIN:
#             try:
#                 app.join_chat(group)
#                 logging.info(f"User {user_id} joined {group}")
#                 time.sleep(5)
#             except Exception as e:
#                 logging.error(f"User {user_id} couldn't join {group}. Error: {e}")
#
#
# def main():
#     users = get_users_from_db()
#
#     for user in users:
#         try:
#             join_groups(user)
#         except Exception as e:
#             logging.error(f"Error with user {user[0]}. Error: {e}")
# user2.get_chat()
# user1.
# Запускаем асинхронную функцию
# asyncio.run(channel_list)
