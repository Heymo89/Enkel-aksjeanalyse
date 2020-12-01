import yfinance as yf
import pandas as pd

#df = pd.read_csv('')

#amerikansk marked
#søk på ['Symbol']
df = pd.read_csv('test_portofolie.csv')

print(df)

#Liste over askjenavn som har økt
okte_navn = []

for stock in df['Symbol']:
    stock = stock.upper()
    if '^' in stock:
        pass
    try:
        stock_info = yf.Ticker(stock)
        hist = stock_info.history(period="5d")
        previous_averaged_volume = hist['Volume'].iloc[1:4:1].mean()
        todays_volume = hist['Volume'][-1]
        if todays_volume > previous_averaged_volume *1.05:
            okte_navn.append(stock)
    except:
        pass

for stock in okte_navn:
    print(stock)
