# LinearRegression
Summary of Model Improvement Journey

 Dataset
	•	Source: Boston Housing dataset (via Kaggle)
	•	Shape: 507 rows, 14 columns
	•	Target: MEDV — Median value of owner-occupied homes ($1000s)
	•	Goal: Predict house prices using regression techniques

⸻

 Data Cleaning & Exploration
	•	Removed rows with missing/null values (394 rows remained)
	•	Exploratory Data Analysis:
	•	Used .describe() for basic stats
	•	Plotted correlation heatmap to evaluate relationships
	•	Found strong negative correlation between LSTAT and MEDV
	•	Found positive correlation between RM and MEDV

⸻

 Baseline Model
	•	Linear Regression (All Features)
	•	R² Score: 0.5807
	•	Used train_test_split (80/20 split)

⸻

 Improvement Techniques Tried

1. Feature Selection
	•	Selected: RM, LSTAT, PTRATIO, ZN
	•	Result: R² dropped to 0.5486 ➝ Discarded

2. Polynomial Features
	•	Degree 2 Polynomial
	•	Tried on:
	•	Selected features: R² = 0.6043
	•	All features: R² = 0.6259 ✅

3. Regularization
	•	With PolynomialFeatures(degree=2) on all features:
	•	Ridge Regression: R² = 0.6283
	•	Lasso Regression: R² = 0.6484 ✅

4. Interpretability
	•	Visualized actual vs predicted prices with matplotlib
	•	Learned how correlation maps help in feature selection

⸻

 Final Model (so far)
	•	Lasso Regression + PolynomialFeatures + StandardScaler
	•	R² Score: 0.6484