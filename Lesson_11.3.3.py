from datetime import datetime

date_row = input('Enter data in format YYYY-MM-DD')
try:
    date_formatted = datetime.strptime(date_row, '%Y-%m-%d')
except ValueError:
    print('Yours input', date_row, 'does not match with format YYYY-MM-DD')

week = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
    }
print(week[date_formatted.weekday()])
