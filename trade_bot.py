"""
Trade bot
"""
from datetime import datetime
from threading import Thread
import time
import requests
from config import KEY, API_URL

# Config data
BITCOIN_API_URL = API_URL
IFTTT_WEBHOOKS_URL = KEY


def get_price(name, pr_val='price_usd'):
    """
    getting coin price
    """
    response = requests.get(BITCOIN_API_URL.format(name))
    response_json = response.json()
    return float(response_json[0][pr_val])


def post_ifttt_webhook(event, text, name):
    """
    sending email
    """
    data = {'value1': str(name), 'value2': str(text)}
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
    requests.post(ifttt_event_url, json=data)


def format_history(history):
    """
    formatting text
    """
    rows = []
    for price in history:
        date = price['date'].strftime('%d.%m.%Y %H:%M')
        price = price['price']
        row = '{}: $<b>{}</b>'.format(date, price)
        rows.append(row)

    return '<br>'.join(rows)


class GetterThread(Thread):
    """
    Creating threads to make a lot of cryptocurrency notifications
    """
    def __init__(self, name):
        """
        Initializing components
        """
        super(GetterThread, self).__init__()
        self.name = name
        self.history = []
        self.month_c = 1
        self.week2_c = 1
        self.changed_pr = 0

    def run(self):
        """
        Running thread
        """
        update_s = '{} price update'
        changed_s = '{} {} changed(if minus value, cryptocurrency price is going down)'
        name = self.name + ' {} price update'

        while True:
            price = get_price(self.name.lower())
            date = datetime.now()
            self.history.append({'date': date, 'price': price})

            post_ifttt_webhook(update_s.format(self.name), format_history(self.history),
                               name.format('weekend'))

            if len(self.history) == 51:
                self.changed_pr = self.history[50]['price'] \
                                  - self.history[0]['price']
                post_ifttt_webhook(update_s.format('1 Year ' + self.name),
                                   changed_s.format('1 Year ' + self.name, self.changed_pr),
                                   name.format('1 Year'))

                self.week2_c = 0
                self.month_c = 0
                self.history = []
            elif len(self.history) % 4 == 0:
                self.month_c += 1

                self.changed_pr = self.history[(4 * self.month_c) - 1]['price'] \
                                  - self.history[0]['price']
                post_ifttt_webhook(update_s.format('1 Month ' + self.name),
                                   changed_s.format('1 Month ' + self.name, self.changed_pr),
                                   name.format('1 Month'))
            elif len(self.history) % 2 == 0:
                self.week2_c += 1

                self.changed_pr = self.history[(2 * self.week2_c) - 1]['price'] \
                                  - self.history[0]['price']
                post_ifttt_webhook(update_s.format('2 Weeks ' + self.name),
                                   changed_s.format('2 Weeks ' + self.name, self.changed_pr),
                                   name.format('2 Weeks'))

            time.sleep(3600 * 60)


if __name__ == '__main__':
    THREAD_BIT = GetterThread('Bitcoin')
    THREAD_BIT.start()
    THREAD_ETH = GetterThread('Ethereum')
    THREAD_ETH.start()
