import nsepy
import pprint
import pandas as pd
symbol="IBREALEST"
data=nsepy.get_quote(symbol)['data'][0]
pprint.pprint(data['pChange'])