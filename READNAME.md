# Project Title 
This is a 4-person team project which works on a dataset provided by Maryland Small Business Development Center(SBDC), the goal of this project is to uncover factors that determine positive economic impact of business consulting which includes but not limits to:

1. Which (if any) socio-demographic, geographical, and industry(NAICS code) characteristics of pre-venture business do predict successful business start? 

2. Are clients with certain demographics more successful in starting business than others?

3. Are there industries with higher success rate?

4. What are the determinants of securing capital investment by the client? 

5. Which of the available factors (if any) affect the amount of investments?

# Dataset
SBDC provides free individual business consulting and group training to small businesses, both existing and pre-venture ones. The original dataset is 'Maryland SBDC Data 4 UMD Data Challenge 2019.xlsx', which lists business who received individual conulting services during the last 10 years (2009 - 2018) and includes:

- economic impact outcomes achieved vt the clients as a result of consulting
- consulting and traning activity
- characteristics of the business and socio-demographics of the owners.

This is a relative small dataset(1.2MB) with total 17080 rows and 16 columns. 
The columns includes the following:

1. Service Center
2. County
3. Initial Services Sought at First Visit
4. Attended Group Training?
5. Total Counseling Time, hrs
6. Business Status
7. Impact: Capital Investments
8. Impact: Created New Jobs	
9. Impact: Revenue Increase	
10. Impact: Started Business	
11. Company's Total employees	
12. Company's Gross Revenue, 
13. NAICS code	
14. Ownership Gender	
15 Owner's Hispanic Origin	
16. Owner's Race


## Prerequistes
Uses data manipulation and exploration tools to process, and visualized data using business intelligent tools. We use R for the data exploring, python for the data processing and both python and tableau for the visualization.

### software install
1. Python (Anaconda Environment) download: https://www.anaconda.com/distribution/
2. R studio: https://www.rstudio.com/products/rstudio/download/
3. Tableau: https://www.tableau.com/products/desktop/download

## Running the tests
1. Data exploration in R (sample):
```
rm(list=ls())
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
library(data.table)
small_business <- fread("Maryland SBDC Data 4 UMD Data Challenge 2019.csv", sep=",", header = TRUE, stringsAsFactors = TRUE)

for (i in columns(small_business)){
  print (levels(small_business$i)
  }
success <- small_business[`Impact: Started Business`=="Yes"&`Business Status`=="Started with SBDC"]
fail <- small_business[`Impact: Started Business`=="No"&`Business Status`=="Pre-\
```
2. Data processing in Pyton (normalization sample):
```
import numpy as np
import pandas as pd
import sklearn
from sklearn import preprocessing

small_business=pd.read_csv('Maryland SBDC Data 4 UMD Data Challenge 2019.csv',sep=',',
                           header=0)
a = [6,7,8,10]
for i in a:
  print('mean:', np.mean(small_business.iloc[:,i])
  print()
  print('stdev:', np.std(small_business.iloc[:,i])

nan_row=small_business[small_business['Impact: Capital Investments'].isnull()]
small_business.isnull().sum()
small_business=small_business.drop(small_business.index[92])

def scale(df):
    for i in a:
        df.iloc[:,i]=preprocessing.scale(df.iloc[:,i])
    return df
    
small_business=scale(small_business)
small_business.to_excel("small_business scale.xlsx")
```

3. Data visualization in python (sample):
```
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
os.chdir('D:/data challenge')
small_business=pd.read_excel('Maryland SBDC Data 4 UMD Data Challenge 2019.xlsx')

###plot### 
plt.hist(small_business.iloc[:,10], density=True,edgecolor='black')
plt.show
plt.title('counseling time')
plt.xlabel('hours')
plt.ylabel('frequencies')
```
### images 
1. Consulting impacts in terms of Consulting times:
![](presentation/histogram%20visualization.png)

2. Consulting impacts in terms of industry and location:
![](presentation/industry%20histogram.png)
![](presentation/pie%20chart%20distribution.png)

3. Consulting imapcts in terms of Business development:
![](presentation/tableau%20line%20graph.png)

# Conclusion

1. Companies which successfully start up the business spent average more than 14 hours on consulting than the pre-venture companies do. The more a company spends on consulting, the more likely the company will success.

2. Consulting has a significant impacts on the companies which have successfully started up but are less than 1 year in business.

3. The Companies which have a large portion within a county tends to be successful. Overall, the most dominated companies are in Professional, Scientific and Technical Services Industry which obtains roughly about 40% of the business. 








					

