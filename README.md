# Check Salary Bot

Telegram bot that converts Chilean pesos into Argentine pesos using the value from the website global66.com 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the bot and how to install them

```
Python 3
```

You have to install dependencies that ```requirements.txt``` contains.

```
pip install -r requirements.txt
```

Create a copy of your .env file

```
cp .env.example .env
```
'YOUR TOKEN' should be replaced by the API token you received from @BotFather. Visit [Introduction to the API](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API) to see how to get that token and more information.
```
TOKEN="YOUR TOKEN"  
```

Actually, the bot run using WebHook so if you want to run locally you have to use polling instead of WebHook. Change this code:
```
updater.start_webhook(listen="0.0.0.0",
                           port=PORT,
                         url_path=TOKEN)
    updater.bot.set_webhook("https://checksalarybot.herokuapp.com/" + TOKEN)
```
to:
```
updater.start_polling()
```

### Installing

You only have to run the main.py file:

```
python3 main.py
```
### How to use and example

Put ```/get_salary 'your salary in Argentine pesos'``` and the bot will return your salary converted to Chilean pesos.

<img src="https://i.imgur.com/PxbYFdo.png"/>

## Built With

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - This library provides a pure Python interface for the Telegram Bot API.

## Author

- **Nicolás Liendro** - _Initial work_ - [GitLab](https://gitlab.com/NicoLiendro14),
  [GitHub](https://github.com/NicoLiendro14) and
  [LinkedIn](https://www.linkedin.com/in/nicol%C3%A1s-liendro-00248a178/)
