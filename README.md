<h1 align="center">House Rocket Insights Project</h1>
<p align="center">Data Science Project</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/191957066-c9699023-eb0e-4e20-9508-869ee8038ecf.jpg" alt="drawing" width="750"/>
</p>

# 1. **House Rocket and Business Problem**
<p align="justify"> House Rocket is a real estate company whose business model consists in identifying good deals, so that those properties could be bought for an interesting price and futurely sold for a higher price, so that the company could turn in a profit. For this particular case, House Rocket will be operating in King County, which includes Seattle. </p>

*Obs: The  company and business problem are both fictitious, although the data is real.*

This **Data Science** project is focused on solving two problems: 

 - **Problem 1: Which properties should House Rocket buy and for which suggested price?**
 - **Problem 2: Once a property is bought, for which price should it be sold?**

*The in-depth Python code explanation is available in [this](https://github.com/brunodifranco/project-house-rocket-insights/blob/main/jupyter-house-rocket.ipynb) Jupyter Notebook.*

# 2. **Data Overview**
The data was collected from [Kaggle](https://www.kaggle.com/). This [dataset](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction) contains house sale prices for King County, from May 2014 to May 2015. The features descriptions are available below:

| Feature | Definition |
|---|---|
| id | Unique ID for each home sold |
| date | Date of the home sale |
| price | Price of each home sold |
| bedrooms | Number of bedrooms |
| bathrooms | Number of bathrooms, where .5 accounts for a room with a toilet but no shower |
| sqft_living | Square footage of the apartments interior living space |
| sqft_lot | Square footage of the land space |
| floors | Number of floors |
| waterfront | A dummy variable for whether the apartment was overlooking the waterfront or not |
| view | An index from 0 to 4 of how good the view of the property was |
| condition  | An index from 1 to 5 on the condition of the apartment |
| grade  | An index from 1 to 13, where 1-3 falls short of building construction and design, 7 has an average level of construction and design, and 11-13 have a high quality level of construction and design. |
| sqft_above | The square footage of the interior housing space that is above ground level |
| sqft_basement | The square footage of the interior housing space that is below ground level |
| yr_built | The year the house was initially built |
| yr_renovated | The year of the house’s last renovation |
| zipcode | What zipcode area the house is in |
| lat | Lattitude |
| long | Longitude |
| sqft_living15 | The square footage of interior housing living space for the nearest 15 neighbors |
| sqft_lot15 | The square footage of the land lots of the nearest 15 neighbors |


# 3. **Assumptions**

 - Location in real estate is undoubtedly a decisive factor in price evaluation.
 - The address information for these properties was gathered by using the two created modules: [address.py](https://github.com/brunodifranco/project-house-rocket-insights/blob/main/modules/address.py) and [defs.py](https://github.com/brunodifranco/project-house-rocket-insights/blob/main/modules/defs.py).
 - So that the business problems could be solved the **ad_season** feature was created. It's a column that shows on which season the property was announced in the real estate market (spring, summer, fall or winter).

# 4. **Solution Plan**
## 4.1. How will both problems be solved?

### **Problem 1: Which properties should House Rocket buy and for which suggested price?**
<p align="justify"> To solve this problem, we firstly need to analyse the properties by their location, because in real estate, location is undoubtedly a decisive factor in price evaluation. One interesting metric in this case is to calculate the price median by each zipcode, as the median isn't influenced by extreme values (outliers) in the data. </p>

The properties that will receive a buy suggestion will be the ones that fulfill the two following rules:

- Their asked price has to be lower than the median price for that region
- The property needs to be in good conditions, which means condition >= 3

<p align="justify"> As for the suggested price, the density by region will be taken into account, which means that for properties in regions that have a higher number of real estate ads it's viable to offer lower prices, and vice-versa. Therefore the rule for suggested buy prices is: </p> 

- From 0 to 204 properties in the region => Offer the asked price 
- From 205 to 282 properties in the region => Offer 3% less than the asked price
- From 283 to 408 properties in the region => Offer 4% less than the asked price
- From 409 properties upwards => Offer 5% less than the asked price

### **Problem 2: Once a property is bought, for which price should it be sold?**

<p align="justify"> To suggest a sell price, again the density by region will be considered, since for regions where the number of real estate ads is lower it's possible to sell the property for a higher price, and vice-versa. Hence, a reasonable rule for suggested sell prices is: </p>

- From 0 to 204 properties in the region => Sell for 16% than the suggested buy price 
- From 205 to 282 properties in the region => Sell for 14% than the suggested buy price
- From 283 to 408 properties in the region => Sell for 12% than the suggested buy price
- From 409 properties upwards => Sell for 10% than the suggested buy price

<p align="justify"> <i>It's important to point out that selling a property for 10-16% more than the paid price is just a suggestion, so that the selling prices are realistic, since selling a property on a short run for say 30-40% more, although it can happen, it seems unlikely (or it would take too long to sell).</i> </p>

## 4.2. What will be delivered?
 - Solution to Problem 1:  
    
    - [Buy Suggestion Table](https://github.com/brunodifranco/project-house-rocket-insights/tree/main/tables/buy-suggestions): Contains buy suggestions and suggested buy prices

 - Solution to Problem 2: 
    - [Sell Suggestion Table](https://github.com/brunodifranco/project-house-rocket-insights/tree/main/tables/sell-sugestions): Contains suggested sell prices and profit

 - Financial Results:
    - [Profit descriptive analysis](https://github.com/brunodifranco/project-house-rocket-insights/blob/main/financial-results/profit-descriptive-analysis.csv)
    - [Average and median profit grouped by ad_season](https://github.com/brunodifranco/project-house-rocket-insights/blob/main/financial-results/med-avg-profit-by-season.csv)
    - [Average and median profit grouped by zipcode](https://github.com/brunodifranco/project-house-rocket-insights/blob/main/financial-results/med-avg-profit-by-zipcode.csv)
    - [Average and median profit grouped by ad_season and zipcode](https://github.com/brunodifranco/project-house-rocket-insights/blob/main/financial-results/med-avg-profit-by-zipcode-season.csv)
    - [House Rocket Cloud App](https://brunodifranco-house-rocket-app-house-rocket-app-4dn0re.streamlitapp.com/): App deployed using Streamlit Cloud containing all tables (Buy Suggestion Table, Sell Suggestion Table and Financial Results Tables) with filters and a Buy Suggestion Map, as well as data insights.
 

## 4.3. Used tools
- [Python 3.9.12](https://www.python.org/downloads/release/python-3912/)
- [VSCode](https://code.visualstudio.com/)
- [Jupyter Notebook](https://jupyter.org/)
- [Streamlit](https://streamlit.io/)
- [Streamlit Cloud](https://streamlit.io/cloud)
- [Git](https://git-scm.com/)
- [Github](https://github.com/)

# 5. **Business Insights**

 - ### 1st - Properties that possess waterfront view are, on average, 212.38% more expensive in comparison to the ones that do not have such feature.
<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/191962514-70edbf52-c08b-4aa1-9d46-9db3ebd39eca.png" alt="drawing" width="750"/>
</p>

#### **Usage**: House Rocket could focus on buying and selling waterfront view properties, since the profit will be higher in absolut values. 
--- 
- ### 2nd - Properties that do not have a basement are, on average, 27.71% cheaper in comparison to the ones that have such feature.
<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/191962495-7f9303a2-8c91-47ab-9940-dc984cc0fbc5.png" alt="drawing" width="750"/>
</p>

#### **Usage**: House Rocket could look to buy properties without a basement that have the potential to possess one. Therefore these properties can be sold for a lot higher price. 
---
- ### 3rd - Properties with good views are, on average, 1.89 times more expensive than the ones with not so good views
<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/191962502-adfbcb5e-2261-46f3-8d1d-1bb8d2281405.png" alt="drawing" width="750"/>
</p>

#### **Usage**: House Rocket could focus on buying and selling properties with good views, since the profit will be higher in absolut values.
---
- ### 4th - Regions bordering Lake Washington produce, on average, 36.23% more profit in comparison to other regions.
<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/192010463-9a0d6027-c6fa-4b4c-9e49-a539873a6ba2.png" alt="drawing" width="750"/>
</p>

#### **Usage**: House Rocket could focus on buying and selling properties around Lake Washington, since the profit will be higher in absolut values.
---
- ### 5th - Properties with the lowest prices (on average) were built from 1941 to 1983.
<p align="center">
  <img src="https://user-images.githubusercontent.com/66283452/191962508-06aaa6af-a466-4181-8d23-e0e1ca88548f.png" alt="drawing" width="750"/>
</p>

#### **Usage**: House Rocket would have higher profits buying and selling properties built from the mid 1980's upwards, as well as the ones built from 1900 to 1940.

# 6. **Financial Results**

<p align="justify"> Three interesting metrics to evaluate the financial performance for this solution is the profit mean and median (grouped by ad_season, zipcode and ad_season with zipcode), as well as the total profit. This in-depth information can be found in <a href="https://github.com/brunodifranco/project-house-rocket-insights/tree/main/financial-results">here</a>. As for the profit for each property it can be checked in the <a href="https://brunodifranco-house-rocket-app-house-rocket-app-4dn0re.streamlitapp.com/">House Rocket Cloud App</a>, where filters can also be applied for better visualization. </p>

<p align="justify"> <b> If the solution strategy used in this project were applied by House Rocket the total obtained profit would be US$ 473,094,328.48, with an average profit of US$ 45,337.26 per property. The main profit metrics are displayed below: </b></p>

<div align="center">
 
| **Metric** | **US$** |
|---|---|
| Total Profit | 473,094,328.48 |
| Profit Mean | 45,337.26 |
| Profit Median | 39,995.00 |
| Min Profit | 8,217.50 |
| Max Profit | 350,036.80 |
 
</div>

# 7. **Conclusion**
In this project the two main objectives were accomplished:

 - A feasible solution was found for both business problems, leading to profitable results.
 - Five interesting and useful insights were found through Exploratory Data Analysis (EDA).

 We also managed to deliver tables with in-depth financial results, as well as buy and sell suggestion tables. All this information can be filtered by using the [House Rocket Cloud App](https://brunodifranco-house-rocket-app-house-rocket-app-4dn0re.streamlitapp.com/), that also has the five business insights and a interactive Buy Suggestion Map.   
 
# 8. **Next Steps**
<p align="justify"> Further on, this solution could be improved by using <a href="https://www.imsl.com/blog/what-is-regression-model">regression models</a> to determine wheter a property is in a good buying price, and for which price it could be bought and sold. Another interesting study would be to produce a market research, so that data about clients could be collected. Then, a <a href="https://machinelearningmastery.com/clustering-algorithms-with-python/">clustering algorithm</a> could be applied to identify what types of property features each group of customers would prefer. </p>

# Contact

- brunodifranco99@gmail.com

- [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/BrunoDiFrancoAlbuquerque/)
