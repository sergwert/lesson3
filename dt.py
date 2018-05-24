from datetime import datetime, date, timedelta

def print_dt():
    dt_now=datetime.now()
    delta_day=timedelta(days=1)
    delta_mon=timedelta(days=30)
    dt_tomorrow=dt_now+delta_day
    dt_yesterday=dt_now-delta_day
    dt_prev_mon=dt_now-delta_mon
    print('Вчера: '+dt_yesterday.strftime('%d.%m.%Y'))
    print('Сегодня: '+dt_now.strftime('%d.%m.%Y'))
    print('Завтра: '+dt_tomorrow.strftime('%d.%m.%Y'))
    print('Месяц назад: '+dt_prev_mon.strftime('%d.%m.%Y'))

def str_to_dt():
    str="01/01/17 12:10:03.234567"
    dt=datetime.strptime(str, '%d/%m/%y %H:%M:%S.%f')
    print('Исходная строка приведена к типу: ')
    print(type(dt))

if __name__=="__main__":
    print_dt()
    str_to_dt()