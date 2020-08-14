import pandas as pd
import matplotlib.pyplot as plt
import re

#csv file to read
IN_FILE = "output.csv" 
COLS = ['A', 'B', 'C', 'D'] #Prices, Title, Dates, URL

df = pd.read_csv(IN_FILE, sep=',', names=COLS, parse_dates=['C'])

df['A'] = df['A'].str.replace('^\\D*', '').astype('str') #rm leading chars, ret str
df['A'] = df['A'].str.replace(',', '').astype('float') #rm comma, ret float

df.plot(kind='scatter', x='C', y='A')
plt.show()
