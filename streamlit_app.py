# This app is for educational purpose only. Insights gained is not financial advice. Use at your own risk!
import streamlit as st
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json
import time

import json
import random
import statistics
import statistics as stat
import time
from csv import writer

import oandapyV20
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.orders as orders
import pandas as pd
import v20
from scipy import stats
from scipy.stats import kendalltau
from scipy.stats import spearmanr
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import RandomForestRegressor

balance = 0

st.set_page_config(layout="wide")

st.title('SaibonFX DashBoard')
st.markdown("""
This app displays key metrics for SBFX clients.
""")

st.write('Saibontest')
expander_bar = st.expander("About")
expander_bar.markdown("""
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn, BeautifulSoup, requests, json, time
* **Data source:** [SaibonFX](https://www.vybesllc.com/).
* **Credit:** SaibonFX *[Web Scraping Crypto Prices With Python](https://www.vybesllc.com/).
""")

# ---------------------------------#
# Page layout (continued)
## Divide page to 3 columns (col1 = sidebar, col2 and col3 = page contents)
col1 = st.sidebar
col2, col3, col4, col5, col6 = st.columns((2, 1, 2, 1, 2))

# ---------------------------------#
# Sidebar + Main panel
col1.header('App location Options')

## Sidebar - Currency price unit
currency_price_unit = col1.selectbox('Select sbfx location', ('Assets', 'Trade', 'Pay', 'Notification', 'Invite'))

RFEE = []
Euler = 0
ret = 0
her = 0
Sbfx = 0
svmp = []
Quant = 0
Sb = 0
wer = 0
EUL1 = 0
D1 = 0
tg1 = 0
Fs = 0
RF = []
TG = []
TW = []
TQ = []
trade = []
returns = []
TV = []
PV = []
T1 = 0
Sbf = 0
db = []
Speed = 1
Time = 1
t0 = 0
UC = 1
t1 = 0
EurUsd = [1.1800]
Area = 0
Chart = []
Long = 0
Short = 0
Ticks = 0
Distance = 1
D = []
BR = []
EUL = []
AREA = []
LT = []
ST = []
SBFX = []
T = []
S = []
SP = []
ST1 = 0
Exitl = 0
wer1 = 0
r = 0
wer = 0
her = 0
balance = 0
NAV = 0
Exits = 0
AREA1 = 0
SBFX1 = 0
LT1 = 0
EP = [1, 1]
sp = 0
ep = 0
LongTrend = 0
ShortTrend = 0
counter = 0
my_series = 0
last = 1
prev = 1
TP = 100
TickBar = 0
E, U = 'EURUSD', 'USDCHF'

API = 'api-fxtrade.oanda.com'
ACCESS_TOKEN = \
    '65977df04d32049a40a9b64cb802ca6a-80ebe64ef60de9d9cfd787ef204a1966'
ACCOUNT_ID = '001-001-7053810-001'
client = oandapyV20.API(environment='live',
                        access_token='65977df04d32049a40a9b64cb802ca6a-80ebe64ef60de9d9cfd787ef204a1966'
                        )

api = v20.Context(hostname=API, token=ACCESS_TOKEN, port=443, ssl=True)

data = {'order': {'instrument': 'GBP_CAD', 'units': '-100', 'type': 'MARKET', 'positionFill': 'DEFAULT'}}
data1 = {'order': {'instrument': 'EUR_NZD', 'units': '100', 'type': 'MARKET', 'positionFill': 'DEFAULT'}}
data2 = {'order': {'instrument': 'EUR_USD', 'units': '4', 'type': 'MARKET', 'positionFill': 'DEFAULT'}}
data3 = {'order': {'instrument': 'EUR_USD', 'units': '8', 'type': 'MARKET', 'positionFill': 'DEFAULT'}}
data4 = {'order': {'instrument': 'EUR_USD', 'units': '16', 'type': 'MARKET', 'positionFill': 'DEFAULT'}}
data5 = {'order': {'instrument': 'EUR_USD', 'units': '32', 'type': 'MARKET', 'positionFill': 'DEFAULT'}}
data6 = {'order': {'instrument': 'EUR_USD', 'units': '64', 'type': 'MARKET', 'positionFill': 'DEFAULT'}}
data7 = {'order': {'instrument': 'EUR_USD', 'units': '128', 'type': 'MARKET', 'positionFill': 'DEFAULT'}}
data8 = {'order': {'instrument': 'EUR_AUD', 'units': '-1', 'type': 'MARKET', 'positionFill': 'DEFAULT'}}
data9 = {'order': {'instrument': 'AUD_CHF', 'units': '-1', 'type': 'MARKET', 'positionFill': 'DEFAULT'}}
data10 = {'order': {'instrument': 'GBP_CAD', 'units': '-900', 'type': 'MARKET', 'positionFill': 'DEFAULT'}}
data11 = {'order': {'instrument': 'EUR_NZD', 'units': '-3', 'type': 'MARKET', 'positionFill': 'DEFAULT'}}

