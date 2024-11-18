import pandas_datareader.data as pdr
from datetime import datetime

def fetch_us_cpi():
    start_date = "2010-01-01"
    end_date = datetime.now().strftime('%Y-%m-%d')
    cpi_data = pdr.DataReader('CPIAUCSL', 'fred', start_date, end_date)
    return cpi_data

def calculate_inflation(cpi_data):
    cpi_data['CPI_Change'] = cpi_data['CPIAUCSL'].pct_change(periods=3)*100
    last_4_quarters = cpi_data['CPI_Change'].dropna().iloc[[-1, -4, -7, -10]]
    return last_4_quarters
