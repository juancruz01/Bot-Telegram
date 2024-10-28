import asyncio

from telegram import Update #nos va permitir estar actualizando nuestro para ver si resivio algun comando

from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN = "7726670264:AAF4Kd5AJ2UoSrGHlgBUMtfhCOeb-BZZarU"

USUARIO = "@Jadx_Bot"

#funciones asincronas nos permite que el codigo espere ciertas operaciones sin bloquear a otra

#-----------------------------------------------------------#
#CHAT_ID TELEGRAM
"""
async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat.id
    print(f"El chat_id del grupo es: {chat_id}")
"""
#-----------------------------------------------------------#
#comando del tipo slash ( / )
#-----------------------------------------------------------#
async def inicio(update: Update, context : ContextTypes.DEFAULT_TYPE):
    #await: significa que el programa tiene que esperar a que se cumpla lo que esta dentro del codigo
     await update.message.reply_text("Hola, Bienvenido!")

async def help_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
    #await: significa que el programa tiene que esperar a que se cumpla lo que esta dentro del codigo
     await update.message.reply_text("¿Como te puedo ayudar?")

async def redes(update : Update, context : ContextTypes.DEFAULT_TYPE):
    #await: significa que el programa tiene que esperar a que se cumpla lo que esta dentro del codigo
     await update.message.reply_text("https://linktr.ee/putenojada?fbclid=PAZXh0bgNhZW0CMTEAAabfogM-AawzyR6Vs7TasK__dby9JYtnvSQOy07I3u6oF38-vKNIyY9iDWY_aem_gaHde8vb81qGzvgiI7blVg")

async def fansly(update : Update, context : ContextTypes.DEFAULT_TYPE):
    #await: significa que el programa tiene que esperar a que se cumpla lo que esta dentro del codigo
     await update.message.reply_text("https://fansly.com/Putenojada")

# Comando para "/ultimopost"
async def ultimopost(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Aquí está el último contenido: [https://www.instagram.com/p/DBQEgbSsmpL/]")
#------------------------------------------------------------#

#mesaje temporales de redes (intervalo cada 5 horas)
#------------------------------------------------------------#

messages = [
    "Visiten mi instagram! https://www.instagram.com/putenojada/",
    "Miren mi ultimo Tiktok! https://www.tiktok.com/@putenojada",
    "Siganme en mi Fansly para Divertinos https://fansly.com/Putenojada"
]

async def send_cyclic_messages(context: ContextTypes.DEFAULT_TYPE):
    if not hasattr(context, "message_index"):
        context.message_index = 0

    message = messages[context.message_index]

    await context.bot.send_message(chat_id="-4516195069", text=message)

    context.message_index = (context.message_index + 1) % len(messages)


#------------------------------------------------------------#
def respuesta(texto):
    texto = texto.lower()
    if "hola" in texto:
        return "hola!!"

    elif "adios" in texto:
        return "adios!!"

    elif "hermosa" in texto:
        return "Graciaas bby!!"
    
    elif "beautiful" in texto:
        return "thanks bby!!"
    elif "info" in texto:
        return "Hablame al privado / talk to md"
    
    else:
        return "No se que quieres decir"

#------------------------------------------------------------#

#------------------------------------------------------------#
async def mensajes_entrantes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tipo = update.message.chat.type
    texto = update.message.text

    if tipo == "group":
        if USUARIO in texto:
            texto_nuevo = texto.replace(USUARIO, "").strip()
            response = respuesta(texto_nuevo)
        else:
            return
    else:
        response = respuesta(texto)

    await update.message.reply_text(response)
#------------------------------------------------------------#

#------------------------------------------------------------#

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    #comando
    app.add_handler(CommandHandler("start",inicio))
    app.add_handler(CommandHandler("help",help_command))
    app.add_handler(CommandHandler("redes",redes))
    app.add_handler(CommandHandler("fansly",fansly))
    app.add_handler(CommandHandler("ultimopost",ultimopost))
    

    #chat_id
    #app.add_handler(MessageHandler(filters.ALL, get_chat_id))
    
    #Tarea repetitiva cada 5 horas
    app.job_queue.run_repeating(send_cyclic_messages, interval=5*60*60, first=0)
    
    #respuestas
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mensajes_entrantes))

    #acutalizacion del bot
    app.run_polling(poll_interval=2)