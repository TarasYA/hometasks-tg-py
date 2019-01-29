"""
Config file
"""
import os

KEY = """https://maker.ifttt.com/trigger/updated_price/with/key/""" + os.getenv("MARKET")
API_URL = 'https://api.coinmarketcap.com/v1/ticker/{}/'
