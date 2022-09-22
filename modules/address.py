import pandas as pd
from multiprocessing import Pool
import defs
 
def address(df_address):
    df_address['query'] = df_address[['lat','long']].apply(lambda x: str(x['lat']) + ',' + str(x['long']), axis=1)
    df1 = df_address[['id','query']]
    p = Pool(3) 
    df1[['road', 'house_number']] = p.map( defs.get_adress, df1.iterrows())
    return df1

if __name__ == "__main__":
    df = pd.read_csv("data/kc_house_data.csv")
    df1 = address(df)
    df1.to_csv('data/address.csv', index=False)
