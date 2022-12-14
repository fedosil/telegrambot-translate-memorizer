# Translator and repeat telegram bot

#### Stack:

- [Python](https://www.python.org/downloads/)
- [iogram](https://docs.aiogram.dev/en/latest/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQlite3](https://www.sqlite.org/index.html)

## Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.

1. Firstly, create and activate a new virtual environment:
   ```bash
   python3.9 -m venv ../venv
   source ../venv/bin/activate
   ```
   
2. Install packages:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
   
3. Create a new bot with BotFather in telegram, get a token from it 

4. Add BOT_TOKEN with token value to environment variables or create a file .env with this variable

#### Connecting PostgreSQL:

1. Create PostgreSQL database
2. Change data_base/config.py
3. Change import in data_base/sql_db.py on:

   ```bash
   from data_base import postgesql_db as db
   ```