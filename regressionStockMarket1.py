import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import quandl, math, warnings, datetime, pickle
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
from matplotlib import style


#style.use('fivethirtyeight')
style.use('ggplot')
#warnings.filterwarnings("always")
#quandl.ApiConfig.api_key = '2R5mRdjANBMYxXK_sy3d'

#df = quandl.get('EIA/PET_RWTC_D', returns='numpy')

####df = quandl.get('WIKI/GOOGL')
####df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
####df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
####df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
####df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

df = quandl.get('CHRIS/CME_M6E1', collapse='daily', paginate=True)
df = df[['Open', 'High', 'Low', 'Last', 'Volume']]
df['HL_PCT'] = (df['High'] - df['Last']) / df['Last'] * 100.0
df['PCT_change'] = (df['Last'] - df['Open']) / df['Open'] * 100.0
df = df[['Last', 'HL_PCT', 'PCT_change', 'Volume']]

forecast_col = 'Last'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.003*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)


X = np.array(df.drop(['label'],1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)
y = np.array(df['label'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)

##with open('linearregression.pickle', 'wb') as f:
##    pickle.dump(clf, f)

##pickle_in = open('linearregression.pickle', 'rb')
##clf = pickle.load(pickle_in)

accuracy = clf.score(X_test, y_test)
forecast_set = clf.predict(X_lately)
print(forecast_set, accuracy, forecast_out)
df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['Last'].plot()
df['Forecast'].plot()
#plt.legend(loc=4)
#plt.xlabel('Date')
#plt.ylabel('Price')
#plt.show()

print(df.head())
print(df.tail())

