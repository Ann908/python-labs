# 1. Отримати курси евро за попередній тиждень, вивести на екран дату + курс
# 2. З отриманого словника побудувати графік зміни курсу за тиждень

import json
import requests
import matplotlib.pyplot as plt

# URL for request https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250317&end=20250321&valcode=eur&json
response_data = requests.get('https://bank.gov.ua/NBU_Exchange/exchange_site?start=20250317&end=20250321&valcode=eur&json')

responce_list = json.loads(response_data.content)

exchange_date = []
rate_list = []
for item in responce_list:
    exchange_date.append(item['exchangedate'])
    rate_list.append(item['rate'])

print(exchange_date)
print(rate_list)

plt.plot(exchange_date, rate_list)
plt.suptitle('Changing rate for one week')
plt.ylabel('Rate')
plt.xlabel('Date')
plt.show()


