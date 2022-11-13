# SmartcloudService
Piplecloud Group is a commercial cloud business intelligence provider
Our goal is:
1. Be able to process the given data sets in batch    2. find proper cloud services to manage the essential tasks of computing, networking, storage and machine learning. 

## Our work:
1. Data sorce management  (Spark & Snowflake)
2. Data cleaning and visualization  (Amazon Kinesis流数据处理平台)
3. Machine learning pipeline (AWS EMR)
4. ELT pipeline and approach (AWS)
5. Result output and visualization  (API & Tableau)

## Tools:
managed by Pipecloud Group: Team member: Alex, Rex, Ryan, Alvin, Ning Ni, Niu Yue, Luna
use this tool to create pipeline diagram: https://app.diagrams.net/


##细节 放document
## Features
Prediction target
Predict whether the user will order one of his prior ordered products or not. Primary Key is the user-product pair to predict 
whether will be a reorder or not.

User dependent Features
1.Ratio of having reordered product in the user's prior orders.
2.Frequency of the user buying this product.
3.Frequency of the user buying products from the same aisle.
4.On avg the hour the user buys this product at.
5.On avg which day of week the user buys this product at.
6.On avg # of days between 2 user's orders containing this product.
7.On avg the add to cart order by which the user puts this product in his prior orders.

## modeling
data input: all product items, order list, all product id
output data: predicted product id
Pre-build optimized ML model 
        - XGBoost model
