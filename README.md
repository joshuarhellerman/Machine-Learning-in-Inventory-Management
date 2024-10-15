Machine Learning in Inventory Management

This repository contains a structured approach to implementing machine learning for sales prediction and inventory management. The project is divided into several modules, each focused on different aspects of the machine learning pipeline, from data collection and cleaning to model comparison.

Project Structure

Data Collection and Cleaning:
Script: Data Collection and Cleaning.ipynb
Description: The first step involves collecting the raw data from various sources and performing data cleaning. This script ensures that the data is properly formatted, missing values are handled, and noisy data is cleaned. The output of this script is a clean dataset ready for further analysis.

Visual and Statistical Data Exploration:
Script: Visual and Statistical Data Exploration.ipynb
Description: After cleaning the data, this step involves visualizing the data and conducting statistical exploration to better understand the underlying patterns, relationships, and distributions. This step provides insights into the data's structure, guiding the subsequent transformation and modeling steps.

Data Transformation:
Script: Data Transformation.ipynb
Description: In this module, data transformations such as scaling, normalization, and dimensionality reduction (PCA) are applied to the dataset. These transformations ensure that the data is in a suitable format for machine learning algorithms to process efficiently.

Predictive Modeling:
Scripts:
Linear Regression.ipynb
Ridge Regression.ipynb
Lasso Regression.ipynb
Random Forest.ipynb
LightGBM.ipynb
XGBoost.ipynb
CatBoost.ipynb
RNN.ipynb
LSTM.ipynb
Description: This section contains various machine learning models used to predict weekly sales. Each script implements a specific model, and hyperparameter tuning is performed using RandomizedSearchCV to optimize the model's performance. Each model generates predictions and calculates performance metrics such as MSE, RMSE, MAE, and R².

Inter-Model Comparison:
Script: Intermodel Comparison.ipynb
Description: This final step compares the performance of all the predictive models using various evaluation metrics. The comparison is visualized using bar plots for metrics like RMSE, MAE, and R². The training times of the models are also compared, allowing you to identify the best-performing model for sales prediction.
Results Files

Results CSVs:
linear_regression_results.csv
ridge_regression_results.csv
lasso_regression_results.csv
random_forest_results.csv
lightgbm_results.csv
xgboost_results.csv
catboost_results.csv
rnn_results.csv
lstm_results.csv
Each results file contains the performance metrics for the respective model, which are then used in the inter-model comparison step.

How to Run the Project

Clone the Repository:
bash
Copy code
git clone https://github.com/joshuarhellerman/Machine-Learning-in-Inventory-Management.git
cd Machine-Learning-in-Inventory-Management
Install Dependencies: Make sure to install all required Python libraries by running:
bash
Copy code
pip install -r requirements-inv.txt
Run the Notebooks:
Begin with Data Collection and Cleaning.ipynb, then proceed through each notebook in the order described above.
After running the predictive models, use Intermodel Comparison.ipynb to compare their performance.

Conclusion

This project demonstrates a complete machine learning pipeline for sales prediction and inventory management, including data preprocessing, model building, and comparison of various machine learning models. The goal is to optimize sales predictions to help manage inventory efficiently.
