# Телеграм бот для получения курса криптовалют

## Список библиотек и их версий: 
aiofiles==23.2.1\n
aiogram==3.3.0
aiohttp==3.9.1
aiosignal==1.3.1
annotated-types==0.6.0
attrs==23.2.0
certifi==2023.11.17   
charset-normalizer==3.3.2
frozenlist==1.4.1
idna==3.6
magic-filter==1.0.12
multidict==6.0.4
pydantic==2.5.3
pydantic_core==2.14.6
requests==2.31.0
typing_extensions==4.9.0
urllib3==2.1.0
yarl==1.9.4

## Использование 
Использование бота:
1. Регистрация (команда /start)
2. Выбор операции:
    2.1 Посмотреть список криптовалют
    2.2 Посмотреть цену криптовалюты
3. Ввод валюты и получение ее стоимости


## Установка:
1. git clone ...
2. pip install ...
3. Указать в data/config.py токен бота и название базы данных 
4. Указаьб в utils/api/fetch_data_api.py API ключ (сллылка на регистрацию: https://rapidapi.com/topapi-topapi-default/api/cryptocurrency-news2/)

