<h1 align="center">translate bot</h1>

## Preparatory works
1. Setup [docker](https://docs.docker.com/get-docker/) and [docker compose v2](https://docs.docker.com/compose/cli-command/#installing-compose-v2);
2. Download the code:

```shell
https:
git clone https://github.com/redbull7214/translate_bot.git

ssh:
git clone git@github.com:redbull7214/translate_bot.git
```

3. Go to the project directory:
```shell
cd translate_bot
```
4. Create .env file with api key.
Example:
```shell
API_TOKEN = 'your bot token from botfather'
```


## How to run the local version

Start the docker containers:
```shell
docker compose up --build
```

## Поддерживаемые ботом команды:
```
/start - регистрация
/history - история сообщений (для зарегистрированных пользователей)
В ответ на любое сообщение в чат(на русском языке) бот вернет его перевод
```