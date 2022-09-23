# **HOUSE ROCKET INSIGHTS PROJECT**

ADICIONAR FOTO AQUI


## 1. **House Rocket and Business Problem**
House Rocket is a real estate company whose business model consists in identifying good deals, so that those properties could be bought for an interesting price and futurely sold for a higher price, so that the company could turn in a profit. For this particular case, House Rocket will be operating in King County, which includes Seattle. 

*Obs: The  company and business problem are both fictitious, although the data is real.*

This project is focused on solving two problems: 

**Problem 1: Which properties should House Rocket buy and for which suggested price?**
**Problem 2: Once a property is bought, for which price should it be sold?**


## 2. **Data Overview**


## 3. **Business Assumptions**


## 4. **Solution Plan**
### 4.1. How will both problems be solved?

#### **Problem 1: Which properties should House Rocket buy and for which suggested price?**

To solve this problem, we firstly need to analyse the properties by their location, because in real estate, location is undoubtedly a decisive factor in price evaluation. One interesting metric in this case is to calculate the price median by each zipcode, as the median isn't influenced by extreme values (outliers) in the data. 

The properties that will receive a buy suggestion will be the ones that fulfill the two following rules:

- Their asked price has to be lower than the median price for that region
- The property needs to be in good conditions, which means condition >= 3

As for the suggested price, the density by region will be taken into account, which means that for properties in regions that have a higher number of real estate ads it's viable to offer lower prices, and vice-versa. Therefore the rule for suggested buy prices is:

- From 0 to 204 properties in the region => Offer the asked price 
- From 205 to 282 properties in the region => Offer 3% less than the asked price
- From 283 to 408 properties in the region => Offer 4% less than the asked price
- From 409 properties upwards => Offer 5% less than the asked price

#### **Problem 2: Once a property is bought, for which price should it be sold?**

 To suggest a sell price, again the density by region will be considered, since for regions where the number of real estate ads is lower it's possible to sell the property for a higher price, and vice-versa. Hence the rule for suggested sell prices is:

- From 0 to 204 properties in the region => Sell for 16% than the suggested buy price 
- From 205 to 282 properties in the region => Sell for 14% than the suggested buy price
- From 283 to 408 properties in the region => Sell for 12% than the suggested buy price
- From 409 properties upwards => Sell for 10% than the suggested buy price

### 4.2. What will be delivered?
 - Solution to Problem 1:  
    
    - [Buy Suggestion Table: ](https://github.com/brunodifranco/project-house-rocket-insights/tree/main/tables/buy-suggestions): Contains buy suggestions and suggested buy prices
    - [Suggestion Map](): Contains suggested properties to be bought, as well as their respective suggested buy price.

 - Solution to Problem 2: 
    - [Sell Suggestion Table](https://github.com/brunodifranco/project-house-rocket-insights/tree/main/tables/sell-sugestions): Contains suggested sell prices and profit

 - Financial Results:
    - [Density Map](): Contains the average profit for each zipcode
    - [Profit descriptive analysis](https://github.com/brunodifranco/project-house-rocket-insights/blob/main/financial-results/profit-descriptive-analysis.csv)
    - [Average and median profit grouped by ad_season](https://github.com/brunodifranco/project-house-rocket-insights/blob/main/financial-results/med-avg-profit-by-season.csv)
    - [Average and median profit grouped by zipcode](https://github.com/brunodifranco/project-house-rocket-insights/blob/main/financial-results/med-avg-profit-by-zipcode.csv)
    - [Average and median profit grouped by ad_season and zipcode](https://github.com/brunodifranco/project-house-rocket-insights/blob/main/financial-results/med-avg-profit-by-zipcode-season.csv)

 - [House Rocket  Cloud App](): App deployed in Heroku containing all tables (Buy Suggestion Table, Sell Suggestion Table and Financial Results Tables) with filters, maps (Suggestion Map and Density Map), as well as insights from the data.  

### 4.3. Used tools
 ADICIONAR OS LINKS AQUI
- Python
- VSCode
- Jupyter Notebook
- Streamlit
- Git
- Github
- Heroku

## 2. **Data Overview**


The data was collected from [Kaggle](https://www.kaggle.com/), and are available in this [link](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction). 



According to [Kaggle](https://www.kaggle.com/) this dataset contains house sale prices for King County, which includes Seattle. It includes homes sold between May 2014 and May 2015.










**a**


1. QUESTÃO DE NEGÓCIO (O que você quer resolver?)
1




3. PREMISSAS DO NEGÓCIO (assumptions)
4. PLAJANEMENTO DA SOLUÇÃO
5. OS 5 PRINCIPAIS INSIGHTS DE NEGÓCIO (5 hipóteses (descobertas acionáveis) - pode ser mais ou menos que 5)
6. RESULTADOS FINANCEIROS PARA O NEGÓCIO
7. CONCLUSÃO (se o objetivo foi alcançado?)
8. PRÓXIMOS PASSOS (como melhorar a solução?)

