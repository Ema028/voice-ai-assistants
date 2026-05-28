import os
import openai
from dotenv import load_dotenv
from pydub import AudioSegment
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

load_dotenv()

client = openai.OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ.get("GROQ_API")
)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")


async def transcrever_audio_telegram(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ouvindo o áudio... Aguarde um momento.")

    if update.message.voice:
        file = await context.bot.get_file(update.message.voice.file_id)
    elif update.message.audio:
        file = await context.bot.get_file(update.message.audio.file_id)
    else:
        await update.message.reply_text("Por favor, me envie ou encaminhe um áudio.")
        return

    caminho_baixado = "audio_recebido.ogg"
    caminho_pedaco = "pedaco_audio.ogg"

    try:
        await file.download_to_drive(caminho_baixado)

        audio = AudioSegment.from_file(caminho_baixado)
        dez_minutos = 10 * 60 * 1000
        transcricao_completa = ""

        #cortar o aúdio por causa limite do whisper
        for i in range(0, len(audio), dez_minutos):
            pedaco = audio[i:i + dez_minutos]


            pedaco.export(caminho_pedaco, format="ogg")
            with open(caminho_pedaco, "rb") as chunk_file:
                transcricao = client.audio.transcriptions.create(
                    model="whisper-large-v3",
                    file=chunk_file
                )
                transcricao_completa += transcricao.text + " "

        #devolve o texto em pedaços para não quebrar o limite do telegram
        if transcricao_completa.strip():
            for x in range(0, len(transcricao_completa), 4000):
                await update.message.reply_text(transcricao_completa[x:x + 4000])
        else:
            await update.message.reply_text("Não consegui ouvir nada nesse áudio.")

    except Exception as e:
        await update.message.reply_text(f"Ocorreu um erro na transcrição: {e}")

    finally:
        try:
            if os.path.exists(caminho_baixado):
                os.remove(caminho_baixado)
            if os.path.exists(caminho_pedaco):
                os.remove(caminho_pedaco)
        except PermissionError:
            pass

if __name__ == '__main__':
    print("Bot ligado")
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.VOICE | filters.AUDIO, transcrever_audio_telegram))
    app.run_polling()