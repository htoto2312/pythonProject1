from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN ="5740888589:AAGtKQ5LQoFP9fCapM1egroWZ4jynKwop1w"  # Забираем значение типа str
ADMINS = "1215043680"  # Тут у нас будет список из админов
IP = "localhost"  # Тоже str, но для айпи адреса хоста

