from datetime import datetime
import pandas as pd

def transform_data(df):
    df['address'] = df['address'].str.replace('\n', ', ')
    df['phone_number'] = df['phone_number'].str.replace(r'\D', '', regex=True)
    df['age'] = df['birthdate'].apply(lambda x: datetime.now().year - pd.to_datetime(x).year)
    df = df[df['age'] >= 21]
    return df
