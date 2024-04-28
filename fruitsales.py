# import pandas
import pandas as pd
#create a data frame with the excerise's specified requirements
fruit_sales = pd.DataFrame({'Apples': [35, 21], 'Bananas': [41, 34]}, index=['2017 Sales', '2018 Sales'])

#save data frame to a csv
fruit_sales.to_csv('fruit.csv')