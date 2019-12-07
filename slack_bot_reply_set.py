import datetime
import re
from slackbot.bot import respond_to
set_date = ''
limit_date = ''

@respond_to('設定')
def reply_set(message):
    message.reply('更新日時:"yyyy/mm/dd"形式')

@respond_to('あと何日')
def reply_when(message):
    global set_date
    global limit_date

    if set_date == '' :
        message.reply('更新日が設定されていません')
    else :
        limit_day = (datetime.datetime.today() - limit_date)
        if 0 > limit_day.days :
            message.reply('更新期限まであと:' + str(abs(limit_day.days)) + '日')
            message.reply('更新期限:' + limit_date.strftime('%Y/%m/%d'))
        else :
            message.reply('期限切れ')
            message.reply('更新期限:' + limit_date.strftime('%Y/%m/%d'))

@respond_to('(.*)')
def reply_new_date(message,arg):
    global set_date
    global limit_date
    
    date_pattern = re.compile('(\d{4})/(\d{1,2})/(\d{1,2})')
    result = date_pattern.search(arg)

    if result:
        set_date = datetime.datetime.strptime(arg, '%Y/%m/%d')
        limit_date = set_date + datetime.timedelta(days=42)
        message.reply('更新日:' + set_date.strftime('%Y/%m/%d'))
        message.reply('更新期限:' + limit_date.strftime('%Y/%m/%d'))
