import pyupbit

coin_lists = pyupbit.get_tickers(fiat="KRW")
print(coin_lists)

print_now = pyupbit.get_current_price(["KRW-BTC", "KRW-ETH"])
print(print_now)
