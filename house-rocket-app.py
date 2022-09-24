# HOUSE ROCKET APP
###################################################################################################################################################################################################
# LIBRARIES
import pandas as pd
import streamlit as st
import plotly.express as px
import os
###################################################################################################################################################################################################
# CONFIG
st.set_page_config(layout='wide') # page layout
st.title('House Rocket Company Insights') # page title
st.markdown('Welcome! In this page you will find tables, maps and insights for the House Rocket Company Project.') # intro
st.write('**Author: Bruno Di Franco Albuquerque**') # author
@st.cache(allow_output_mutation=True) 
###################################################################################################################################################################################################
# FUNCTIONS
###################################################################################################################################################################################################
# GET DATA
def get_all_data(path):
    path, dirs, files = next(os.walk(f"{path}"))
    dataframes_list = []

    for i in range(len(files)):
        temp_df = pd.read_csv(f"./{path}"+files[i])
        dataframes_list.append(temp_df) 
               
    return dataframes_list

# ASSIGN DATA
def assign_data(dataframes_list):
    df_buy = dataframes_list[0]
    df_profit = dataframes_list[1]    
    df_sell = dataframes_list[2]
    df_sell_final = dataframes_list[3]
    med_avg_profit_by_zipcode_season = dataframes_list[4]
    
    return df_buy, df_profit, df_sell, df_sell_final, med_avg_profit_by_zipcode_season  
####################################################################################################################################################################################################
# SUGGESTION
def suggestion(df_sell_final, data_mapa, hover_col, df_buy):
    # INTRO - BUSINESS PROBLEM
    st.header('Business Problem') 
    st.markdown('House Rocket is a real estate company whose business model consists in identifying good deals, so that those properties could be bought for an interesting price and futurely sold for a higher price, so that the company could turn in a profit. For this particular case, House Rocket will be operating in King County, which includes Seattle.')
    st.markdown('Obs: The  company and business problem are both fictitious, although the data is real.')
    st.sidebar.title('Options')
    
    # INTRO - SUGGESTIONS
    st.header('Suggestions') 
        
    # BUY FILTERS
    st.sidebar.header('Buy Suggestions and Suggested Buy Prices Options') # filter header
    f_zipcode = st.sidebar.multiselect('Enter Zip Code', df_buy['zipcode'].unique(),key=1) # zipcode filter
    f_season = st.sidebar.multiselect('Select Season', df_buy['ad_season'].unique(),key=2) # ad_season filter
    f_buy = st.sidebar.multiselect('Select Buy Suggestion', df_buy['buy_suggestion'].unique(),key=3) # buy_suggestion filter
    
    # gathering the filters
    if (f_season != []) & (f_zipcode != []) & (f_buy != []): 
        df_buy = df_buy.loc[ (df_buy['ad_season'].isin(f_season)) & (df_buy['zipcode'].isin(f_zipcode)) & (df_buy['buy_suggestion'].isin(f_buy)),:]            
    elif (f_season == []) & (f_zipcode != []) & (f_buy != []):
        df_buy = df_buy.loc[(df_buy['zipcode'].isin(f_zipcode))&(df_buy['buy_suggestion'].isin(f_buy)),:]
    elif (f_season != []) & (f_zipcode == []) & (f_buy != []):  
        df_buy = df_buy.loc[(df_buy['ad_season'].isin(f_season))&(df_buy['buy_suggestion'].isin(f_buy)),:]
    elif (f_season != []) & (f_zipcode != []) & (f_buy == []):  
        df_buy = df_buy.loc[(df_buy['ad_season'].isin(f_season))&(df_buy['zipcode'].isin(f_zipcode)),:]             
    elif (f_season != []) & (f_zipcode == []) & (f_buy == []): 
        df_buy = df_buy.loc[df_buy['ad_season'].isin(f_season), :] 
    elif (f_season == []) & (f_zipcode != []) & (f_buy == []): 
        df_buy = df_buy.loc[df_buy['zipcode'].isin(f_zipcode), :]        
    elif (f_season == []) & (f_zipcode == []) & (f_buy != []): 
        df_buy = df_buy.loc[df_buy['buy_suggestion'].isin(f_buy), :]         
    else:
        df_buy = df_buy.copy() # Caso contrário mostra tudo (default)
        
    # BUY
    st.subheader('Buy Suggestions and Suggested Buy Prices')
    st.markdown('Below are displayed the buy suggestions (whether a property should or should not be bought), as well as suggested buy prices for the properties that got a Yes suggestion.')
    df_buy_final = df_buy[['id','date','ad_season','zipcode','median_price_zipcode_season','asked_price','buy_suggestion','suggested_buy_price']]
    st.write(df_buy_final)           

    # SUGGESTION MAP
    st.subheader('Suggestion Map')
    st.markdown('For better visualization a map is display below with the suggested properties to be bought, as well as their respective suggested buy price.')
    
    # SUGGESTION MAP FILTERS
    min_price_map = int(data_mapa['asked_price'].min())
    max_price_map = int(data_mapa['asked_price'].max())
    st.sidebar.header('Suggestion Map Options') # filter header
    f_price = st.sidebar.slider('Max Buy Price', min_price_map, max_price_map, max_price_map) # buy price filter
   
    properties = data_mapa[(data_mapa['asked_price'] <= f_price)] # making the filter functional
    map_ = px.scatter_mapbox(properties, 
                             lat='lat', 
                             lon='long',
                             size='asked_price', # Size based on the asked price 
                             hover_name='id',
                             hover_data=hover_col, 
                             color='buy_suggestion', # Color based on whether the buy suggestion is 'Yes' or 'No'
                             color_continuous_scale='rdgy', 
                             zoom=8.5, 
                             height=400)
    map_.update_layout(mapbox_style="open-street-map")
    map_.update_layout(height=600, width=1400 ,margin={"r": 0, "t": 0, "l": 0, "b": 0})
    st.plotly_chart(map_)
       
    # SELL
    st.subheader('Suggested Sell Prices and Profits')
    st.markdown('The suggested sell prices are shown below, alonside the profit for each property:')
    
    # SELL FILTERS
    st.sidebar.header('Suggested Sell Prices and Profits')
    min_profit = int(df_sell_final['profit'].min())
    max_profit = int(df_sell_final['profit'].max())
    f_profit = st.sidebar.slider('Max Profit', min_profit, max_profit, max_profit) # profit filter  
    df_sell_final = df_sell_final[(df_sell_final['profit'] <= f_profit)] # making the filter functional   
    
    f_zipcode = st.sidebar.multiselect('Enter Zip Code', df_sell_final['zipcode'].unique(),key=5) # zipcode filter
    f_season = st.sidebar.multiselect('Select Season', df_sell_final['ad_season'].unique(),key=6) # ad_season filter
    
    # gathering the filters
    if (f_season != []) & (f_zipcode != []): 
        df_sell_final = df_sell_final.loc[(df_sell_final['zipcode'].isin(f_zipcode))&(df_sell_final['ad_season'].isin(f_season))]
    elif (f_season == []) & (f_zipcode != []): 
        df_sell_final = df_sell_final.loc[df_sell_final['zipcode'].isin(f_zipcode), :] 
    elif (f_season != []) & (f_zipcode == []): 
        df_sell_final = df_sell_final.loc[df_sell_final['ad_season'].isin(f_season), :]       
    else:
        df_sell_final = df_sell_final.copy() 
    st.write(df_sell_final)   
     
    return None
