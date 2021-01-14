# by Vladislav or Rustan2287
import logging
import time
import os
import requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'your token'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#приветствие
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer("привет я бот для оповещения о выходе манги  \"Девушка на час\"")
    await get(message)

#берется html файл и создается кэш
async def get(message: types.Message):
    r = requests.get("https://readmanga.live/kanojo__okarishimasu").text
    file = open("site.html", 'w', encoding=("utf8"))
    for index in r:
        file.write(index)
    file.close
    url = open("site.html", encoding=("utf8"))
    soup = BeautifulSoup(url, 'lxml')
    kanojo = soup.find("table", class_="table table-hover").text
    f = open("manga.txt", 'w', encoding=("utf8"))
    for j in kanojo:
        f.write(j)
    f.close()
    await sammer(message)

#проверка
async def sammer(message: types.Message):
    n = os.path.getsize("manga.txt")
    m = os.path.getsize("kanojo.txt")
    if n == m:
        time.sleep(1)
        await get(message)
    else:
        await message.answer("Вышла новая глава манги Девушка на час")
        await message.answer("https://readmanga.live/kanojo__okarishimasu")
        h = open("manga.txt", encoding=("utf8"))
        file = open("kanojo.txt", 'w', encoding=("utf8"))
        for z in h:
            file.write(z)
        file.close()
        h.close()
        await get(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
