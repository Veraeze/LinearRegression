# Summary for predicting house prices

 Dataset
	•	Source: Boston Housing dataset (via Kaggle)
	•	Shape: 507 rows, 14 columns
	•	Target: MEDV - Median value of owner-occupied homes ($1000s)
	•	Goal: Predict house prices using regression techniques

 Data Cleaning & Exploration
	•	Removed rows with missing/null values (394 rows remained)
	•	Exploratory Data Analysis:
	•	Used .describe() for basic stats
	•	Plotted correlation heatmap to evaluate relationships
	•	Found strong negative correlation between LSTAT and MEDV
	•	Found positive correlation between RM and MEDV

 Baseline Model
	•	Linear Regression (All Features)
	•	R² Score: 0.5807
	•	Used train_test_split (80/20 split)


 Improvement Techniques Tried

1. Feature Selection
	•	Selected: RM, LSTAT, PTRATIO, ZN
	•	Result: R² dropped to 0.5486 ➝ Discarded

2. Polynomial Features
	•	Degree 2 Polynomial
	•	Tried on:
	•	Selected features: R² = 0.6043
	•	All features: R² = 0.6259 

3. Regularization
	•	With PolynomialFeatures(degree=2) on all features:
	•	Ridge Regression: R² = 0.6283
	•	Lasso Regression: R² = 0.6484 

4. Interpretability
	•	Visualized actual vs predicted prices with matplotlib
	•	Learned how correlation maps help in feature selection

 Final Model (so far)
	•	Lasso Regression + PolynomialFeatures + StandardScaler
	•	R² Score: 0.6484
 

 # Summary for Student Performance Project

Student Performance Regression Project

This project explores the predictability of student academic scores using demographic and categorical data.

Dataset
	•	Source: Open educational dataset (gender, race/ethnicity, parental education, lunch, test preparation course)
	•	Target Variables: math score, reading score, writing score
	•	New Feature: average_score = mean of the three scores

Objective

To build regression models predicting student scores based only on demographic features, and evaluate the effectiveness of those features.

Steps Taken
1.	Data Cleaning & Preparation
	•	Created an average_score column.
	•	One-hot encoded all categorical features.
	•	Split into training and test sets using train_test_split. 
2. Exploratory Data Analysis
	•	Checked correlation between each subject score and the average.
	•	Found strong internal correlation between scores but weaker link with demographics.
3.	Modeling
    •	Built a pipeline using ColumnTransformer + Pipeline for clean preprocessing and modeling.
    •	Trained 5 regression models:
    i.  Linear Regression
    ii. Random Forest Regressor
    iii.Decision Tree Regressor
    iv.	Gradient Boosting Regressor
    v.	K-Nearest Neighbors Regressor
4.	Evaluation
   •	Used R² Score to evaluate model accuracy for each subject.
	Findings:
   •	All models performed poorly using only demographic features.
   •	Best R² scores:
   •	Math: ~0.34
   •	Reading: ~0.18
   •	Writing: ~0.28
   •	Demographics alone are insufficient to accurately predict academic scores.
   •    The quality of input features significantly affects model performance.

# Summary for Toyota Car Price Prediction Project

Toyota Car Price Regression Project

This project analyzes the predictability of used Toyota car prices based on multiple vehicle features using regression techniques.

Dataset
	•	Source: Open Toyota used car dataset from kaggle
	•	Features:
	•	Year, Mileage, Engine Size, Transmission, Fuel Type, Tax, MPG, Model
	•	Target Variable: Price

Objective

To build regression models that predict the price of used Toyota cars based on vehicle specifications, and to evaluate how different feature encoding choices affect model performance.

Steps Taken

1. Data Cleaning & Preparation
	•	Handled categorical variables using two approaches:
	•	One-Hot Encoding for Transmission, Fuel Type.
	•	Label Encoding vs Ordinal Encoding tested for Model feature.
	•	Split data into training and testing sets using train_test_split.

2. Exploratory Data Analysis
	•	Visualized feature distributions and checked correlations.
	•	Found strong correlation between Price and features like Year, Mileage, Engine Size.
	•	Categorical variables (Model, Transmission, Fuel Type) required proper encoding due to their mixed nature.

3. Modeling
	•	Built a pipeline using ColumnTransformer and Pipeline for clean preprocessing and modeling.
	•	Trained linear regression model

4. Evaluation
	•	Used R² Score as evaluation metric.
	•	Tested how encoding strategies impacted model accuracy:
	•	With One-Hot Encoding for Model: R² ≈ 0.90
	•	With Ordinal Encoding for Model: R² ≈ 0.927
	•	Findings:
	•	Certain models benefit from ordinal encoding when categorical variables have many levels.
	•	Features like Year and Mileage are strong predictors.
	•	Proper encoding of high-cardinality categorical features significantly improves model performance.