####################################################################################################################################################################################################    
# FINANCIAL RESULTS
def financial_results(df_profit, data):    
    # INTRO - FINANCIAL RESULTS
    st.header('Financial Results')
    st.markdown('Two interesting metrics to evaluate the financial performance for this solution is the mean and median, grouped by ad_season, zipcode and ad_season with zipcode.')
    st.subheader('Profit Descriptive Analysis')  
    st.write(df_profit)
    st.sidebar.header('Average and Median Profit Options')
    st.subheader('Average and Median Profit by Season and Zipcode')
    
    # MED_AVG_PROFIT FILTERS
    f_zipcode = st.sidebar.multiselect('Enter Zip Code', data['zipcode'].unique()) # zipcode filter
    f_season = st.sidebar.multiselect('Select Season', data['ad_season'].unique()) # ad_season filter
    
    # gathering the filters
    if (f_season != []) & (f_zipcode != []): 
        data = data.loc[(data['zipcode'].isin(f_zipcode))&(data['ad_season'].isin(f_season))] 
    elif (f_season == []) & (f_zipcode != []): 
        data = data.loc[data['zipcode'].isin(f_zipcode), :] 
    elif (f_season != []) & (f_zipcode == []): 
        data = data.loc[data['ad_season'].isin(f_season), :] 
    else:
        data = data.copy()
    st.write(data)
      
    return None
####################################################################################################################################################################################################
# INSIGHTS
def insights():
    st.header('Business Insights')    
    # 1st Insight
    st.subheader('1st Insight: Properties that possess waterfront view are, on average, 212.38% more expensive in comparison to the ones that do not have such feature.')
    st.image('images/waterfront.png',width=900)    
    st.markdown('Usage: House Rocket could focus on buying and selling waterfront view properties, since the profit will be higher in absolut values.')  
    
    # 2nd Insight
    st.subheader('2nd Insight: A property year built is not necessaraly directly proportional to its price, on average.')
    st.image('images/periods.png',width=900) 
    st.markdown('Usage: House Rocket would have higher profits buying and selling properties from around 1985 upwards, as well as from 1900 to 1940.')
    
    # 3rd Insight
    st.subheader('3rd Insight: Properties that do not have a basement are, on average, around 30% cheaper in comparison to the ones that have such feature.')
    st.image('images/basement.png',width=900)      
    st.markdown('Usage: House Rocket could look to buy properties without a basement that have the potential to possess one. Therefore these properties can be sold for a lot higher price.')

    # 4th Insight
    st.subheader('4th Insight: Properties with good views are, on average, around two times more expensive than the ones with not so good views')    
    st.image('images/view.png',width=900) 
    st.markdown('Usage: House Rocket could focus on buying and selling properties with good views, since the profit will be higher in absolut values.')

    # 5th Insight
    st.subheader('5th Insight: Regions bordering Lake Washington produce, on average, 36% more profit in comparison to other regions.')
    st.image('images/lake.png',width=900) 
    st.markdown('Usage: House Rocket could focus on buying and selling properties around Lake Washington, since the profit will be higher in absolut values.') 
     
    return None
####################################################################################################################################################################################################
if __name__ == '__main__':
    # EXTRACT DATA
    path = 'data/' 
    dataframes_list = get_all_data(path)     
    
    # ASSIGN DATA
    df_buy,df_profit,df_sell,df_sell_final,med_avg_profit_by_zipcode_season = assign_data(dataframes_list)

    # BUILD APP    
    suggestion(df_sell_final, df_buy, ['asked_price','buy_suggestion','suggested_buy_price'],df_buy)
    financial_results(df_profit,med_avg_profit_by_zipcode_season)
    insights()