B1 = orders.OrderCreate(ACCOUNT_ID, data=data)
B2 = orders.OrderCreate(ACCOUNT_ID, data=data1)
B3 = orders.OrderCreate(ACCOUNT_ID, data=data2)
B4 = orders.OrderCreate(ACCOUNT_ID, data=data3)
B5 = orders.OrderCreate(ACCOUNT_ID, data=data4)
B6 = orders.OrderCreate(ACCOUNT_ID, data=data5)
B7 = orders.OrderCreate(ACCOUNT_ID, data=data6)
B8 = orders.OrderCreate(ACCOUNT_ID, data=data7)
B9 = orders.OrderCreate(ACCOUNT_ID, data=data8)
B10 = orders.OrderCreate(ACCOUNT_ID, data=data9)
S1 = orders.OrderCreate(ACCOUNT_ID, data=data10)
S2 = orders.OrderCreate(ACCOUNT_ID, data=data11)

@st.cache
def b1():
    client.request(B1)
    print(B1.response)


def b2():
    client.request(B2)
    print(B2.response)


def b3():
    client.request(B3)
    print(B3.response)


def b4():
    client.request(B4)
    print(B4.response)


def b5():
    client.request(B5)
    print(B5.response)


def b6():
    client.request(B6)
    print(B6.response)


def b7():
    client.request(B7)
    print(B7.response)


def b8():
    client.request(B8)
    print(B8.response)


def b9():
    client.request(B9)
    print(B9.response)


def b10():
    client.request(B10)
    print(B10.response)


def s1():
    client.request(S1)
    print(S1.response)


def s2():
    client.request(S2)
    print(S2.response)


EurCsvTransform = []
A1 = [1, 1]
A2 = []
A3 = []
APV = [1, 1, 1, 1, 1, 1, 1]
f2 = []
Base = 0
Tvalue = 1
Pvalue = 1
TV1 = 0
PV1 = 0
Volatility = 0
f3 = []
f8 = [1, 1]
c = 0
output = 0
clog = []
sp = 0
fin = 0
while True:
    www = random.uniform(1, 100)
    c = c + www
    sp = sp + 1
    clog.append(c)
    if sp > 2:
        start = clog[-1]
        end = clog[-2]
        fin = start - end
    try:
        USDCHF = api.pricing.get(accountID=ACCOUNT_ID, instruments='EUR_NZD')
        USDCHF = json.loads(USDCHF.body['prices'][0].json())
        UC = USDCHF['closeoutBid']
        CU = USDCHF['closeoutAsk']
        EURUSD = api.pricing.get(accountID=ACCOUNT_ID, instruments='AUD_CAD')
        EURUSD = json.loads(EURUSD.body['prices'][0].json())
        EU = EURUSD['closeoutBid']
        UE = EURUSD['closeoutAsk']
        r = accounts.AccountDetails(ACCOUNT_ID)
        wer1 = client.request(r)
        wer = wer1["account"]["positions"][-13]["unrealizedPL"]
        her = wer1["account"]["openTradeCount"]
        her = float(her)
        wer = float(wer)
        balance = wer1["account"]["balance"]
        balance = float(balance)
        NAV = wer1["account"]["NAV"]
        NAV = float(NAV)
    except Exception:
        pass
    wer = wer1["account"]["positions"][0]["unrealizedPL"]
    her = wer1["account"]["openTradeCount"]
    her = float(her)
    wer = float(wer)

    lunits = wer1["account"]["positions"][0]["long"]["units"]
    sunits = wer1["account"]["positions"][0]["short"]["units"]
    lunits = float(lunits)
    sunits = float(sunits)
    units = lunits + sunits
    st.write('Current Units ', units)


    balance = wer1["account"]["balance"]
    balance = float(balance)
    st.write('The balance is ', balance)

    NAV = wer1["account"]["NAV"]
    NAV = float(NAV)
    st.write('The NAV is ', NAV)

    pl = wer1["account"]["pl"]
    pl = float(pl)
    st.write('The pl is ', pl)

    mu = wer1["account"]["marginUsed"]
    mu = float(mu)
    st.write('The marginUsed is ', mu)

    import numpy as np

    mu = int(mu)
    pl = int(pl)
    df = pd.DataFrame((mu, pl), columns=('col %d' % i for i in range(1)))
    # st.dataframe(df.style.highlight_max(axis=0))

    st.altair_chart(df)


    @st.cache
    def convert_df(df):

        return df.to_csv().encode('utf-8')


    csv = convert_df(df)

    st.download_button(label="Download data as CSV", data=csv, file_name='large_df.csv', mime='text/csv', key=www)

    with st.spinner('Wait'):
        time.sleep(8)
        st.success('Done!')
    continue

#
