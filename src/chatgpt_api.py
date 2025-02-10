# # устаревший способ вызова API OpenAI (ошибка APIRemovedInV1)

# import openai

# # Замените на ваш API-ключ
# OPENAI_API_KEY = "ключ сюда"

# # Функция для общения с ChatGPT-4o-mini
# def ask_gpt(prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-4o-mini",  # Используем модель 4o-mini
#         messages=[{"role": "user", "content": prompt}],
#         api_key=OPENAI_API_KEY  # Передаём API-ключ
#     )
#     return response["choices"][0]["message"]["content"]

# # Тестовый запрос
# user_input = "Привет, расскажи шутку!"
# answer = ask_gpt(user_input)
# print("Ответ от ChatGPT:", answer)
#......................................................................................

# Современный способ вызова:
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Берем ключ из окружения

# Устанавливаем API-ключ
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Функция для общения с ChatGPT-4o-mini
def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Используем модель 4o-mini
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Тестовый запрос
user_input = "Привет, расскажи шутку!"
answer = ask_gpt(user_input)
print("Ответ от ChatGPT:", answer)
#......................................................................................


# # Проверка баланса:
# import openai

# OPENAI_API_KEY = "ключ сюда"

# client = openai.OpenAI(api_key=OPENAI_API_KEY)

# try:
#     balance = client.billing.usage()  # Запрос баланса
#     print("Баланс OpenAI API:", balance)
# except Exception as e:
#     print("Ошибка:", e)
#......................................................................................









