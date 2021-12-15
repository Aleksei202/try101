from datetime import datetime

date_row = input('Enter data in format YYYY-MM-DD')
try:
    date_formatted = datetime.strptime(date_row, '%Y-%m-%d')
except ValueError:
    print('Yours input', date_row, 'does not match with format YYYY-MM-DD')

print(date_formatted)