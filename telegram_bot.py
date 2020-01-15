# coding:utf-8
# Author : Negoo_wen
import telegram
bot = telegram.Bot(token='984081007:AAHY2mAAFh3EF-lly')
print bot.get_me()
info = bot.get_webhook_info()
print info
bot.send_message(chat_id='@testonet', text=str(bot.get_me()))

href = "https://baidu.com"
title = "嘿嘿嘿马"
#发送带标题网址链接
bot.send_message(chat_id='@testonet',
    text='<a href="http://slowread.net/monitor-hostloc/">HOSTLOC 交易贴提醒</a>.',
    parse_mode=telegram.ParseMode.HTML)
#发送无预览带标题网址链接
bot.send_message(chat_id='@testonet',
    text='<a href="' + href + '">' + title + '</a>.',
    parse_mode=telegram.ParseMode.HTML,
    disable_web_page_preview=True)
chat_id = '@testonet'
#其它文字样式
bot.send_message(chat_id=chat_id,
    text='<b>bold</b> <i>italic</i> <a href="http://google.com">link</a>.',
    parse_mode=telegram.ParseMode.HTML)
#发送图片
bot.send_photo(chat_id=chat_id,
    photo=open("115171338.png",'rb'))

bot.sendPhoto(chat_id = chat_id,
    photo=open("115171339.png",'rb'),
    caption="Sample photo Done")
