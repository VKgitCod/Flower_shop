import telebot
from orders.models import Order

BOT_TOKEN = '7947334919:AAG0pQRxgkHJUaACKkrb6bxOaJifbuHS8zc'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Добро пожаловать! Здесь вы будете получать уведомления о новых заказах.")

def send_order_notification(order_id):
    order = Order.objects.get(id=order_id)
    message = f"Новый заказ #{order.id} от {order.user.username}:\nАдрес доставки: {order.delivery_address}\n"
    for product in order.products.all():
        message += f"- {product.name} ({product.price}₽)\n"
    bot.send_message(ADMIN_TELEGRAM_ID, message)
